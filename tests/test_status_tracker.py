from workflow_command.status_tracker import (
    get_demo_project_statuses,
    project_status_table_rows,
    summarize_project_statuses,
)


def test_status_tracker_loads_required_demo_projects():
    projects = get_demo_project_statuses()
    names = {project["project_name"] for project in projects}

    assert len(projects) >= 10
    assert {
        "VideoExtractSkill",
        "MarketSenseAgent",
        "QuantLabAgent",
        "SocialPainFinderAgent",
        "CareerPilotAgent",
        "NewsSignalAgent",
        "BusinessOpsAgent",
        "AgentHubControlCenter",
        "WorkflowPackAgent",
        "WorkflowCommandCenterAgent",
    }.issubset(names)


def test_status_tracker_summary_and_table_rows():
    projects = get_demo_project_statuses()
    summary = summarize_project_statuses(projects)
    rows = project_status_table_rows(projects)

    assert summary["total_projects"] == len(projects)
    assert "WorkflowCommandCenterAgent" in summary["high_priority_projects"]
    assert len(rows) == len(projects)
    assert "current_checkpoint" in rows[0]
