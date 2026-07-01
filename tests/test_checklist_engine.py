from workflow_command.checklist_engine import (
    checklist_to_markdown,
    generate_checklist_from_pack,
)
from workflow_command.workflow_packs import get_pack_by_name


def test_checklist_can_be_generated_from_pack():
    pack = get_pack_by_name("Bugfix Pack")
    checklist = generate_checklist_from_pack(pack)

    assert checklist
    assert any(item.title == "Read PROJECT_STATUS.md" for item in checklist)
    assert any(item.title == "Reproduce the bug" for item in checklist)
    assert all(item.status in {"pending", "in_progress", "done", "skipped"} for item in checklist)
    assert all(hasattr(item, "required") for item in checklist)


def test_checklist_markdown_contains_status_and_description():
    pack = get_pack_by_name("New Agent MVP Pack")
    checklist = generate_checklist_from_pack(pack)
    markdown = checklist_to_markdown(checklist)

    assert "Execution Checklist" in markdown
    assert "pending" in markdown
    assert "Read README.md" in markdown
