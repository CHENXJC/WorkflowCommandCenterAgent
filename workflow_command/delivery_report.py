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
        checkpoint="WCC-004-GITHUB-PUBLIC-RELEASE",
        stage_goal="Publish WorkflowCommandCenterAgent as a demo-safe GitHub public showcase without profile pinning or modifying AgentHubControlCenter.",
        completed_items=[
            "Captured eight real Streamlit screenshots.",
            "Connected screenshots to README.",
            "Updated manifests and project status to GitHub public release.",
            "Ran final release safety checks.",
            "Pushed to GitHub public repo.",
            "Verified GitHub README and screenshot raw URLs.",
        ],
        modified_files=[
            "app.py",
            "workflow_command/",
            "data/demo_projects.json",
            "docs/SCREENSHOTS_GUIDE.md",
            "docs/PUBLIC_SHOWCASE_CHECKLIST.md",
            "docs/WCC_003_GITHUB_SHOWCASE_PREP.md",
            "docs/WCC_004_GITHUB_PUBLIC_RELEASE.md",
            "docs/AGENTHUB_INTEGRATION.md",
            "docs/WCC_002_AGENTHUB_READINESS.md",
            "docs/PROJECT_PLAN.md",
            "README.md",
            "PROJECT_STATUS.md",
            "agent_manifest.json",
            "release/public_showcase_manifest.json",
            "release/public_release_check.py",
            "screenshots/*.png",
        ],
        validation_results=[
            "python -m pytest -q",
            "python -m compileall .",
            "python release/public_release_check.py",
            "python -c \"import app; print('APP_IMPORT_OK')\"",
            "JSON manifest parse checks",
        ],
        risks=[
            "WCC-004 uses demo data only and does not modify AgentHubControlCenter.",
            "Profile pin and AgentHubControlCenter integration are intentionally out of scope.",
        ],
        git_status_summary="Public GitHub showcase repository should be synced to origin/main.",
        next_recommended_action="Optional profile pin decision or AgentHubControlCenter integration only when explicitly requested.",
    )


def _bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)
