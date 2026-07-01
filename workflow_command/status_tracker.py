"""Demo project status tracker."""

from __future__ import annotations

from collections import Counter
from typing import Any

from .demo_data import load_demo_projects


def get_demo_project_statuses() -> list[dict[str, Any]]:
    return load_demo_projects()


def filter_projects_by_priority(priority: str) -> list[dict[str, Any]]:
    priority_normalized = priority.strip().lower()
    return [
        project
        for project in get_demo_project_statuses()
        if str(project.get("priority", "")).lower() == priority_normalized
    ]


def summarize_project_statuses(projects: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    records = projects if projects is not None else get_demo_project_statuses()
    status_counts = Counter(str(project.get("status", "unknown")) for project in records)
    pin_counts = Counter(str(project.get("profile_pin_status", "unknown")) for project in records)
    github_counts = Counter(str(project.get("github_status", "unknown")) for project in records)
    high_priority = [project["project_name"] for project in records if str(project.get("priority", "")).lower() == "high"]

    return {
        "total_projects": len(records),
        "status_counts": dict(status_counts),
        "profile_pin_counts": dict(pin_counts),
        "github_counts": dict(github_counts),
        "high_priority_projects": high_priority,
    }


def project_status_table_rows(projects: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    records = projects if projects is not None else get_demo_project_statuses()
    columns = [
        "project_name",
        "category",
        "current_checkpoint",
        "status",
        "github_status",
        "profile_pin_status",
        "next_action",
        "priority",
        "notes",
    ]
    return [{column: project.get(column, "") for column in columns} for project in records]
