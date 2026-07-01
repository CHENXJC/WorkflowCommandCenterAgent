import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_showcase_prep_docs_and_placeholder_exist():
    required_paths = [
        "docs/SCREENSHOTS_GUIDE.md",
        "docs/PUBLIC_SHOWCASE_CHECKLIST.md",
        "docs/WCC_003_GITHUB_SHOWCASE_PREP.md",
        "screenshots/.gitkeep",
        "release/public_release_check.py",
    ]

    for relative_path in required_paths:
        assert (ROOT / relative_path).exists(), relative_path


def test_readme_contains_showcase_agenthub_and_local_first_sections():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "Project Overview" in readme
    assert "Why This Is Not A Simple Prompt Library" in readme
    assert "UI Preview / Screenshot Plan" in readme
    assert "WorkflowCommandCenterAgent vs AgentHubControlCenter" in readme
    assert "AgentHub-Ready, Not AgentHub-Integrated" in readme
    assert "Local-First And Demo-Data-Only Safety Model" in readme
    assert "GitHub public release: not completed" in readme
    assert "Actual screenshots: not completed" in readme


def test_release_manifest_showcase_prep_fields():
    manifest = json.loads((ROOT / "release" / "public_showcase_manifest.json").read_text(encoding="utf-8"))

    assert manifest["current_checkpoint"] == "WCC-003-GITHUB-SHOWCASE-PREP"
    assert manifest["release_stage"] == "github-showcase-prep"
    assert manifest["github_public_release_completed"] is False
    assert manifest["github_repo"] == "not_configured"
    assert manifest["screenshots_ready"] is False
    assert manifest["screenshot_guide_ready"] is True
    assert manifest["public_showcase_checklist_ready"] is True
    assert manifest["profile_pin_status"] == "not_applicable_yet"
    assert manifest["agenthub_modified"] is False
    assert manifest["agenthub_readiness"] == "ready-local"
    assert manifest["next_stage"] == "WCC-004-GITHUB-PUBLIC-RELEASE"


def test_agent_manifest_showcase_prep_fields():
    manifest = json.loads((ROOT / "agent_manifest.json").read_text(encoding="utf-8"))

    assert manifest["current_checkpoint"] == "WCC-003-GITHUB-SHOWCASE-PREP"
    assert manifest["hub_ready"] is True
    assert manifest["modifies_agent_hub"] is False
    assert manifest["github_showcase_ready"] == "prep"
    assert manifest["github_repo"] == "not_configured"
    assert manifest["next_recommended_action"] == "WCC-004-GITHUB-PUBLIC-RELEASE"
