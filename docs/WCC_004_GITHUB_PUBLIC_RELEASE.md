# WCC-004 GitHub Public Release

## Goal

WCC-004 publishes WorkflowCommandCenterAgent as a demo-safe GitHub public showcase project.

This stage includes real Streamlit screenshots, README screenshot references, final release checks, GitHub repository setup, push to `main`, and live README / raw screenshot URL verification.

## Screenshot Completion

WCC-004 captures eight real Streamlit screenshots:

1. `screenshots/01_command_center_home.png`
2. `screenshots/02_project_starter_generator.png`
3. `screenshots/03_workflow_packs.png`
4. `screenshots/04_checklist_manager.png`
5. `screenshots/05_project_status_tracker.png`
6. `screenshots/06_prompt_rule_library.png`
7. `screenshots/07_delivery_report_generator.png`
8. `screenshots/08_export_center.png`

The screenshots use demo data only and are intended for README showcase display.

## README Showcase

The README now includes:

- Project overview
- Explanation of why this is not a simple prompt library
- Core capabilities
- Screenshot showcase with eight real screenshots
- Difference from AgentHubControlCenter
- AgentHub-ready but not AgentHub-integrated boundary
- Local-first and demo-data-only safety model
- Local run commands
- Validation commands
- Current checkpoint and roadmap

## GitHub Repository

Target repo:

`https://github.com/CHENXJC/WorkflowCommandCenterAgent`

Branch:

`main`

## Validation

Required local validation:

```powershell
python -m pytest -q
python -m compileall .
python release/public_release_check.py
python -c "import app; print('APP_IMPORT_OK')"
```

Required online validation:

- GitHub README page returns HTTP 200.
- All eight screenshot raw URLs return HTTP 200.
- Remote tree does not contain unsafe private artifacts.

## Safety Boundary

WCC-004 does not:

- Profile pin
- Modify `F:\AIProjects\AgentHubControlCenter`
- Read `.env`, tokens, credentials, cookies, or passwords
- Submit private data
- Include generated private outputs
- Force push

## Not Done

- Profile Pin: not done
- AgentHubControlCenter integration: not done
- SaaS production hardening: not done
- Paid API integration: not done

## Next Stage

Recommended optional next step:

`optional-profile-pin-or-agenthub-integration`

Profile pinning should remain a separate explicit decision.
