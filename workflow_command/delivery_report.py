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
        checkpoint="WCC-002-AGENTHUB-READINESS",
        stage_goal="Prepare WorkflowCommandCenterAgent for future AgentHubControlCenter recognition without modifying the hub repo.",
        completed_items=[
            "Enhanced agent_manifest.json for AgentHub readiness.",
            "Enhanced release/public_showcase_manifest.json with local release boundary.",
            "Created AgentHub integration documentation.",
            "Created WCC-002 readiness summary.",
            "Updated README and PROJECT_STATUS.",
            "Added AgentHub readiness tests.",
        ],
        modified_files=[
            "app.py",
            "workflow_command/",
            "data/demo_projects.json",
            "docs/AGENTHUB_INTEGRATION.md",
            "docs/WCC_002_AGENTHUB_READINESS.md",
            "docs/PROJECT_PLAN.md",
            "README.md",
            "PROJECT_STATUS.md",
            "agent_manifest.json",
            "release/public_showcase_manifest.json",
        ],
        validation_results=[
            "python -m pytest -q",
            "python -m compileall .",
            "python -c \"import app; print('APP_IMPORT_OK')\"",
            "JSON manifest parse checks",
        ],
        risks=[
            "WCC-002 uses demo data only and does not modify AgentHubControlCenter.",
            "GitHub release and profile pin are intentionally out of scope.",
        ],
        git_status_summary="Local-only repository; no remote push required for WCC-002.",
        next_recommended_action="WCC-003 GitHub showcase prep after local readiness validation.",
    )


def _bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)
