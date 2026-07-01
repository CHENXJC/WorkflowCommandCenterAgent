"""Generate execution checklists from workflow packs."""

from __future__ import annotations

from typing import Any

from .models import ChecklistItem, WorkflowPack


BASE_CHECKLIST = [
    ("Read PROJECT_STATUS.md", "Understand current checkpoint, completed work, and next action."),
    ("Read README.md", "Confirm user-facing purpose, setup, and public showcase boundary."),
    ("Inspect project structure", "Use the existing structure before adding new files or abstractions."),
    ("Make minimal changes", "Keep edits scoped to the requested checkpoint."),
    ("Run pytest", "Run python -m pytest -q and report the result honestly."),
    ("Run compileall", "Run python -m compileall . and report the result honestly."),
    ("Validate JSON files", "Parse manifest and demo JSON files before declaring completion."),
    ("Update docs", "Keep README, PROJECT_STATUS, and docs aligned with real behavior."),
    ("Check git status", "Review staged and unstaged changes before commit."),
    ("Commit selected files only", "Stage explicit paths only; do not use git add ."),
    ("Output final summary", "Report completed work, validation, safety checks, checkpoint, and next step."),
]


PACK_EXTRA_ITEMS = {
    "GitHub Showcase Pack": [
        ("Run public safety audit", "Confirm no secrets, private data, outputs, caches, or oversized files are included."),
        ("Verify showcase metadata", "Confirm README, screenshots guide, manifest, and GitHub topics are ready."),
    ],
    "Bugfix Pack": [
        ("Reproduce the bug", "Capture the failing command or behavior before changing code."),
        ("Add focused regression test", "Cover the specific failing behavior with a small test."),
    ],
    "Status Sync Pack": [
        ("Compare status files", "Ensure README, PROJECT_STATUS, and planning docs use the same checkpoint."),
        ("Avoid feature drift", "Keep the pass metadata-only unless the user explicitly asks for features."),
    ],
    "Report Export Pack": [
        ("Validate export formats", "Confirm Markdown, text, and JSON exports contain the required sections."),
        ("Check generated report safety", "Ensure exported examples use demo data only."),
    ],
    "Commercial Delivery Pack": [
        ("Mark demo boundary", "Separate portfolio demo behavior from client-delivery assumptions."),
        ("List handoff risks", "Call out privacy, dependency, and operational risks before delivery."),
    ],
}


def generate_checklist_from_pack(pack: WorkflowPack | dict[str, Any]) -> list[ChecklistItem]:
    workflow_pack = pack if isinstance(pack, WorkflowPack) else WorkflowPack.from_mapping(pack)
    items = [ChecklistItem(title=title, description=description) for title, description in BASE_CHECKLIST]

    for step in workflow_pack.recommended_steps:
        items.append(
            ChecklistItem(
                title=step,
                description=f"Pack-specific step for {workflow_pack.pack_name}.",
                required=True,
            )
        )

    for title, description in PACK_EXTRA_ITEMS.get(workflow_pack.pack_name, []):
        items.append(ChecklistItem(title=title, description=description, required=True))

    return _dedupe_items(items)


def checklist_to_markdown(items: list[ChecklistItem | dict[str, Any]], title: str = "Execution Checklist") -> str:
    lines = [f"# {title}", ""]
    for item in items:
        checklist_item = item if isinstance(item, ChecklistItem) else ChecklistItem(**item)
        marker = "x" if checklist_item.status == "done" else " "
        required = "required" if checklist_item.required else "optional"
        lines.append(f"- [{marker}] **{checklist_item.title}** ({required}, {checklist_item.status})")
        lines.append(f"  - {checklist_item.description}")
    return "\n".join(lines)


def checklist_to_dicts(items: list[ChecklistItem]) -> list[dict[str, Any]]:
    return [item.to_dict() for item in items]


def _dedupe_items(items: list[ChecklistItem]) -> list[ChecklistItem]:
    seen: set[str] = set()
    result: list[ChecklistItem] = []
    for item in items:
        key = item.title.lower()
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
