"""Demo data loading helpers.

The project intentionally reads only its own checked-in demo JSON files. It does
not inspect private project folders, credentials, browser data, or user output
directories.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def load_json_file(filename: str) -> list[dict[str, Any]]:
    path = DATA_DIR / filename
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, list):
        raise ValueError(f"{filename} must contain a JSON array")
    return payload


def load_demo_projects() -> list[dict[str, Any]]:
    return load_json_file("demo_projects.json")


def load_demo_workflow_packs() -> list[dict[str, Any]]:
    return load_json_file("demo_workflow_packs.json")


def load_demo_prompts() -> list[dict[str, Any]]:
    return load_json_file("demo_prompts.json")
