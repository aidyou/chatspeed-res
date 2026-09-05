# Resource specification

## Common fields

| Field | Required | Description |
| --- | --- | --- |
| `id` | yes | Globally unique kebab-case identifier. |
| `channel` | yes | `mcp` or `free-ai`. |
| `name` | yes | Localized object with `en`, `zh-Hans`, and `zh-Hant`. |
| `description` | yes | Localized short summary used in import lists. |
| `detail` | yes | Localized full introduction shown on the standalone detail page. |
| `categories` | yes | One or more IDs from `resources/categories.json`. |
| `tags` | yes | Searchable lowercase tags. |
| `website` | yes | Canonical HTTPS/HTTP website URL. |
| `status` | yes | `active`, `review`, or `deprecated`. |
| `lastVerifiedAt` | yes | ISO date (`YYYY-MM-DD`). |

## Detail content

`description` is the short localized summary used by import lists and channel indexes. `detail` is a required localized object with `en`, `zh-Hans`, and `zh-Hant`; it is the full introduction rendered on each standalone VuePress detail page. Include purpose, usage/setup guidance, limitations, and verification notes rather than repeating only the summary.


- `mcp`：MCP 服务，可导入 `Mcp.vue`。
- `free-ai`：免费 AI 网站或免费 API 服务；如果具备 ChatSpeed 模型导入能力，在资源顶层附带 `provider` 配置（见下文）。导入接口 `/catalog/model-providers.json` 由这些自带 `provider` 的资源生成。


`mcp` contains the transport configuration. The generator also creates the legacy-compatible `config.mcpServers` field in the output index.

- `type`: `stdio`, `sse`, or `http`.
- `command` and `args`: required for `stdio`.
- `url`: required for `sse` or `http`.
- `env`: pairs of variable name and placeholder/value. Never use a real secret.
- `requiredInputs`: optional declarations such as an API key name and application URL.

## Provider fields (free-ai import)

A free-ai resource becomes importable into ChatSpeed when it carries an optional top-level `provider` object. It mirrors the fields currently consumed by `Model.vue`:

- `protocol`: `openai`, `ollama`, `gemini`, `claude`, or `huggingface`.
- `name`, `logo`, `desc`, `baseUrl`, `models`.
- `maxTokens`, `temperature`, `topP`, `topK`.
- `documentationUrl`, `modelListUrl`, `keyApplyUrl`.

Every model in `provider.models` must contain a unique `id`. Optional capability fields include `reasoning`, `functionCall`, `imageInput`, `contextSize`, and `maxTokens`.

## Free AI fields

`freeAi` describes the public service and must not imply that a website is an API:

- `accessType`: `web`, `api`, or `web-and-api`.
- `requiresLogin`: boolean.
- `hasFreeTier`: boolean.
- `freeLimit`: localized text.
- `availability`: `global`, `regional`, or `unknown`.
- `signupUrl`: optional absolute URL of the free-tier registration entry.
- `freePolicyUrl`: optional absolute URL of the official page documenting the latest free quota or rate limits; omit when no authoritative page exists.
- `registrationRestriction`: optional localized text describing sign-up or verification requirements (linking a cloud account, real-name verification, SMS verification, credit-card requirements, etc.).
- `freeQuotas`: optional non-empty array of per-model/scope free-tier details; each item is an object with localized `model`, `quota`, and `frequency` fields, rendered as a table on the detail page.
- Optional top-level `provider`: when present, the service exposes an importable API and its config is published to `/catalog/model-providers.json` for `Model.vue`; it must never contain a user API key.

## Security rules

- Never commit API keys, passwords, bearer tokens, cookies, or private endpoints.
- Use placeholders such as `{YOUR_API_KEY_HERE}` only when the client will ask the user to replace them.
- All resources remain subject to ChatSpeed-side validation before import.
