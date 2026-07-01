"""Prompt and rule library helpers."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from .demo_data import load_demo_prompts


def get_demo_prompts() -> list[dict[str, Any]]:
    return load_demo_prompts()


def list_prompt_categories(prompts: list[dict[str, Any]] | None = None) -> list[str]:
    records = prompts if prompts is not None else get_demo_prompts()
    return sorted({str(prompt.get("category", "")) for prompt in records if prompt.get("category")})


def filter_prompts_by_category(category: str) -> list[dict[str, Any]]:
    category_normalized = category.strip().lower()
    return [
        prompt
        for prompt in get_demo_prompts()
        if str(prompt.get("category", "")).lower() == category_normalized
    ]


def group_prompts_by_category(prompts: list[dict[str, Any]] | None = None) -> dict[str, list[dict[str, Any]]]:
    records = prompts if prompts is not None else get_demo_prompts()
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for prompt in records:
        grouped[str(prompt.get("category", "Uncategorized"))].append(prompt)
    return dict(grouped)


def render_prompt_record(prompt: dict[str, Any]) -> str:
    tags = ", ".join(str(tag) for tag in prompt.get("tags", []))
    return "\n".join(
        [
            f"# {prompt.get('title', '')}",
            "",
            f"- Category: {prompt.get('category', '')}",
            f"- Target tool: {prompt.get('target_tool', '')}",
            f"- Tags: {tags}",
            "",
            "## Prompt",
            str(prompt.get("prompt_text", "")).strip(),
            "",
            "## Usage Note",
            str(prompt.get("usage_note", "")).strip(),
            "",
            "## Safety Note",
            str(prompt.get("safety_note", "")).strip(),
        ]
    )
