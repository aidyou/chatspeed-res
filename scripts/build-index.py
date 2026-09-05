#!/usr/bin/env python3
"""Validate resource files and generate the public catalog.

Only Python's standard library is used so the catalog check can run in CI
before JavaScript dependencies are installed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "resources"
PUBLIC_CATALOG = ROOT / "public" / "catalog"
GENERATED_DATA = ROOT / "src" / "data" / "generated"
DOCS_ROOT = ROOT / "docs"
LOCALES = ("en", "zh-Hans")
# Active locale during docs generation. localized() falls back to this so every
# localized(...) call site (including ones we must not hand-edit) becomes
# locale-aware. write_docs sets it per generated locale.
_LOCALE = "en"
CHANNELS = ("mcp", "models", "free-ai")
COMMON_FIELDS = (
    "id",
    "channel",
    "name",
    "description",
    "detail",
    "categories",
    "tags",
    "website",
    "status",
    "lastVerifiedAt",
)
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SECRET_KEY_PATTERN = re.compile(
    r"(?:^|_)(?:api[_-]?key|password|passwd|secret|bearer[_-]?token|authorization|cookie)(?:$|_)",
    re.IGNORECASE,
)

PLACEHOLDER_TOKEN_PATTERN = re.compile(
    r"(?:\*+|xxx+|your[\w-]*|you[\w-]*|api[\w-]*key|token|placeholder|your|my|the|a|an)"
    r"|^[^a-z0-9]+$"
    r"|<[^>]*>|\{[^}]*\}|[^\x00-\x7f]",
    re.IGNORECASE,
)


def looks_like_placeholder(token: str) -> bool:
    """Return True when a sk-/bearer token is clearly a documentation placeholder."""
    if not token:
        return True
    if PLACEHOLDER_TOKEN_PATTERN.search(token):
        return True
    # A real secret is a longer alphanumeric token; short words are prose
    if len(re.sub(r"[^a-z0-9]", "", token)) < 8:
        return True
    return False


class ValidationError(Exception):
    """A resource validation error with a file-relative location."""


def fail(path: Path, message: str) -> None:
    raise ValidationError(f"{path.relative_to(ROOT)}: {message}")


def load_json(path: Path) -> object:
    try:
        with path.open(encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, json.JSONDecodeError) as error:
        fail(path, f"invalid JSON ({error})")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ensure_localized(path: Path, field: str, value: object) -> None:
    if not isinstance(value, dict):
        fail(path, f"{field} must be an object with localized values")
    missing = [locale for locale in LOCALES if not isinstance(value.get(locale), str) or not value[locale].strip()]
    if missing:
        fail(path, f"{field} is missing non-empty locales: {', '.join(missing)}")


def ensure_url(path: Path, field: str, value: object) -> None:
    if not isinstance(value, str):
        fail(path, f"{field} must be a URL string")
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        fail(path, f"{field} must be an absolute HTTP(S) URL")


def check_secrets(path: Path, value: object, location: str = "") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            key_location = f"{location}.{key}" if location else str(key)
            if SECRET_KEY_PATTERN.search(str(key)) and key != "keyApplyUrl":
                fail(path, f"secret-like field is not allowed: {key_location}")
            check_secrets(path, child, key_location)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            check_secrets(path, child, f"{location}[{index}]")
    elif isinstance(value, str):
        lowered = value.lower()
        if re.search(r"\bghp_[a-z0-9]{10,}", lowered):
            fail(path, f"possible credential found at {location}")
        # sk-/bearer tokens that look like real secrets (not doc placeholders)
        sk_bearer = re.finditer(r"(?:\bsk-|\bbearer\s+)([^\s\"'`]+)", lowered)
        for match in sk_bearer:
            token = match.group(1)
            if looks_like_placeholder(token):
                continue
            fail(path, f"possible credential found at {location}")


def validate_mcp(path: Path, resource: dict) -> None:
    mcp = resource.get("mcp")
    if not isinstance(mcp, dict):
        fail(path, "mcp must be an object")
    transport = mcp.get("type")
    if transport not in ("stdio", "sse", "http"):
        fail(path, "mcp.type must be stdio, sse, or http")
    if transport == "stdio":
        if not isinstance(mcp.get("command"), str) or not mcp["command"].strip():
            fail(path, "mcp.command is required for stdio")
        if not isinstance(mcp.get("args", []), list) or not all(isinstance(item, str) for item in mcp["args"]):
            fail(path, "mcp.args must be an array of strings")
    else:
        ensure_url(path, "mcp.url", mcp.get("url"))
    env = mcp.get("env", [])
    if not isinstance(env, list) or not all(isinstance(item, list) and len(item) == 2 and all(isinstance(x, str) for x in item) for item in env):
        fail(path, "mcp.env must be an array of [name, placeholder] pairs")


def validate_provider(path: Path, resource: dict) -> None:
    provider = resource.get("provider")
    if not isinstance(provider, dict):
        fail(path, "provider must be an object")
    if provider.get("protocol") not in ("openai", "ollama", "gemini", "claude", "huggingface"):
        fail(path, "provider.protocol is unsupported")
    for field in ("name", "desc", "baseUrl"):
        if not isinstance(provider.get(field), str):
            fail(path, f"provider.{field} must be a string")
    ensure_url(path, "provider.baseUrl", provider.get("baseUrl"))
    models = provider.get("models")
    if not isinstance(models, list):
        fail(path, "provider.models must be an array")
    model_ids = set()
    for index, model in enumerate(models):
        if not isinstance(model, dict) or not isinstance(model.get("id"), str) or not model["id"].strip():
            fail(path, f"provider.models[{index}].id is required")
        if model["id"] in model_ids:
            fail(path, f"duplicate model ID: {model['id']}")
        model_ids.add(model["id"])


def validate_free_ai(path: Path, resource: dict) -> None:
    free_ai = resource.get("freeAi")
    if not isinstance(free_ai, dict):
        fail(path, "freeAi must be an object")
    if free_ai.get("accessType") not in ("web", "api", "web-and-api"):
        fail(path, "freeAi.accessType is unsupported")
    if not isinstance(free_ai.get("requiresLogin"), bool) or not isinstance(free_ai.get("hasFreeTier"), bool):
        fail(path, "freeAi.requiresLogin and freeAi.hasFreeTier must be booleans")
    ensure_localized(path, "freeAi.freeLimit", free_ai.get("freeLimit"))
    if free_ai.get("availability") not in ("global", "regional", "unknown"):
        fail(path, "freeAi.availability is unsupported")
    for field in ("signupUrl", "freePolicyUrl"):
        if free_ai.get(field):
            ensure_url(path, f"freeAi.{field}", free_ai[field])
    if free_ai.get("registrationRestriction") is not None:
        ensure_localized(path, "freeAi.registrationRestriction", free_ai["registrationRestriction"])
    free_quotas = free_ai.get("freeQuotas")
    if free_quotas is not None:
        if not isinstance(free_quotas, list) or not free_quotas:
            fail(path, "freeAi.freeQuotas must be a non-empty array")
        for index, quota in enumerate(free_quotas):
            if not isinstance(quota, dict):
                fail(path, f"freeAi.freeQuotas[{index}] must be an object")
            for field in ("model", "quota", "frequency"):
                ensure_localized(path, f"freeAi.freeQuotas[{index}].{field}", quota.get(field))
    integrations = free_ai.get("integrations", {})
    if not isinstance(integrations, dict):
        fail(path, "freeAi.integrations must be an object")
    chat_speed_model = integrations.get("chatSpeedModel")
    if chat_speed_model is not None:
        if not isinstance(chat_speed_model, dict) or not isinstance(chat_speed_model.get("providerRef"), str) or not isinstance(chat_speed_model.get("importable"), bool):
            fail(path, "freeAi.integrations.chatSpeedModel must contain providerRef and importable")


def validate_resource(path: Path, expected_channel: str) -> dict:
    value = load_json(path)
    if not isinstance(value, dict):
        fail(path, "resource must be a JSON object")
    for field in COMMON_FIELDS:
        if field not in value:
            fail(path, f"missing required field: {field}")
    resource_id = value["id"]
    if not isinstance(resource_id, str) or not ID_PATTERN.fullmatch(resource_id):
        fail(path, "id must be kebab-case")
    if value["channel"] != expected_channel:
        fail(path, f"channel must be {expected_channel} for this directory")
    for field in ("name", "description", "detail"):
        ensure_localized(path, field, value[field])
    if not isinstance(value["categories"], list) or not value["categories"] or not all(isinstance(item, str) for item in value["categories"]):
        fail(path, "categories must be a non-empty array of strings")
    if not isinstance(value["tags"], list) or not all(isinstance(item, str) and item.strip() for item in value["tags"]):
        fail(path, "tags must be an array of non-empty strings")
    ensure_url(path, "website", value["website"])
    if value["status"] not in ("active", "review", "deprecated"):
        fail(path, "status must be active, review, or deprecated")
    if not isinstance(value["lastVerifiedAt"], str) or not DATE_PATTERN.fullmatch(value["lastVerifiedAt"]):
        fail(path, "lastVerifiedAt must use YYYY-MM-DD")
    try:
        dt.date.fromisoformat(value["lastVerifiedAt"])
    except ValueError:
        fail(path, "lastVerifiedAt is not a valid date")
    if expected_channel == "mcp":
        validate_mcp(path, value)
    elif expected_channel == "models":
        validate_provider(path, value)
    else:
        validate_free_ai(path, value)
    check_secrets(path, value)
    return value


def resource_score(resource: dict) -> float:
    """Return the numeric quality score used for ordering (default 0.0)."""
    value = resource.get("score")
    if isinstance(value, (int, float)):
        return float(value)
    return 0.0


def build_catalog() -> tuple[dict, dict[str, list[dict]]]:
    categories = load_json(RESOURCES / "categories.json")
    if not isinstance(categories, dict):
        fail(RESOURCES / "categories.json", "must be an object")
    resources: list[dict] = []
    by_channel: dict[str, list[dict]] = {channel: [] for channel in CHANNELS}
    seen_ids: set[str] = set()
    for channel in CHANNELS:
        directory = RESOURCES / channel
        directory.mkdir(parents=True, exist_ok=True)
        for path in sorted(directory.glob("*.json")):
            resource = validate_resource(path, channel)
            if resource["id"] in seen_ids:
                fail(path, f"duplicate resource ID: {resource['id']}")
            seen_ids.add(resource["id"])
            allowed_categories = categories.get(channel, [])
            invalid_categories = sorted(set(resource["categories"]) - set(allowed_categories))
            if invalid_categories:
                fail(path, f"unknown categories: {', '.join(invalid_categories)}")
            resources.append(resource)
            by_channel[channel].append(resource)
    # Order by status (active first, review/deprecated last), then quality score
    # (descending), then id for stability, so that confirmed and well-made
    # resources appear first while entries still under review sit at the end.
    status_priority = {"active": 0, "review": 1, "deprecated": 2}
    sort_key = lambda r: (status_priority.get(r["status"], 1), -resource_score(r), r["id"])
    for channel in CHANNELS:
        by_channel[channel].sort(key=sort_key)
    resources.sort(key=sort_key)
    for resource in resources:
        if resource["channel"] != "free-ai":
            continue
        free_ai = resource.get("freeAi", {})
        references = [free_ai.get("modelProviderRef")]
        integration = free_ai.get("integrations", {}).get("chatSpeedModel")
        if integration:
            references.append(integration.get("providerRef"))
        for ref in filter(None, references):
            if ref not in {item["id"] for item in resources if item["channel"] == "models"}:
                fail(RESOURCES / "free-ai" / f"{resource['id']}.json", f"unknown model provider reference: {ref}")
    catalog = {
        "version": 1,
        "generatedAt": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "channels": list(CHANNELS),
        "resources": resources,
    }
    return catalog, by_channel


def localized_search_text(resource: dict) -> str:
    values = []
    for field in ("name", "description"):
        values.extend(resource[field].values())
    values.extend(resource["categories"])
    values.extend(resource["tags"])
    return " ".join(values).lower()


def localized(resource: dict, field: str, locale: str | None = None) -> str:
    values = resource[field]
    locale = locale or _LOCALE
    return values.get(locale) or values.get("en") or next(iter(values.values()))


def markdown_link(url: str, label: str) -> str:
    return f"[{label}]({url})"


# Upstream README content in the localized `description`/`detail` fields can contain
# raw HTML, Vue `{{ }}` interpolation, and relative asset links. English entries in
# particular are dirtier than Chinese and break the VuePress markdown->Vue compile.
# These sanitizers make arbitrary resource content safe to emit as markdown pages.
def _strip_tags(text: str) -> str:
    return re.sub(r"</?[a-zA-Z][^>]*>", " ", text)


def _plain_summary(text: str, limit: int = 200) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = _strip_tags(text)
    text = re.sub(r"[`*_#>]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return (text[:limit].rstrip(" ,;:.") + "…") if len(text) > limit else text


def _fix_relative_assets(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\((?:\.\.?/)[^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\((?:\.\.?/)[^)]*\)", r"\1", text)
    return text


def _outside_code(text: str, transform) -> str:
    out = []
    fence = False
    for line in text.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            fence = not fence
            out.append(line)
            continue
        out.append(line if fence else transform(line))
    return "\n".join(out)


def _escape_vue_line(line: str) -> str:
    # Wrap {{ ... }} in inline code so VuePress does not treat it as interpolation.
    # (HTML entities are decoded back to braces by markdown-it, so they do not help.)
    return re.sub(r"\{\{(.+?)\}\}", r"`{{\1}}`", line)


def _sanitize_detail(text: str) -> str:
    text = _fix_relative_assets(text)
    text = _outside_code(text, _escape_vue_line)
    text = _outside_code(text, _strip_tags)
    return text


_DETAIL_LABELS = {
    "en": {
        "official": "Official site", "status": "Status", "lastVerified": "Last verified",
        "catTags": "Categories & Tags", "categories": "Categories", "tags": "Tags",
        "mcpConfig": "MCP Configuration", "transport": "Transport", "command": "Command",
        "args": "Args", "argsNone": "none",
        "mcpNote": "This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.",
        "providerConfig": "Provider Configuration", "protocol": "Protocol", "baseUrl": "Base URL",
        "modelCount": "Model count", "docs": "Docs", "modelList": "Model list", "apiKey": "API key",
        "supportedModels": "Supported models", "colModelId": "Model ID", "colName": "Name",
        "colCaps": "Capabilities", "basicChat": "Basic chat",
        "freeUsage": "Free Usage", "access": "Access", "requiresLogin": "Requires login",
        "hasFreeTier": "Has free tier", "availability": "Availability", "yes": "Yes", "no": "No",
        "quotaDetail": "Per-model free quota", "colModel": "Model", "colQuota": "Free quota",
        "colFreq": "Rate / frequency",
        "regLimits": "Registration & Limits", "signup": "Sign up", "regLimit": "Registration limit",
        "freePolicy": "Free policy doc",
        "csImport": "ChatSpeed Import",
        "csImportNote": "This service is linked to model provider `{ref}`; import its config from the model provider list. Call entry points:",
        "logo": "Logo", "dataSource": "Data source",
        "sourceNote": "Resource file: `resources/{channel}/{id}.json`. Content last verified on `{date}`; free quotas and service limits may change with official policies.",
    },
    "zh-Hans": {
        "official": "官方网站", "status": "状态", "lastVerified": "最后核验",
        "catTags": "分类与标签", "categories": "分类", "tags": "标签",
        "mcpConfig": "MCP 配置", "transport": "传输方式", "command": "启动命令",
        "args": "参数", "argsNone": "无",
        "mcpNote": "该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。",
        "providerConfig": "供应商配置", "protocol": "协议", "baseUrl": "Base URL",
        "modelCount": "模型数量", "docs": "文档", "modelList": "模型列表", "apiKey": "密钥申请",
        "supportedModels": "支持的模型", "colModelId": "模型 ID", "colName": "名称",
        "colCaps": "能力", "basicChat": "基础对话",
        "freeUsage": "免费使用说明", "access": "访问方式", "requiresLogin": "是否需要登录",
        "hasFreeTier": "是否有免费层", "availability": "可用区域", "yes": "是", "no": "否",
        "quotaDetail": "分模型免费额度明细", "colModel": "模型", "colQuota": "免费额度",
        "colFreq": "频率与限速",
        "regLimits": "注册与限制", "signup": "注册入口", "regLimit": "注册限制",
        "freePolicy": "免费政策文档",
        "csImport": "ChatSpeed 导入",
        "csImportNote": "该服务关联模型供应商 `{ref}`，可从模型供应商列表导入配置，调用入口如下：",
        "logo": "Logo", "dataSource": "数据来源",
        "sourceNote": "资源文件：`resources/{channel}/{id}.json`。内容最后核验于 `{date}`；免费额度和服务限制可能随官方政策变化。",
    },
}

_HOME_META = {
    "en": {"title": "ChatSpeed Resource Center", "description": "A catalog of MCP servers, model providers, and free AI services."},
    "zh-Hans": {"title": "ChatSpeed 资源中心", "description": "MCP、模型供应商和免费 AI 服务目录"},
}

_CHANNEL_META = {
    "en": {
        "mcp": ("MCP Servers", "MCP servers you can import into ChatSpeed. The list shows a short summary; open a resource for the full configuration and usage."),
        "models": ("Model Providers", "Model providers compatible with ChatSpeed. The list is for quick selection; detail pages include protocol, endpoints, and model info."),
        "free-ai": ("Free AI", "Directory of free AI websites and API services. Free quotas are dynamic; refer to the detail page and official site."),
    },
    "zh-Hans": {
        "mcp": ("MCP 服务", "可导入 ChatSpeed 的 MCP 服务。列表展示简要说明，点击资源进入完整配置与使用详情。"),
        "models": ("模型供应商", "可接入 ChatSpeed 的模型供应商。列表用于快速选择，详情页包含协议、接口和模型信息。"),
        "free-ai": ("免费 AI", "免费 AI 网站与 API 服务目录。免费额度是动态信息，请以详情页和官方页面为准。"),
    },
}

_GUIDE = {
    "en": """---
