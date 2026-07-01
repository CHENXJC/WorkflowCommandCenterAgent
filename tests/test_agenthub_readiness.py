import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_agent_manifest_has_agenthub_ready_contract():
    manifest = json.loads((ROOT / "agent_manifest.json").read_text(encoding="utf-8"))

    required_fields = {
        "agent_name",
        "display_name",
        "chinese_name",
        "category",
        "subcategory",
        "role_in_portfolio",
        "current_checkpoint",
        "status",
        "lifecycle_stage",
        "hub_ready",
        "modifies_agent_hub",
        "launch_command",
        "local_path",
        "github_repo",
        "github_showcase_ready",
        "profile_pin_status",
        "demo_mode",
        "privacy_mode",
        "core_capabilities",
        "key_modules",
        "ui_tabs",
        "validation_commands",
        "last_validation",
        "integration_notes",
        "next_recommended_action",
    }

    assert required_fields.issubset(manifest)
    assert manifest["agent_name"] == "WorkflowCommandCenterAgent"
    assert manifest["subcategory"] == "project-execution-command-center"
    assert manifest["current_checkpoint"] == "WCC-004-GITHUB-PUBLIC-RELEASE"
    assert manifest["status"] == "github-public-showcase"
    assert manifest["hub_ready"] is True
    assert manifest["modifies_agent_hub"] is False
    assert manifest["github_repo"] == "https://github.com/CHENXJC/WorkflowCommandCenterAgent"
    assert manifest["profile_pin_status"] == "not_pinned"
    assert manifest["next_recommended_action"] == "optional-profile-pin-or-agenthub-integration"


def test_release_manifest_states_not_public_release_or_agenthub_modified():
    manifest = json.loads((ROOT / "release" / "public_showcase_manifest.json").read_text(encoding="utf-8"))

    assert manifest["project_name"] == "WorkflowCommandCenterAgent"
    assert manifest["current_checkpoint"] == "WCC-004-GITHUB-PUBLIC-RELEASE"
    assert manifest["release_stage"] == "github-public-release"
    assert manifest["github_public_release_completed"] is True
    assert manifest["github_repo"] == "https://github.com/CHENXJC/WorkflowCommandCenterAgent"
    assert manifest["profile_pin_status"] == "not_pinned"
    assert manifest["agenthub_modified"] is False
    assert manifest["safety_summary"]["agenthub_modified"] is False
    assert manifest["safety_summary"]["secrets_read"] is False
    assert manifest["next_stage"] == "optional-profile-pin-or-agenthub-integration"


def test_agenthub_readiness_docs_exist():
    integration_doc = ROOT / "docs" / "AGENTHUB_INTEGRATION.md"
    readiness_doc = ROOT / "docs" / "WCC_002_AGENTHUB_READINESS.md"

    assert integration_doc.exists()
    assert readiness_doc.exists()
    assert "AgentHub-ready, not AgentHub-integrated" in readiness_doc.read_text(encoding="utf-8")
    assert "WorkflowCommandCenterAgent = project execution" in integration_doc.read_text(encoding="utf-8")
