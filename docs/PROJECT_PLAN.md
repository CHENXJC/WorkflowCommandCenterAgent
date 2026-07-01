# WorkflowCommandCenterAgent Project Plan

## Project Positioning

WorkflowCommandCenterAgent is a local-first AI project execution command center.

It helps an AI product creator, AI Skill builder, or automation consultant turn repeated project execution work into structured, reusable workflows:

- Generate Codex-ready project starter instructions
- Build and reuse workflow packs
- Convert workflow packs into execution checklists
- Track demo portfolio project status
- Maintain prompt and rule libraries
- Generate delivery reports
- Export Markdown, TXT, and JSON artifacts

This project fills the "project execution war room" slot in the AI Agent portfolio matrix. It is not a normal todo app and not a generic prompt library because its core object is a checkpoint-based AI project delivery workflow.

## Business And Portfolio Value

Target user:

- Solo AI product creator
- Local automation consultant
- SME workflow automation builder
- Portfolio maintainer using Codex / ChatGPT for repeated project delivery

Pain points:

- Rewriting similar Codex instructions for every project
- Forgetting project safety boundaries
- Losing track of checkpoint status across multiple AI Agent projects
- Mixing GitHub release work with local MVP work
- Manually formatting delivery reports after each stage

Portfolio value:

- Shows AI workflow orchestration thinking
- Shows business-aware project management for Agent delivery
- Complements AgentHubControlCenter without replacing it
- Creates a reusable command layer for future AI Skill / Agent projects

## Stage Roadmap

### WCC-001-LOCAL-MVP

Scope:

- Create local project structure
- Implement core Python modules
- Add demo workflow packs
- Add checklist generation
- Add demo project status tracking
- Add prompt/rule library
- Add delivery report generation
- Add Markdown / TXT / JSON export helpers
- Build Streamlit dashboard
- Add README, PROJECT_STATUS, and project plan
- Add `agent_manifest.json`
- Add `release/public_showcase_manifest.json`
- Add focused tests

Explicitly out of scope:

- Modifying `F:\AIProjects\AgentHubControlCenter`
- GitHub public release
- GitHub profile pin
- Real private data ingestion
- Paid API integration
- SaaS hardening

### WCC-002-AGENTHUB-READINESS

Completed scope:

- Refine `agent_manifest.json`
- Add richer capability and status metadata
- Add compatibility notes for AgentHubControlCenter
- Add future integration documentation
- Add WCC-002 readiness summary
- Add tests for manifest and readiness docs

Boundary:

- Did not modify `F:\AIProjects\AgentHubControlCenter`.

Final checkpoint:

`WCC-002-AGENTHUB-READINESS-COMPLETE`

### WCC-003-GITHUB-SHOWCASE-PREP

Completed scope:

- Add `docs/SCREENSHOTS_GUIDE.md`
- Add `docs/PUBLIC_SHOWCASE_CHECKLIST.md`
- Add `docs/WCC_003_GITHUB_SHOWCASE_PREP.md`
- Polish README screenshots and feature sections
- Add public safety checklist
- Add release audit script
- Confirm no generated private outputs are tracked

Boundary:

- Did not configure GitHub remote.
- Did not push.
- Did not mark public release as complete.
- Did not create fake screenshots.
- Did not modify `F:\AIProjects\AgentHubControlCenter`.

Final checkpoint:

`WCC-003-GITHUB-SHOWCASE-PREP-COMPLETE`

### WCC-004-GITHUB-PUBLIC-RELEASE

Potential scope:

- Create or connect GitHub repository only when explicitly requested
- Publish demo-safe files
- Set GitHub About and topics
- Verify remote tree safety
- Decide whether profile pin is appropriate

## Data Flow

```text
Project request
  -> Project Starter Generator
  -> Workflow Pack Builder
  -> Checklist Manager
  -> Delivery Report Generator
  -> Markdown / TXT / JSON Export

Demo portfolio data
  -> Project Status Tracker
  -> Command Center dashboard

Prompt records
  -> Prompt / Rule Library
  -> Export Center
```

## Technical Structure

- Python modules under `workflow_command/`
- Demo data under `data/`
- Streamlit UI in `app.py`
- Tests under `tests/`
- AgentHub-compatible metadata in `agent_manifest.json`
- Public release status in `release/public_showcase_manifest.json`

## Validation Plan

```powershell
cd F:\AIProjects\WorkflowCommandCenterAgent
python -m pytest -q
python -m compileall .
python -m json.tool agent_manifest.json
python -m json.tool release/public_showcase_manifest.json
```

## Safety And Privacy Boundary

- Local-first execution
- Demo data only
- No `.env` reads
- No credentials or tokens
- No browser cookies
- No private project file scanning
- No remote GitHub push in WCC-001, WCC-002, or WCC-003
- No AgentHubControlCenter modification in WCC-001, WCC-002, or WCC-003

## WCC-003 Showcase Boundary

WCC-003 prepares GitHub showcase assets inside this project. It does not edit, import from, or write to `F:\AIProjects\AgentHubControlCenter`, does not configure a GitHub remote, does not push, and does not mark public release as complete.
