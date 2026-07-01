# Screenshots Guide

WCC-004 captures the screenshots needed for the GitHub public showcase.

The screenshot filenames below are fixed and are referenced by `README.md`.

## Screenshot Rules

- Use demo data only.
- Do not show `.env`, tokens, credentials, browser cookies, private folders, or personal account data.
- Keep the browser window clean and focused on the Streamlit UI.
- Do not include terminal output containing private paths beyond the demo project path.
- Capture stable UI states with readable text and no loading spinners.
- Store final images in `screenshots/` only when they are intentionally prepared for public showcase.

## Planned Screenshot Set

### 01_command_center_home.png

Purpose:

- Show the Command Center home tab.
- Show project positioning, checkpoint, and core capability overview.
- Make it clear this is an AI Project Execution Command Center.

Suggested UI state:

- Open `Command Center`.
- Confirm the sidebar shows the current checkpoint.
- Confirm the boundary text states local-first, demo-data-only, and no AgentHubControlCenter modification.

### 02_project_starter_generator.png

Purpose:

- Show the Project Starter Generator.
- Demonstrate Codex-ready project execution instruction generation.

Suggested UI state:

- Open `Project Starter`.
- Keep default WCC-003 values visible.
- Show the generated instruction preview.

### 03_workflow_packs.png

Purpose:

- Show reusable workflow packs.
- Demonstrate New Agent MVP, GitHub Showcase, Bugfix, Status Sync, Report Export, and Commercial Delivery thinking.

Suggested UI state:

- Open `Workflow Packs`.
- Select `GitHub Showcase Pack` or `New Agent MVP Pack`.
- Show purpose, recommended steps, validation commands, and risk notes.

### 04_checklist_manager.png

Purpose:

- Show automatic execution checklist generation.
- Make the project look like a real execution control tool rather than a prompt list.

Suggested UI state:

- Open `Checklist Manager`.
- Select `GitHub Showcase Pack`.
- Show checklist table with titles, descriptions, required flag, and status.

### 05_project_status_tracker.png

Purpose:

- Show demo portfolio matrix status tracking.
- Demonstrate how multiple Agent / Skill projects can be tracked without reading private repos.

Suggested UI state:

- Open `Project Status`.
- Show the metric row and project status table.
- Confirm WorkflowCommandCenterAgent is visible as a demo tracked project.

### 06_prompt_rule_library.png

Purpose:

- Show prompt and rule categories.
- Demonstrate the library is structured by workflow context, not just random prompts.

Suggested UI state:

- Open `Prompt Library`.
- Select a category such as `GitHub Public Release` or `Codex Project Start`.
- Show prompt, usage note, and safety note.

### 07_delivery_report_generator.png

Purpose:

- Show delivery report generation.
- Demonstrate stage summary, modified files, validation results, risks, and next action.

Suggested UI state:

- Open `Delivery Report`.
- Use the default demo WCC-003 report values.
- Show the generated Markdown report preview.

### 08_export_center.png

Purpose:

- Show Markdown / TXT / JSON export capability.
- Demonstrate that generated prompts, workflow summaries, checklists, and reports can become reusable artifacts.

Suggested UI state:

- Open `Export Center`.
- Select `Delivery report` or `Checklist`.
- Show the download buttons and Markdown preview.

## WCC-004 Status

- Screenshot guide ready: yes
- Actual screenshots ready: yes
- Screenshots directory: `screenshots/`
- Screenshot count: 8
