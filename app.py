"""Streamlit dashboard for WorkflowCommandCenterAgent."""

from __future__ import annotations

import json

import streamlit as st

from workflow_command.checklist_engine import (
    checklist_to_dicts,
    checklist_to_markdown,
    generate_checklist_from_pack,
)
from workflow_command.delivery_report import (
    build_demo_delivery_report,
    generate_delivery_report_markdown,
)
from workflow_command.exporters import export_json, export_markdown, export_text
from workflow_command.models import DeliveryReportInput, ProjectStarterRequest
from workflow_command.prompt_library import (
    filter_prompts_by_category,
    get_demo_prompts,
    list_prompt_categories,
    render_prompt_record,
)
from workflow_command.starter_generator import (
    build_default_wcc_starter,
    generate_project_starter_prompt,
)
from workflow_command.status_tracker import (
    get_demo_project_statuses,
    project_status_table_rows,
    summarize_project_statuses,
)
from workflow_command.workflow_packs import (
    get_demo_workflow_packs,
    get_pack_by_name,
    summarize_workflow_pack,
    workflow_pack_options,
)


CHECKPOINT = "WCC-003-GITHUB-SHOWCASE-PREP"


def main() -> None:
    st.set_page_config(
        page_title="Workflow Command Center Agent",
        page_icon="🧭",
        layout="wide",
    )
    _apply_style()

    st.sidebar.title("Workflow Command")
    st.sidebar.caption("Local-first AI project execution command center")
    st.sidebar.metric("Checkpoint", CHECKPOINT)
    st.sidebar.success("AgentHub-ready manifest: true")
    st.sidebar.info("WCC-003 prepares GitHub showcase assets only; it does not publish or push.")

    tabs = st.tabs(
        [
            "Command Center",
            "Project Starter",
            "Workflow Packs",
            "Checklist Manager",
            "Project Status",
            "Prompt Library",
            "Delivery Report",
            "Export Center",
            "About",
        ]
    )

    with tabs[0]:
        render_command_center()
    with tabs[1]:
        render_project_starter()
    with tabs[2]:
        render_workflow_packs()
    with tabs[3]:
        render_checklist_manager()
    with tabs[4]:
        render_project_status()
    with tabs[5]:
        render_prompt_library()
    with tabs[6]:
        render_delivery_report()
    with tabs[7]:
        render_export_center()
    with tabs[8]:
        render_about()


def render_command_center() -> None:
    st.title("AI Project Execution Command Center")
    st.caption("WorkflowCommandCenterAgent / AI 工作流指令中台")

    col1, col2, col3, col4 = st.columns(4)
    packs = get_demo_workflow_packs()
    projects = get_demo_project_statuses()
    prompts = get_demo_prompts()
    summary = summarize_project_statuses(projects)
    col1.metric("Workflow Packs", len(packs))
    col2.metric("Demo Projects", summary["total_projects"])
    col3.metric("Prompt Categories", len(list_prompt_categories(prompts)))
    col4.metric("Hub Ready", "Yes")

    st.subheader("WCC-003 Scope")
    st.write(
        "This local MVP generates Codex-ready project instructions, reusable workflow packs, "
        "execution checklists, demo project status views, prompt/rule records, and delivery reports. "
        "WCC-003 adds public showcase prep docs, screenshot planning, and release safety checks."
    )

    st.subheader("Portfolio Control Boundary")
    left, right = st.columns(2)
    with left:
        st.markdown(
            """
- Local-first and demo-data-only
- Designed for AI Agent / AI Skill portfolio execution
- AgentHub-ready manifest enhanced
- Showcase prep checklist included
- Markdown, text, and JSON exports available
"""
        )
    with right:
        st.markdown(
            """
- Does not modify `F:\\AIProjects\\AgentHubControlCenter`
- Does not read `.env`, tokens, browser cookies, or private files
- Not a GitHub release checkpoint
- Not a profile pin checkpoint
- Screenshots are planned, not captured
"""
        )


