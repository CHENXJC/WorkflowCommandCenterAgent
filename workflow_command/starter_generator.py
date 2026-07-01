"""Generate structured Codex-ready project starter prompts."""

from __future__ import annotations

from typing import Any

from .models import ProjectStarterRequest


DEFAULT_BLOCKED_ACTIONS = [
    "Do not read .env, credentials, browser cookies, tokens, or private data.",
    "Do not modify unrelated projects or external repositories.",
    "Do not use git add . or force push.",
    "Do not connect paid APIs unless explicitly requested.",
]


def generate_project_starter_prompt(payload: ProjectStarterRequest | dict[str, Any]) -> str:
    """Return a copy-ready Codex execution instruction."""

    request = payload if isinstance(payload, ProjectStarterRequest) else ProjectStarterRequest.from_mapping(payload)
    blocked_actions = request.blocked_actions or DEFAULT_BLOCKED_ACTIONS

    return "\n".join(
        [
            f"# Codex Project Execution Instruction: {request.project_name}",
            "",
            "## 1. Project Context",
            f"- Project name: {request.project_name}",
            f"- Project path: {request.project_path}",
            f"- Project type: {request.project_type}",
            f"- Current checkpoint: {request.checkpoint}",
            f"- Stage goal: {request.stage_goal}",
            "",
            "## 2. Files To Read First",
            _bullet_list(request.files_to_read or ["AGENTS.md", "PROJECT_STATUS.md", "README.md", "docs/"]),
            "",
            "## 3. Allowed Actions",
            _bullet_list(request.allowed_actions or ["Inspect structure", "Make minimal scoped edits", "Add tests", "Update docs"]),
            "",
            "## 4. Blocked Actions",
            _bullet_list(blocked_actions),
            "",
            "## 5. Test Commands",
            _bullet_list(request.test_commands or ["python -m pytest -q", "python -m compileall ."]),
            "",
            "## 6. Git Policy",
            _bullet_list(
                request.git_policy
                or [
                    "Run git status before staging.",
                    "Stage only explicit files changed in this task.",
                    "Do not push unless the user explicitly asks.",
                ]
            ),
            "",
            "## 7. Final Output Requirements",
            _bullet_list(
                request.output_requirements
                or [
                    "Summarize completed work.",
                    "List modified files.",
                    "Report validation results honestly.",
                    "State current checkpoint and next recommended action.",
                ]
            ),
            "",
            "## 8. Delivery Boundary",
            "Keep the work local-first, demo-safe, and scoped to the current checkpoint.",
        ]
    )


def build_default_wcc_starter() -> ProjectStarterRequest:
    return ProjectStarterRequest(
        project_name="WorkflowCommandCenterAgent",
        project_path=r"F:\AIProjects\WorkflowCommandCenterAgent",
        checkpoint="WCC-001-LOCAL-MVP",
        stage_goal="Create a local Streamlit MVP with workflow packs, checklists, demo status tracking, prompt library, reports, exports, tests, docs, and AgentHub-ready manifests.",
        project_type="Local-first Streamlit AI workflow command center",
        files_to_read=[
            "README.md",
            "PROJECT_STATUS.md",
            "docs/PROJECT_PLAN.md",
            "agent_manifest.json",
        ],
        allowed_actions=[
            "Create and edit files inside F:\\AIProjects\\WorkflowCommandCenterAgent only.",
            "Use demo data for project status, prompts, and workflow packs.",
            "Run pytest, compileall, and optional Streamlit smoke checks.",
            "Initialize local git and commit selected files only.",
        ],
        blocked_actions=[
            "Do not read .env, credentials, tokens, browser cookies, or private files.",
            "Do not modify F:\\AIProjects\\AgentHubControlCenter during WCC-001.",
            "Do not connect GitHub remote, push, or force push.",
            "Do not use git add .",
        ],
        test_commands=[
            "python -m pytest -q",
            "python -m compileall .",
        ],
        git_policy=[
            "Run git status before staging.",
            "Stage explicit WCC project files only.",
            "Commit message: feat: create WorkflowCommandCenterAgent local MVP",
            "Do not push.",
        ],
        output_requirements=[
            "Confirm whether WCC-001 is complete.",
            "List core modules created.",
            "Show Streamlit launch command.",
            "Report pytest and compileall results.",
            "Report git commit and push status.",
            "Mark checkpoint as WCC-001-LOCAL-MVP-COMPLETE when complete.",
        ],
    )


def _bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)
