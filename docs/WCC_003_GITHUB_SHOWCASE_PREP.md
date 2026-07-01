# WCC-003 GitHub Showcase Prep

## Goal

WCC-003 prepares WorkflowCommandCenterAgent for a future GitHub public showcase release.

The goal is showcase readiness: README clarity, screenshot planning, public showcase checklist, release manifest accuracy, release-prep safety checks, and tests.

WCC-003 is not GitHub public release.

## Why Showcase Prep Matters

WorkflowCommandCenterAgent is a portfolio-facing project. Before publishing it, the project needs to clearly show:

- what problem it solves,
- why it is not a generic prompt library,
- how it fits the AI Agent portfolio matrix,
- how it differs from AgentHubControlCenter,
- how it runs locally,
- what demo data it uses,
- what safety boundaries it follows,
- what validation proves.

This stage improves the public-facing story without claiming GitHub release or profile pin completion.

## What Changed

- Added `docs/SCREENSHOTS_GUIDE.md`.
- Added `docs/PUBLIC_SHOWCASE_CHECKLIST.md`.
- Added `docs/WCC_003_GITHUB_SHOWCASE_PREP.md`.
- Added `screenshots/.gitkeep` as a placeholder only.
- Added `release/public_release_check.py`.
- Updated README with stronger showcase sections.
- Updated `PROJECT_STATUS.md` for WCC-003.
- Updated `agent_manifest.json` and `release/public_showcase_manifest.json`.
- Added tests for showcase prep docs and manifest fields.

## Screenshot Plan

The planned screenshot set is:

1. `01_command_center_home.png`
2. `02_project_starter_generator.png`
3. `03_workflow_packs.png`
4. `04_checklist_manager.png`
5. `05_project_status_tracker.png`
6. `06_prompt_rule_library.png`
7. `07_delivery_report_generator.png`
8. `08_export_center.png`

Actual screenshots are not created in WCC-003.

## README Showcase Enhancements

The README now emphasizes:

- Project Overview
- Why this is not a simple prompt library
- Core Capabilities
- UI Preview / Screenshot Plan
- WorkflowCommandCenterAgent vs AgentHubControlCenter
- AgentHub-ready but not AgentHub-integrated
- Local-first and demo-data-only safety model
- Current Status
- Validation
- Roadmap

## Safety Checks

WCC-003 keeps these boundaries:

- No GitHub remote configured.
- No push performed.
- No GitHub public release completed.
- No profile pin.
- No modification to `F:\AIProjects\AgentHubControlCenter`.
- No `.env`, token, credential, cookie, password, or private data read.
- No fake screenshots.

## Current Release State

- Current checkpoint: `WCC-003-GITHUB-SHOWCASE-PREP-COMPLETE`
- Release stage: `github-showcase-prep`
- GitHub public release completed: false
- GitHub repo: not configured
- Screenshot guide ready: true
- Actual screenshots ready: false
- Public showcase checklist ready: true
- AgentHub modified: false

## Validation

Run from `F:\AIProjects\WorkflowCommandCenterAgent`:

```powershell
python -m pytest -q
python -m compileall .
python release/public_release_check.py
python -c "import app; print('APP_IMPORT_OK')"
```

## Next Stage

Recommended next checkpoint:

`WCC-004-GITHUB-PUBLIC-RELEASE`

WCC-004 should only start when the user explicitly wants GitHub publishing work.