title: Guide
description: How to browse resources and import them into ChatSpeed
sidebar: false
---

# Guide

## Browse resources

Use the top navigation to switch between the MCP Servers, Model Providers, and Free AI channels. Each channel page supports keyword search, category filtering, and sorting by update time.

## Before importing

- Resource configs come from a public catalog. Before importing, verify the official site, command, arguments, and permission source.
- This site never stores your ChatSpeed API key, MCP secrets, or other credentials.
- Free quotas, model availability, and service limits change over time. Refer to the official pages and the last-verified date on each resource detail page.

## Submit a resource

Online submissions are not available yet. You can contribute resource files through the project repository, following the [resource spec](/RESOURCE_SPEC.html) for localized descriptions, categories, tags, official links, and verification date.
""",
    "zh-Hans": """---
title: 使用说明
description: 如何浏览资源并导入 ChatSpeed
sidebar: false
---

# 使用说明

## 浏览资源

使用顶部导航切换 MCP 服务、模型供应商和免费 AI 频道。频道页支持关键词搜索、分类筛选和按更新时间排序。

## 导入前检查

- 资源配置来自公开目录，导入前请核对官方网站、命令、参数和权限来源。
- 资源站点不会保存 ChatSpeed API Key、MCP 密钥或其他凭据。
- 免费额度、模型可用性和服务限制会变化，请以官方页面和资源详情页的最后核验时间为准。

