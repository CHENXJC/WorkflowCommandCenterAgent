"""Delivery report generation."""

from __future__ import annotations

from typing import Any

from .models import DeliveryReportInput


def generate_delivery_report_markdown(payload: DeliveryReportInput | dict[str, Any]) -> str:
    report = payload if isinstance(payload, DeliveryReportInput) else DeliveryReportInput.from_mapping(payload)
    return "\n".join(
        [
            f"# Delivery Report: {report.project_name}",
            "",
            f"- Checkpoint: {report.checkpoint}",
            f"- Stage goal: {report.stage_goal}",
            "",
            "## Completed Items",
            _bullet_list(report.completed_items),
            "",
            "## Modified Files",
            _bullet_list(report.modified_files),
            "",
            "## Validation Results",
            _bullet_list(report.validation_results),
            "",
            "## Risks",
            _bullet_list(report.risks or ["No known high-risk issue for the demo MVP."]),
            "",
            "## Git Status Summary",
            report.git_status_summary or "Not checked yet.",
            "",
            "## Next Recommended Action",
            report.next_recommended_action or "Define the next checkpoint.",
        ]
    )


def build_demo_delivery_report() -> DeliveryReportInput:
    return DeliveryReportInput(
        project_name="WorkflowCommandCenterAgent",
        checkpoint="WCC-001-LOCAL-MVP",
        stage_goal="Create a local-first Streamlit MVP for Codex-ready project execution workflows.",
        completed_items=[
            "Created project starter generator.",
            "Created reusable workflow packs.",
            "Created checklist manager.",
            "Created demo project status tracker.",
            "Created prompt/rule library.",
            "Created delivery report and export modules.",
        ],
        modified_files=[
            "app.py",
            "workflow_command/",
            "data/",
            "docs/PROJECT_PLAN.md",
            "README.md",
            "PROJECT_STATUS.md",
            "agent_manifest.json",
            "release/public_showcase_manifest.json",
        ],
        validation_results=[
            "python -m pytest -q",
            "python -m compileall .",
            "JSON manifest parse checks",
        ],
        risks=[
            "WCC-001 uses demo data only and does not modify AgentHubControlCenter.",
            "GitHub release and profile pin are intentionally out of scope.",
        ],
        git_status_summary="Local-only repository; no remote push required for WCC-001.",
        next_recommended_action="WCC-002 AgentHub readiness polish without modifying AgentHubControlCenter until explicitly requested.",
    )


def _bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)
