"""Export helpers for prompts, workflow packs, checklists, and reports."""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from typing import Any


def export_markdown(title: str, content: Any) -> str:
    if isinstance(content, str):
        body = content
    else:
        body = _structured_to_markdown(content)

    if body.lstrip().startswith("#"):
        return body
    return f"# {title}\n\n{body}".strip() + "\n"


def export_text(title: str, content: Any) -> str:
    if isinstance(content, str):
        return content.strip() + "\n"
    return f"{title}\n{'=' * len(title)}\n{_structured_to_plain_text(content)}\n"


def export_json(content: Any) -> str:
    return json.dumps(_to_jsonable(content), ensure_ascii=False, indent=2)


def _structured_to_markdown(content: Any) -> str:
    jsonable = _to_jsonable(content)
    if isinstance(jsonable, list):
        lines: list[str] = []
        for item in jsonable:
            if isinstance(item, dict):
                title = item.get("title") or item.get("pack_name") or item.get("project_name") or "Item"
                lines.append(f"## {title}")
                for key, value in item.items():
                    lines.extend(_field_to_markdown(key, value))
                lines.append("")
            else:
                lines.append(f"- {item}")
        return "\n".join(lines).strip()
    if isinstance(jsonable, dict):
        lines = []
        for key, value in jsonable.items():
            lines.extend(_field_to_markdown(key, value))
        return "\n".join(lines).strip()
    return str(jsonable)


def _field_to_markdown(key: str, value: Any) -> list[str]:
    label = key.replace("_", " ").title()
    if isinstance(value, list):
        return [f"### {label}", *[f"- {item}" for item in value]]
    if isinstance(value, dict):
        return [f"### {label}", "```json", json.dumps(value, ensure_ascii=False, indent=2), "```"]
    return [f"- **{label}:** {value}"]


def _structured_to_plain_text(content: Any) -> str:
    jsonable = _to_jsonable(content)
    if isinstance(jsonable, (dict, list)):
        return json.dumps(jsonable, ensure_ascii=False, indent=2)
    return str(jsonable)


def _to_jsonable(content: Any) -> Any:
    if is_dataclass(content):
        return asdict(content)
    if isinstance(content, list):
        return [_to_jsonable(item) for item in content]
    if isinstance(content, tuple):
        return [_to_jsonable(item) for item in content]
    if isinstance(content, dict):
        return {str(key): _to_jsonable(value) for key, value in content.items()}
    return content
