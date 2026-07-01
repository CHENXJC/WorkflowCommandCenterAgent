from workflow_command.starter_generator import (
    build_default_wcc_starter,
    generate_project_starter_prompt,
)


def test_project_starter_prompt_contains_required_fields():
    prompt = generate_project_starter_prompt(build_default_wcc_starter())

    assert "WorkflowCommandCenterAgent" in prompt
    assert r"F:\AIProjects\WorkflowCommandCenterAgent" in prompt
    assert "WCC-002-AGENTHUB-READINESS" in prompt
    assert "Files To Read First" in prompt
    assert "Allowed Actions" in prompt
    assert "Blocked Actions" in prompt
    assert "Test Commands" in prompt
    assert "Git Policy" in prompt
    assert "Final Output Requirements" in prompt
