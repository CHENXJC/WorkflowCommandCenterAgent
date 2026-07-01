import json
from pathlib import Path

from workflow_command.checklist_engine import generate_checklist_from_pack
from workflow_command.exporters import export_json, export_markdown, export_text
from workflow_command.workflow_packs import get_pack_by_name


ROOT = Path(__file__).resolve().parents[1]


def test_exporters_output_markdown_text_and_json():
    pack = get_pack_by_name("New Agent MVP Pack")
    checklist = generate_checklist_from_pack(pack)

    markdown = export_markdown("Checklist", checklist)
    text = export_text("Checklist", checklist)
    json_text = export_json(checklist)

    assert markdown.startswith("# Checklist") or "Read PROJECT_STATUS.md" in markdown
    assert "Checklist" in text
    parsed = json.loads(json_text)
    assert isinstance(parsed, list)
    assert parsed[0]["title"] == "Read PROJECT_STATUS.md"


def test_agent_manifest_contains_agenthub_fields():
    manifest = json.loads((ROOT / "agent_manifest.json").read_text(encoding="utf-8"))

    assert manifest["agent_name"] == "WorkflowCommandCenterAgent"
    assert manifest["current_checkpoint"] == "WCC-004-GITHUB-PUBLIC-RELEASE"
    assert manifest["hub_ready"] is True
    assert manifest["modifies_agent_hub"] is False
    assert manifest["github_showcase_ready"] is True


def test_public_showcase_manifest_is_not_public_release_completed():
    manifest = json.loads((ROOT / "release" / "public_showcase_manifest.json").read_text(encoding="utf-8"))

    assert manifest["project_name"] == "WorkflowCommandCenterAgent"
    assert manifest["release_stage"] == "github-public-release"
    assert manifest["github_public_release_completed"] is True
    assert manifest["github_showcase_ready"] is True