def render_project_starter() -> None:
    st.header("Project Starter Generator")
    default = build_default_wcc_starter()

    with st.form("starter-form"):
        project_name = st.text_input("Project name", value=default.project_name)
        project_path = st.text_input("Project path", value=default.project_path)
        checkpoint = st.text_input("Checkpoint", value=default.checkpoint)
        stage_goal = st.text_area("Stage goal", value=default.stage_goal, height=90)
        project_type = st.text_input("Project type", value=default.project_type)
        files_to_read = st.text_area("Files to read", value="\n".join(default.files_to_read), height=100)
        allowed_actions = st.text_area("Allowed actions", value="\n".join(default.allowed_actions), height=120)
        blocked_actions = st.text_area("Blocked actions", value="\n".join(default.blocked_actions), height=120)
        test_commands = st.text_area("Test commands", value="\n".join(default.test_commands), height=80)
        git_policy = st.text_area("Git policy", value="\n".join(default.git_policy), height=100)
        output_requirements = st.text_area(
            "Output requirements",
            value="\n".join(default.output_requirements),
            height=120,
        )
        submitted = st.form_submit_button("Generate Codex Instruction")

    request = ProjectStarterRequest(
        project_name=project_name,
        project_path=project_path,
        checkpoint=checkpoint,
        stage_goal=stage_goal,
        project_type=project_type,
        files_to_read=_lines(files_to_read),
        allowed_actions=_lines(allowed_actions),
        blocked_actions=_lines(blocked_actions),
        test_commands=_lines(test_commands),
        git_policy=_lines(git_policy),
        output_requirements=_lines(output_requirements),
    )
    prompt = generate_project_starter_prompt(request)
    if submitted:
        st.success("Codex-ready instruction generated.")
    st.text_area("Generated instruction", value=prompt, height=430)
    st.download_button("Download Markdown", prompt, "codex_project_instruction.md", "text/markdown")


def render_workflow_packs() -> None:
    st.header("Workflow Pack Builder")
    options = workflow_pack_options()
    selected = st.selectbox("Workflow pack", options)
    pack = get_pack_by_name(selected)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Category", pack.category)
        st.write(pack.purpose)
        st.download_button(
            "Download JSON",
            export_json(pack),
            f"{pack.pack_name.lower().replace(' ', '_')}.json",
            "application/json",
        )
    with col2:
        summary = summarize_workflow_pack(pack)
        st.markdown(summary)


def render_checklist_manager() -> None:
    st.header("Execution Checklist Manager")
    selected = st.selectbox("Pack for checklist", workflow_pack_options(), key="checklist-pack")
    pack = get_pack_by_name(selected)
    checklist = generate_checklist_from_pack(pack)
    rows = checklist_to_dicts(checklist)
    st.dataframe(rows, use_container_width=True, hide_index=True)
    markdown = checklist_to_markdown(checklist, f"{selected} Checklist")
    st.download_button("Download Checklist Markdown", markdown, "execution_checklist.md", "text/markdown")
    st.download_button("Download Checklist JSON", export_json(rows), "execution_checklist.json", "application/json")


def render_project_status() -> None:
    st.header("Demo Project Status Tracker")
    projects = get_demo_project_statuses()
    summary = summarize_project_statuses(projects)

    col1, col2, col3 = st.columns(3)
    col1.metric("Tracked Projects", summary["total_projects"])
    col2.metric("High Priority", len(summary["high_priority_projects"]))
    col3.metric("Pinned", summary["profile_pin_counts"].get("pinned", 0))

    st.dataframe(project_status_table_rows(projects), use_container_width=True, hide_index=True)
    st.json(summary)


def render_prompt_library() -> None:
    st.header("Prompt / Rule Library")
    categories = list_prompt_categories()
    category = st.selectbox("Category", categories)
    prompts = filter_prompts_by_category(category)

    for prompt in prompts:
        with st.expander(prompt["title"], expanded=True):
            rendered = render_prompt_record(prompt)
            st.markdown(rendered)
            st.download_button(
                f"Download {prompt['title']}",
                rendered,
                f"{prompt['title'].lower().replace(' ', '_')}.md",
                "text/markdown",
            )


