"""Workflow pack loading and summarization."""

from __future__ import annotations

from typing import Any

from .demo_data import load_demo_workflow_packs
from .models import WorkflowPack


def get_demo_workflow_packs() -> list[WorkflowPack]:
    return [WorkflowPack.from_mapping(item) for item in load_demo_workflow_packs()]


def get_pack_by_name(pack_name: str) -> WorkflowPack:
    for pack in get_demo_workflow_packs():
        if pack.pack_name == pack_name:
            return pack
    raise ValueError(f"Workflow pack not found: {pack_name}")


def summarize_workflow_pack(pack: WorkflowPack | dict[str, Any]) -> str:
    workflow_pack = pack if isinstance(pack, WorkflowPack) else WorkflowPack.from_mapping(pack)
    return "\n".join(
        [
            f"# {workflow_pack.pack_name}",
            "",
            f"- Category: {workflow_pack.category}",
            f"- Purpose: {workflow_pack.purpose}",
            "",
            "## Recommended Steps",
            _bullet_list(workflow_pack.recommended_steps),
            "",
            "## Required Files",
            _bullet_list(workflow_pack.required_files),
            "",
            "## Validation Commands",
            _bullet_list(workflow_pack.validation_commands),
            "",
            "## Risk Notes",
            _bullet_list(workflow_pack.risk_notes),
            "",
            "## Final Output Format",
            _bullet_list(workflow_pack.final_output_format),
        ]
    )


def workflow_pack_options() -> list[str]:
    return [pack.pack_name for pack in get_demo_workflow_packs()]


def _bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)
