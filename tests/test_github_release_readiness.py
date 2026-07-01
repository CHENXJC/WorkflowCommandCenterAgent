import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCREENSHOTS = [
    "screenshots/01_command_center_home.png",
    "screenshots/02_project_starter_generator.png",
    "screenshots/03_workflow_packs.png",
    "screenshots/04_checklist_manager.png",
    "screenshots/05_project_status_tracker.png",
    "screenshots/06_prompt_rule_library.png",
    "screenshots/07_delivery_report_generator.png",
    "screenshots/08_export_center.png",
]


def test_eight_release_screenshots_exist_and_are_png_files():
    for relative_path in SCREENSHOTS:
        path = ROOT / relative_path
        assert path.exists(), relative_path
        assert path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_readme_references_all_release_screenshots():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    for relative_path in SCREENSHOTS:
        assert relative_path in readme


def test_release_manifest_marks_public_release_complete_without_pin_or_agenthub_change():
    manifest = json.loads((ROOT / "release" / "public_showcase_manifest.json").read_text(encoding="utf-8"))

    assert manifest["github_public_release_completed"] is True
    assert manifest["screenshots_ready"] is True
    assert manifest["screenshot_count"] == 8
    assert manifest["agenthub_modified"] is False
    assert manifest["profile_pin_status"] == "not_pinned"


def test_agent_manifest_marks_showcase_ready_without_agenthub_change_or_profile_pin():
    manifest = json.loads((ROOT / "agent_manifest.json").read_text(encoding="utf-8"))

    assert manifest["github_showcase_ready"] is True
    assert manifest["modifies_agent_hub"] is False
    assert manifest["profile_pin_status"] == "not_pinned"
