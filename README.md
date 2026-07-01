# WorkflowCommandCenterAgent

AI 工作流指令中台 / 项目启动与执行控制台。

WorkflowCommandCenterAgent is a local-first AI project execution command center for generating Codex-ready project instructions, building reusable workflow packs, managing execution checklists, tracking demo project delivery status, maintaining prompt/rule libraries, and exporting structured delivery reports.

## Why This Is Not A Generic Prompt Library

This project is built around project delivery checkpoints, not isolated prompt snippets. It connects:

- Project starter instructions
- Reusable workflow packs
- Execution checklist generation
- Demo portfolio project status tracking
- Prompt and rule records
- Delivery report generation
- Markdown, TXT, and JSON exports

The goal is to help an AI product creator or automation consultant turn repeated Codex / ChatGPT project execution work into a reusable local workflow.

## Target Users

- AI Agent / AI Skill builders
- Local-first automation creators
- Portfolio project maintainers
- Business workflow consultants preparing repeatable delivery templates

## Core Features

- Project Starter Generator for Codex-ready execution instructions
- Workflow Pack Builder with six demo workflow packs
- Execution Checklist Manager generated from workflow packs
- Demo Project Status Tracker for the AI Agent portfolio matrix
- Prompt / Rule Library with ten practical categories
- Delivery Report Generator for checkpoint summaries
- Markdown / TXT / JSON export helpers
- AgentHub-ready `agent_manifest.json`

## Current Status

- Current checkpoint: `WCC-002-AGENTHUB-READINESS-COMPLETE`
- Stage type: local MVP plus AgentHub readiness
- GitHub public release: not completed
- GitHub remote: not configured
- Profile pin: not applicable yet
- Demo mode: yes
- Privacy mode: local-first demo data only

## Portfolio Role

WorkflowCommandCenterAgent is the project execution command center in the AI Agent portfolio matrix.

It supports repeated delivery work: project start instructions, continuation instructions, workflow packs, execution checklists, status summaries, prompt/rule records, and delivery reports.

## AgentHub Readiness

WCC-002 enhances the internal manifest contract so AgentHubControlCenter can recognize this project in a future integration checkpoint.

AgentHub-ready fields now include:

- `subcategory`
- `lifecycle_stage`
- `local_path`
- `github_repo`
- `profile_pin_status`
- `key_modules`
- `ui_tabs`
- `validation_commands`
- `last_validation`
- `integration_notes`
- `next_recommended_action`

This is readiness only. WCC-002 does not modify `F:\AIProjects\AgentHubControlCenter`.

## Difference From AgentHubControlCenter

AgentHubControlCenter = portfolio visibility / agent registry.

WorkflowCommandCenterAgent = project execution / Codex instruction command center.

AgentHubControlCenter should show which agents exist, their status, priority, and next actions. WorkflowCommandCenterAgent helps generate the concrete instruction packs, checklist items, and reports used to execute those next actions.

## Demo / Screenshot Area

WCC-002 focuses on local MVP plus AgentHub readiness. Screenshots can be added in a later GitHub showcase checkpoint after UI review.

Recommended future screenshots:

- Command Center overview
- Project Starter generated instruction
- Workflow Pack detail
- Checklist Manager table
- Project Status tracker
- Delivery Report preview

## How To Run

```powershell
cd F:\AIProjects\WorkflowCommandCenterAgent
python -m pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal, usually `http://localhost:8501`.

## Project Structure

```text
WorkflowCommandCenterAgent/
├─ app.py
├─ workflow_command/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ demo_data.py
│  ├─ starter_generator.py
│  ├─ workflow_packs.py
│  ├─ checklist_engine.py
│  ├─ status_tracker.py
│  ├─ prompt_library.py
│  ├─ delivery_report.py
│  └─ exporters.py
├─ data/
│  ├─ demo_projects.json
│  ├─ demo_workflow_packs.json
│  └─ demo_prompts.json
├─ docs/
│  ├─ PROJECT_PLAN.md
│  ├─ AGENTHUB_INTEGRATION.md
│  └─ WCC_002_AGENTHUB_READINESS.md
├─ tests/
├─ release/
│  └─ public_showcase_manifest.json
├─ agent_manifest.json
├─ README.md
├─ PROJECT_STATUS.md
├─ requirements.txt
└─ .gitignore
```

## Demo Data

The project uses checked-in demo JSON files only:

- `data/demo_projects.json`
- `data/demo_workflow_packs.json`
- `data/demo_prompts.json`

It does not read real private project files, `.env`, tokens, credentials, browser cookies, Gmail data, GitHub tokens, or generated private outputs.

## AgentHub Future Integration

WCC-002 includes an enhanced `agent_manifest.json` with AgentHub-ready fields such as `subcategory`, `lifecycle_stage`, `local_path`, `key_modules`, `ui_tabs`, `last_validation`, and `integration_notes`.

Important boundary: WCC-002 does not modify `F:\AIProjects\AgentHubControlCenter`. Actual AgentHub integration should be a later checkpoint after this project is stable and explicitly approved.

## Safety Boundary

- Local-first
- Demo data only
- No `.env` reads
- No secret, token, cookie, or credential access
- No remote GitHub push in WCC-002
- No modification to `AgentHubControlCenter` in WCC-002
- No production SaaS or client delivery claims

## Validation Commands

```powershell
cd F:\AIProjects\WorkflowCommandCenterAgent
python -m pytest -q
python -m compileall .
python -c "import app; print('APP_IMPORT_OK')"
```

## Future Roadmap

- `WCC-003-GITHUB-SHOWCASE-PREP`: screenshot guide, README polish, public safety manifest, release checklist
- `WCC-004-GITHUB-PUBLIC`: publish demo-safe GitHub public showcase when explicitly requested
- Later: optional AgentHubControlCenter integration after approval

## Disclaimer

WorkflowCommandCenterAgent is a local workflow and portfolio execution tool. It is not a secure secrets manager, not an account automation system, and not a production SaaS platform in WCC-002.
