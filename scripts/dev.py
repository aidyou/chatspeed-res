#!/usr/bin/env python3
"""Generate resource docs and start VuePress with resource-file watching."""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "resources"


def run_catalog() -> None:
    result = subprocess.run([sys.executable, "scripts/build-index.py"], cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)


def main() -> int:
    run_catalog()
    vuepress = subprocess.Popen(["pnpm", "exec", "vuepress", "dev", "docs", "--clean-cache"], cwd=ROOT)
    snapshot = {path: path.stat().st_mtime_ns for path in RESOURCES.rglob("*.json")}
    try:
        while vuepress.poll() is None:
            time.sleep(0.75)
            current = {path: path.stat().st_mtime_ns for path in RESOURCES.rglob("*.json")}
            if current != snapshot:
                print("Resource files changed; rebuilding catalog and detail pages.", flush=True)
                run_catalog()
                snapshot = current
    except KeyboardInterrupt:
        vuepress.terminate()
    return vuepress.wait()


if __name__ == "__main__":
    raise SystemExit(main())
