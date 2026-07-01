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

## Demo / Screenshot Area

WCC-001 focuses on local MVP functionality. Screenshots can be added in a later GitHub showcase checkpoint after UI review.

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
│  └─ PROJECT_PLAN.md
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

WCC-001 includes `agent_manifest.json` with AgentHub-ready fields such as `hub_ready`, `modifies_agent_hub`, `launch_command`, and `core_capabilities`.

Important boundary: WCC-001 does not modify `F:\AIProjects\AgentHubControlCenter`. Actual AgentHub integration should be a later checkpoint after the local MVP is stable.

## Current MVP Status

- Current checkpoint: `WCC-001-LOCAL-MVP-COMPLETE`
- Stage type: local MVP
- GitHub showcase ready: no
- Profile pin ready: no
- Demo mode: yes

## Safety Boundary

- Local-first
- Demo data only
- No `.env` reads
- No secret, token, cookie, or credential access
- No remote GitHub push in WCC-001
- No modification to `AgentHubControlCenter` in WCC-001
- No production SaaS or client delivery claims

## Future Roadmap

- `WCC-002-AGENTHUB-READINESS`: polish manifest/status fields and prepare integration contract
- `WCC-003-SHOWCASE-PREP`: screenshot guide, README polish, public safety manifest, release checklist
- `WCC-004-GITHUB-PUBLIC`: publish demo-safe GitHub public showcase when explicitly requested
- Later: optional AgentHubControlCenter integration after approval

## Disclaimer

WorkflowCommandCenterAgent is a local workflow and portfolio execution tool. It is not a secure secrets manager, not an account automation system, and not a production SaaS platform in WCC-001.