## 提交资源

暂不提供在线投稿。可以通过项目仓库提交资源文件，并按照 [资源规范](/RESOURCE_SPEC.html) 补齐多语言描述、分类、标签、官方链接和核验时间。
""",
}


def detail_markdown(resource: dict, provider_by_id: dict[str, dict]) -> str:
    L = _DETAIL_LABELS[_LOCALE]
    colon = "：" if _LOCALE == "zh-Hans" else ": "
    channel = resource["channel"]
    title = localized(resource, "name")
    description = _plain_summary(localized(resource, "description"))
    detail = _sanitize_detail(localized(resource, "detail"))
    lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "---",
        "",
        f"# {title}",
        "",
        description,
        "",
        detail,
        "",
        f"**{L['official']}{colon}** {markdown_link(resource['website'], resource['website'])}",
        f"**{L['status']}{colon}** `{resource['status']}`　**{L['lastVerified']}{colon}** `{resource['lastVerifiedAt']}`",
        "",
        f"## {L['catTags']}",
        "",
        f"- {L['categories']}{colon}{', '.join(f'`{item}`' for item in resource['categories'])}",
        f"- {L['tags']}{colon}{', '.join(f'`{item}`' for item in resource['tags'])}",
    ]
    if channel == "mcp":
        mcp = resource["mcp"]
        lines.extend([
            "",
            f"## {L['mcpConfig']}",
            "",
            f"- {L['transport']}{colon}`{mcp['type']}`",
            f"- {L['command']}{colon}`{mcp.get('command', '')}`",
            (f"- {L['args']}{colon}`{' '.join(mcp.get('args', []))}`" if mcp.get("args") else f"- {L['args']}{colon}{L['argsNone']}"),
            "",
            L["mcpNote"],
        ])
    elif channel == "models":
        provider = resource["provider"]
        lines.extend([
            "",
            f"## {L['providerConfig']}",
            "",
            f"- {L['protocol']}{colon}`{provider['protocol']}`",
            f"- {L['baseUrl']}{colon}`{provider['baseUrl']}`",
            f"- {L['modelCount']}{colon}{len(provider['models'])}",
            f"- {L['docs']}{colon}{markdown_link(provider['documentationUrl'], provider['documentationUrl'])}",
            f"- {L['modelList']}{colon}{markdown_link(provider['modelListUrl'], provider['modelListUrl'])}",
            f"- {L['apiKey']}{colon}{markdown_link(provider['keyApplyUrl'], provider['keyApplyUrl'])}",
        ])
        if provider["models"]:
            lines.extend(["", f"### {L['supportedModels']}", "", f"| {L['colModelId']} | {L['colName']} | {L['colCaps']} |", "| --- | --- | --- |"])
            for model in provider["models"]:
                capabilities = [key for key in ("reasoning", "functionCall", "imageInput") if model.get(key)]
                lines.append(f"| `{model['id']}` | {model.get('name', model['id'])} | {', '.join(capabilities) or L['basicChat']} |")
    else:
        free_ai = resource["freeAi"]
        lines.extend([
            "",
            f"## {L['freeUsage']}",
            "",
            f"- {L['access']}{colon}`{free_ai['accessType']}`",
            f"- {L['requiresLogin']}{colon}`{L['yes'] if free_ai['requiresLogin'] else L['no']}`",
            f"- {L['hasFreeTier']}{colon}`{L['yes'] if free_ai['hasFreeTier'] else L['no']}`",
            f"- {L['availability']}{colon}`{free_ai['availability']}`",
            "",
            f"{localized(free_ai, 'freeLimit')}",
        ])
        free_quotas = free_ai.get("freeQuotas")
        if free_quotas:
            lines.extend(["", f"### {L['quotaDetail']}", "", f"| {L['colModel']} | {L['colQuota']} | {L['colFreq']} |", "| --- | --- | --- |"])
            for quota in free_quotas:
                lines.append(
                    f"| {localized(quota, 'model').replace('|', '\\\\|')} "
                    f"| {localized(quota, 'quota').replace('|', '\\\\|')} "
                    f"| {localized(quota, 'frequency').replace('|', '\\\\|')} |"
                )
        signup_url = free_ai.get("signupUrl")
        restriction = free_ai.get("registrationRestriction")
        policy_url = free_ai.get("freePolicyUrl")
        if signup_url or restriction or policy_url:
            lines.extend(["", f"## {L['regLimits']}"])
            if signup_url:
                lines.append(f"- {L['signup']}{colon}{markdown_link(signup_url, signup_url)}")
            if restriction:
                lines.append(f"- {L['regLimit']}{colon}{localized(free_ai, 'registrationRestriction')}")
            if policy_url:
                lines.append(f"- {L['freePolicy']}{colon}{markdown_link(policy_url, policy_url)}")
        integration = free_ai.get("integrations", {}).get("chatSpeedModel")
        if integration and integration.get("importable"):
            provider_ref = integration["providerRef"]
            lines.extend(["", f"## {L['csImport']}", "", L["csImportNote"].format(ref=provider_ref)])
            provider = provider_by_id.get(provider_ref)
            if provider:
                info = provider["provider"]
                lines.append(f"- {L['protocol']}{colon}`{info['protocol']}`")
                lines.append(f"- {L['baseUrl']}{colon}`{info['baseUrl']}`")
                if info.get("logo"):
                    lines.append(f"- {L['logo']}{colon}![{info.get('name', provider_ref)}]({info['logo']})")
                for label, field in ((L["docs"], "documentationUrl"), (L["modelList"], "modelListUrl"), (L["apiKey"], "keyApplyUrl")):
                    url = info.get(field)
                    if url:
                        lines.append(f"- {label}{colon}{markdown_link(url, url)}")
    lines.extend(["", f"## {L['dataSource']}", "", L["sourceNote"].format(channel=channel, id=resource["id"], date=resource["lastVerifiedAt"])])
    return "\n".join(lines) + "\n"


def _frontmatter_lines(title: str, description: str) -> list[str]:
    return [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "sidebar: false",
        "breadcrumb: false",
        "pageInfo: false",
        "toc: false",
        "containerClass: resource-directory",
        "---",
        "",
    ]


def write_docs(catalog: dict, by_channel: dict[str, list[dict]]) -> None:
    global _LOCALE
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    provider_by_id = {item["id"]: item for item in by_channel.get("models", [])}
    # English is the default locale at the site root; Chinese lives under /zh/.
    # The ResourceBrowser component reads the active locale from the route path,
    # so the same <ResourceBrowser/> markup serves both locales.
    for locale, prefix in (("en", ""), ("zh-Hans", "zh")):
        _LOCALE = locale
        base = DOCS_ROOT / prefix if prefix else DOCS_ROOT
        base.mkdir(parents=True, exist_ok=True)
        home = _HOME_META[locale]
        home_lines = _frontmatter_lines(home["title"], home["description"]) + ["<ResourceBrowser />", ""]
        write_text(base / "README.md", "\n".join(home_lines))
        write_text(base / "guide" / "README.md", _GUIDE[locale])
        for channel, resources in by_channel.items():
            channel_dir = base / channel
            channel_dir.mkdir(parents=True, exist_ok=True)
            title, intro = _CHANNEL_META[locale][channel]
            index_lines = _frontmatter_lines(title, intro) + [f'<ResourceBrowser channel="{channel}" />', ""]
            write_text(channel_dir / "README.md", "\n".join(index_lines))
            for resource in resources:
                write_text(channel_dir / f"{resource['id']}.md", detail_markdown(resource, provider_by_id))


def output_item(resource: dict) -> dict:
    item = dict(resource)
    item["searchText"] = localized_search_text(resource)
    item["detailPath"] = f"/{resource['channel']}/{resource['id']}/"
    if resource["channel"] == "mcp":
        mcp = resource["mcp"]
        server_name = resource["id"]
        item["config"] = {"mcpServers": {server_name: {key: value for key, value in mcp.items() if key != "requiredInputs"}}}
    if resource["channel"] == "models":
        item["provider"] = resource["provider"]
    return item


def mcp_compat_item(resource: dict) -> dict:
    """Return the legacy shape currently consumed by Mcp.vue."""
    item = output_item(resource)
    item.pop("detail", None)
    item["nameI18n"] = item.pop("name")
    item["descriptionI18n"] = item.pop("description")
    item["name"] = item["nameI18n"]["en"]
    item["description"] = item["descriptionI18n"]["en"]
    return item


def provider_compat_item(resource: dict) -> dict:
    """Return the flat provider shape currently consumed by Model.vue."""
    item = output_item(resource)
    item.pop("detail", None)
    provider = item.pop("provider")
    item["resourceId"] = item["id"]
    item.update(provider)
    return item


def channel_items(channel: str, resources: list[dict]) -> list[dict]:
    if channel == "mcp":
        return [mcp_compat_item(resource) for resource in resources]
    if channel == "models":
        return [provider_compat_item(resource) for resource in resources]
    return [output_item(resource) for resource in resources]


def write_channel_catalog(path: Path, catalog: dict, channel: str, items: list[dict]) -> None:
    write_json(path, {"version": catalog["version"], "generatedAt": catalog["generatedAt"], "channel": channel, "items": items})


def generate(catalog: dict, by_channel: dict[str, list[dict]]) -> None:
    all_items = [output_item(resource) for resource in catalog["resources"]]
    public_index = {
        "version": catalog["version"],
        "generatedAt": catalog["generatedAt"],
        "channels": [
            {
                "id": channel,
                "url": f"/catalog/{'model-providers' if channel == 'models' else channel}.json",
                "count": len(by_channel[channel]),
            }
            for channel in CHANNELS
        ],
    }
    full_index = {"version": catalog["version"], "generatedAt": catalog["generatedAt"], "channels": catalog["channels"], "items": all_items}
    write_json(PUBLIC_CATALOG / "index.json", public_index)
    write_json(GENERATED_DATA / "catalog.json", full_index)
    for channel, resources in by_channel.items():
        items = channel_items(channel, resources)
        filename = "model-providers.json" if channel == "models" else f"{channel}.json"
        write_channel_catalog(PUBLIC_CATALOG / filename, catalog, channel, items)
        if channel == "models":
            # Keep the internal channel filename as a compatibility alias while
            # Model.vue consumes the explicit model-providers filename.
            write_channel_catalog(PUBLIC_CATALOG / "models.json", catalog, channel, items)
        write_channel_catalog(GENERATED_DATA / f"{channel}.json", catalog, channel, items)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate resources without writing generated files")
    args = parser.parse_args()
    try:
        catalog, by_channel = build_catalog()
        if not args.check:
            generate(catalog, by_channel)
            write_docs(catalog, by_channel)
        print(f"Validated {len(catalog['resources'])} resources across {len(CHANNELS)} channels.")
        if not args.check:
            print(f"Generated catalog files in {PUBLIC_CATALOG.relative_to(ROOT)}.")
        return 0
    except ValidationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
