"""Shared lightweight data models for the workflow command center."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Iterable


CHECKLIST_STATUSES = {"pending", "in_progress", "done", "skipped"}


@dataclass(frozen=True)
class ProjectStarterRequest:
    """Input contract for a Codex-ready project starter prompt."""

    project_name: str
    project_path: str
    checkpoint: str
    stage_goal: str
    project_type: str
    files_to_read: list[str] = field(default_factory=list)
    allowed_actions: list[str] = field(default_factory=list)
    blocked_actions: list[str] = field(default_factory=list)
    test_commands: list[str] = field(default_factory=list)
    git_policy: list[str] = field(default_factory=list)
    output_requirements: list[str] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, payload: dict[str, Any]) -> "ProjectStarterRequest":
        return cls(
            project_name=str(payload.get("project_name", "")).strip(),
            project_path=str(payload.get("project_path", "")).strip(),
            checkpoint=str(payload.get("checkpoint", "")).strip(),
            stage_goal=str(payload.get("stage_goal", "")).strip(),
            project_type=str(payload.get("project_type", "")).strip(),
            files_to_read=_as_list(payload.get("files_to_read")),
            allowed_actions=_as_list(payload.get("allowed_actions")),
            blocked_actions=_as_list(payload.get("blocked_actions")),
            test_commands=_as_list(payload.get("test_commands")),
            git_policy=_as_list(payload.get("git_policy")),
            output_requirements=_as_list(payload.get("output_requirements")),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class WorkflowPack:
    """Reusable workflow template for recurring project execution tasks."""

    pack_name: str
    category: str
    purpose: str
    recommended_steps: list[str]
    required_files: list[str]
    validation_commands: list[str]
    risk_notes: list[str]
    final_output_format: list[str]

    @classmethod
    def from_mapping(cls, payload: dict[str, Any]) -> "WorkflowPack":
        return cls(
            pack_name=str(payload.get("pack_name", "")).strip(),
            category=str(payload.get("category", "")).strip(),
            purpose=str(payload.get("purpose", "")).strip(),
            recommended_steps=_as_list(payload.get("recommended_steps")),
            required_files=_as_list(payload.get("required_files")),
            validation_commands=_as_list(payload.get("validation_commands")),
            risk_notes=_as_list(payload.get("risk_notes")),
            final_output_format=_as_list(payload.get("final_output_format")),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ChecklistItem:
    """A single execution checklist item."""

    title: str
    description: str
    required: bool = True
    status: str = "pending"

    def __post_init__(self) -> None:
        if self.status not in CHECKLIST_STATUSES:
            raise ValueError(f"Unsupported checklist status: {self.status}")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DeliveryReportInput:
    """Input contract for a structured delivery report."""

    project_name: str
    checkpoint: str
    stage_goal: str
    completed_items: list[str]
    modified_files: list[str]
    validation_results: list[str]
    risks: list[str]
    git_status_summary: str
    next_recommended_action: str

    @classmethod
    def from_mapping(cls, payload: dict[str, Any]) -> "DeliveryReportInput":
        return cls(
            project_name=str(payload.get("project_name", "")).strip(),
            checkpoint=str(payload.get("checkpoint", "")).strip(),
            stage_goal=str(payload.get("stage_goal", "")).strip(),
            completed_items=_as_list(payload.get("completed_items")),
            modified_files=_as_list(payload.get("modified_files")),
            validation_results=_as_list(payload.get("validation_results")),
            risks=_as_list(payload.get("risks")),
            git_status_summary=str(payload.get("git_status_summary", "")).strip(),
            next_recommended_action=str(payload.get("next_recommended_action", "")).strip(),
        )


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [line.strip() for line in value.splitlines() if line.strip()]
    if isinstance(value, Iterable):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()]
