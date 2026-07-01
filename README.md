# WorkflowCommandCenterAgent

AI 工作流指令中台 / 项目启动与执行控制台。

WorkflowCommandCenterAgent is a local-first AI project execution command center for generating Codex-ready project instructions, reusable workflow packs, execution checklists, demo portfolio status views, prompt/rule records, delivery reports, and exportable Markdown / TXT / JSON artifacts.

## Project Overview

This project is the "project execution command center" in an AI Agent portfolio matrix.

It helps an AI product creator, automation consultant, or Agent builder repeatedly answer:

- What should Codex do next?
- Which files should be read first?
- What actions are allowed or blocked?
- Which validation commands should run?
- What checklist should guide the execution?
- What delivery report should summarize the checkpoint?
- What public showcase boundaries must be respected?

## Why This Is Not A Simple Prompt Library

WorkflowCommandCenterAgent is built around checkpoint-based delivery, not isolated prompt snippets.

It connects:

- project starter instructions,
- reusable workflow packs,
- execution checklist generation,
- demo portfolio status tracking,
- prompt and rule records,
- delivery report generation,
- public showcase prep checks,
- Markdown, TXT, and JSON exports.

A normal prompt library stores text. This project turns repeated AI project execution into a structured local workflow.

## Target Users

- AI Agent / AI Skill builders
- Local-first automation creators
- Portfolio project maintainers
- SME workflow automation consultants
- Codex / ChatGPT users who repeatedly run staged project work

## Core Capabilities

- Project Starter Generator for Codex-ready execution instructions
- Workflow Pack Builder with six demo workflow packs
- Execution Checklist Manager generated from workflow packs
- Demo Project Status Tracker for the AI Agent portfolio matrix
- Prompt / Rule Library with workflow-specific categories
- Delivery Report Generator for checkpoint summaries
- Markdown / TXT / JSON export helpers
- AgentHub-ready `agent_manifest.json`
- GitHub showcase prep docs and checklist
- Public release prep check script

## Current Status

- Current checkpoint: `WCC-003-GITHUB-SHOWCASE-PREP-COMPLETE`
- Stage type: GitHub showcase preparation
- GitHub public release: not completed
- GitHub remote: not configured
- GitHub push: not performed
- Profile pin: not applicable yet
- Screenshot guide: ready
- Actual screenshots: not completed
- Demo mode: yes
- Privacy mode: local-first demo data only

## UI Preview / Screenshot Plan

Planned screenshots are documented in [docs/SCREENSHOTS_GUIDE.md](docs/SCREENSHOTS_GUIDE.md).

Actual screenshots will be added during `WCC-004-GITHUB-PUBLIC-RELEASE` if the user explicitly starts the GitHub release stage. WCC-003 does not create or fake screenshot files.

Planned screenshot set:

- `01_command_center_home.png`
- `02_project_starter_generator.png`
- `03_workflow_packs.png`
- `04_checklist_manager.png`
- `05_project_status_tracker.png`
- `06_prompt_rule_library.png`
- `07_delivery_report_generator.png`
- `08_export_center.png`

## WorkflowCommandCenterAgent vs AgentHubControlCenter

AgentHubControlCenter = portfolio visibility / agent registry.

WorkflowCommandCenterAgent = project execution / Codex instruction command center.

AgentHubControlCenter should show which agents exist, their status, priority, and next actions. WorkflowCommandCenterAgent helps generate the concrete instruction packs, checklist items, reports, and showcase prep artifacts used to execute those next actions.

## AgentHub-Ready, Not AgentHub-Integrated

WCC-002 prepared the internal manifest contract for future AgentHubControlCenter recognition.

WCC-003 keeps that readiness while adding GitHub showcase prep assets.

Important boundary:

- `agent_manifest.json` is AgentHub-ready.
- `hub_ready` remains true.
- `modifies_agent_hub` remains false.
- `F:\AIProjects\AgentHubControlCenter` is not modified.
- Actual AgentHub integration remains a future explicit task.

## Local-First And Demo-Data-Only Safety Model

The project uses checked-in demo JSON files only:

- `data/demo_projects.json`
- `data/demo_workflow_packs.json`
- `data/demo_prompts.json`

It does not read real private project files, `.env`, tokens, credentials, browser cookies, Gmail data, GitHub tokens, or generated private outputs.

WCC-003 also keeps these boundaries:

- no GitHub remote configuration,
- no push,
- no GitHub public release,
- no profile pin,
- no fake screenshots,
- no AgentHubControlCenter modification.

## How To Run

```powershell
cd F:\AIProjects\WorkflowCommandCenterAgent
python -m pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal, usually `http://localhost:8501`.

## Validation

```powershell
cd F:\AIProjects\WorkflowCommandCenterAgent
python -m pytest -q
python -m compileall .
python release/public_release_check.py
python -c "import app; print('APP_IMPORT_OK')"
```

## Project Structure

```text
WorkflowCommandCenterAgent/
├─ app.py
├─ workflow_command/
├─ data/
│  ├─ demo_projects.json
│  ├─ demo_workflow_packs.json
│  └─ demo_prompts.json
├─ docs/
│  ├─ PROJECT_PLAN.md
│  ├─ AGENTHUB_INTEGRATION.md
│  ├─ WCC_002_AGENTHUB_READINESS.md
│  ├─ SCREENSHOTS_GUIDE.md
│  ├─ PUBLIC_SHOWCASE_CHECKLIST.md
│  └─ WCC_003_GITHUB_SHOWCASE_PREP.md
├─ release/
│  ├─ public_showcase_manifest.json
│  └─ public_release_check.py
├─ screenshots/
│  └─ .gitkeep
├─ tests/
├─ agent_manifest.json
├─ README.md
├─ PROJECT_STATUS.md
├─ requirements.txt
└─ .gitignore
```

## Roadmap

- `WCC-001-LOCAL-MVP-COMPLETE`: local MVP completed
- `WCC-002-AGENTHUB-READINESS-COMPLETE`: AgentHub-ready local metadata completed
- `WCC-003-GITHUB-SHOWCASE-PREP-COMPLETE`: GitHub showcase prep assets completed
- `WCC-004-GITHUB-PUBLIC-RELEASE`: publish demo-safe GitHub public showcase only when explicitly requested
- Later: optional AgentHubControlCenter integration after approval

## Disclaimer

WorkflowCommandCenterAgent is a local workflow and portfolio execution tool. It is not a secure secrets manager, not an account automation system, not a production SaaS platform, and not a GitHub public release in WCC-003.
