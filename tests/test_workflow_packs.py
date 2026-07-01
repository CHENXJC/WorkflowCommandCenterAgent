from workflow_command.workflow_packs import (
    get_demo_workflow_packs,
    get_pack_by_name,
    summarize_workflow_pack,
)


def test_demo_workflow_packs_have_required_six_packs():
    packs = get_demo_workflow_packs()
    names = {pack.pack_name for pack in packs}

    assert len(packs) >= 6
    assert {
        "New Agent MVP Pack",
        "GitHub Showcase Pack",
        "Bugfix Pack",
        "Status Sync Pack",
        "Report Export Pack",
        "Commercial Delivery Pack",
    }.issubset(names)


def test_workflow_pack_summary_contains_sections():
    pack = get_pack_by_name("New Agent MVP Pack")
    summary = summarize_workflow_pack(pack)

    assert "# New Agent MVP Pack" in summary
    assert "Recommended Steps" in summary
    assert "Validation Commands" in summary
    assert "Risk Notes" in summary