def render_delivery_report() -> None:
    st.header("Delivery Report Generator")
    demo = build_demo_delivery_report()

    with st.form("delivery-report-form"):
        project_name = st.text_input("Project name", value=demo.project_name)
        checkpoint = st.text_input("Checkpoint", value=demo.checkpoint)
        stage_goal = st.text_area("Stage goal", value=demo.stage_goal, height=90)
        completed_items = st.text_area("Completed items", value="\n".join(demo.completed_items), height=120)
        modified_files = st.text_area("Modified files", value="\n".join(demo.modified_files), height=120)
        validation_results = st.text_area("Validation results", value="\n".join(demo.validation_results), height=90)
        risks = st.text_area("Risks", value="\n".join(demo.risks), height=90)
        git_status_summary = st.text_area("Git status summary", value=demo.git_status_summary, height=70)
        next_recommended_action = st.text_area(
            "Next recommended action",
            value=demo.next_recommended_action,
            height=70,
        )
        submitted = st.form_submit_button("Generate Delivery Report")

    report_input = DeliveryReportInput(
        project_name=project_name,
        checkpoint=checkpoint,
        stage_goal=stage_goal,
        completed_items=_lines(completed_items),
        modified_files=_lines(modified_files),
        validation_results=_lines(validation_results),
        risks=_lines(risks),
        git_status_summary=git_status_summary,
        next_recommended_action=next_recommended_action,
    )
    report = generate_delivery_report_markdown(report_input)
    if submitted:
        st.success("Delivery report generated.")
    st.markdown(report)
    st.download_button("Download Report Markdown", report, "delivery_report.md", "text/markdown")


def render_export_center() -> None:
    st.header("Export Center")
    export_type = st.selectbox(
        "Export content",
        ["Generated Codex prompt", "Workflow pack summary", "Checklist", "Delivery report"],
    )

    if export_type == "Generated Codex prompt":
        content = generate_project_starter_prompt(build_default_wcc_starter())
        title = "Generated Codex Prompt"
    elif export_type == "Workflow pack summary":
        pack = get_pack_by_name("New Agent MVP Pack")
        content = summarize_workflow_pack(pack)
        title = "Workflow Pack Summary"
    elif export_type == "Checklist":
        pack = get_pack_by_name("New Agent MVP Pack")
        content = checklist_to_dicts(generate_checklist_from_pack(pack))
        title = "Checklist"
    else:
        content = generate_delivery_report_markdown(build_demo_delivery_report())
        title = "Delivery Report"

    markdown = export_markdown(title, content)
    text = export_text(title, content)
    json_text = export_json(content)

    col1, col2, col3 = st.columns(3)
    col1.download_button("Markdown", markdown, "wcc_export.md", "text/markdown")
    col2.download_button("TXT", text, "wcc_export.txt", "text/plain")
    col3.download_button("JSON", json_text, "wcc_export.json", "application/json")

    st.subheader("Preview")
    st.code(markdown, language="markdown")


def render_about() -> None:
    st.header("About")
    st.markdown(
        """
WorkflowCommandCenterAgent is a local-first AI workflow command center for portfolio-grade project execution.

It is not a generic prompt library because it connects project-start instructions, reusable workflow packs,
execution checklists, project status tracking, prompt/rule records, delivery reporting, and export formats
around concrete AI Agent delivery checkpoints.
"""
    )
    st.subheader("Current Boundary")
    st.markdown(
        """
- Current checkpoint: `WCC-003-GITHUB-SHOWCASE-PREP`
- Uses demo data only
- AgentHub-ready manifest has been enhanced
- Does not modify `F:\\AIProjects\\AgentHubControlCenter`
- GitHub public release is a later checkpoint
- Screenshot guide exists, but actual screenshots are not completed
"""
    )
    st.subheader("Agent Manifest Preview")
    with open("agent_manifest.json", "r", encoding="utf-8") as handle:
        st.json(json.load(handle))


def _apply_style() -> None:
    st.markdown(
        """
<style>
div[data-testid="stMetric"] {
    background: #f7f8fa;
    border: 1px solid #e6e8ec;
    border-radius: 8px;
    padding: 14px 16px;
}
.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 8px 12px;
}
</style>
""",
        unsafe_allow_html=True,
    )


def _lines(value: str) -> list[str]:
    return [line.strip() for line in value.splitlines() if line.strip()]


if __name__ == "__main__":
    main()
