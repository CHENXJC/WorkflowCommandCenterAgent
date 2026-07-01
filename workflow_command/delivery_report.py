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
        checkpoint="WCC-003-GITHUB-SHOWCASE-PREP",
        stage_goal="Prepare WorkflowCommandCenterAgent for a future GitHub public showcase without publishing, pushing, profile pinning, or modifying AgentHubControlCenter.",
        completed_items=[
            "Created screenshot guide.",
            "Created public showcase checklist.",
            "Created WCC-003 showcase prep summary.",
            "Added public release prep check script.",
            "Updated README and PROJECT_STATUS for showcase prep.",
            "Updated release and agent manifests for WCC-003.",
        ],
        modified_files=[
            "app.py",
            "workflow_command/",
            "data/demo_projects.json",
            "docs/SCREENSHOTS_GUIDE.md",
            "docs/PUBLIC_SHOWCASE_CHECKLIST.md",
            "docs/WCC_003_GITHUB_SHOWCASE_PREP.md",
            "docs/AGENTHUB_INTEGRATION.md",
            "docs/WCC_002_AGENTHUB_READINESS.md",
            "docs/PROJECT_PLAN.md",
            "README.md",
            "PROJECT_STATUS.md",
            "agent_manifest.json",
            "release/public_showcase_manifest.json",
            "release/public_release_check.py",
            "screenshots/.gitkeep",
        ],
        validation_results=[
            "python -m pytest -q",
            "python -m compileall .",
            "python release/public_release_check.py",
            "python -c \"import app; print('APP_IMPORT_OK')\"",
            "JSON manifest parse checks",
        ],
        risks=[
            "WCC-003 uses demo data only and does not modify AgentHubControlCenter.",
            "GitHub public release, remote configuration, push, screenshots, and profile pin are intentionally out of scope.",
        ],
        git_status_summary="Local-only repository; no remote push required for WCC-003.",
        next_recommended_action="WCC-004 GitHub public release only when explicitly requested.",
    )


def _bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)
