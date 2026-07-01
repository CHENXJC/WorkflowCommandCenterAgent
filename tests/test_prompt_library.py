from workflow_command.prompt_library import (
    filter_prompts_by_category,
    get_demo_prompts,
    list_prompt_categories,
    render_prompt_record,
)


def test_prompt_library_loads_required_categories():
    prompts = get_demo_prompts()
    categories = set(list_prompt_categories(prompts))

    assert len(prompts) >= 10
    assert {
        "Codex Project Start",
        "Codex Continue Project",
        "GitHub Public Release",
        "Screenshot / README Polish",
        "Bugfix",
        "Status Sync",
        "Video / Image Analysis",
        "Business Analysis",
        "Study / Assignment Support",
        "Outreach / Email Draft",
    }.issubset(categories)


def test_prompt_record_rendering_contains_safety_note():
    prompt = filter_prompts_by_category("Bugfix")[0]
    rendered = render_prompt_record(prompt)

    assert "# Scoped Bugfix" in rendered
    assert "Safety Note" in rendered
