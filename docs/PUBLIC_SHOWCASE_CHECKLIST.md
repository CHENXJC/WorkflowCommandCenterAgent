# Public Showcase Checklist

This checklist prepares WorkflowCommandCenterAgent for a future GitHub public showcase. WCC-003 is prep only; it is not GitHub public release.

## README Readiness

- [x] README explains the project positioning.
- [x] README explains why this is not a simple prompt library.
- [x] README lists core capabilities.
- [x] README includes local run commands.
- [x] README explains demo data and local-first safety.
- [x] README states GitHub public release is not completed yet.
- [x] README states profile pin is not applicable yet.
- [x] README points to the screenshot plan instead of claiming screenshots already exist.

## Screenshot Readiness

- [x] `docs/SCREENSHOTS_GUIDE.md` exists.
- [x] Screenshot plan covers Command Center, Project Starter, Workflow Packs, Checklist Manager, Project Status, Prompt Library, Delivery Report, and Export Center.
- [x] `screenshots/.gitkeep` exists as a placeholder.
- [ ] Actual screenshots have been captured.

## Manifest Readiness

- [x] `agent_manifest.json` parses as JSON.
- [x] `agent_manifest.json` keeps `hub_ready: true`.
- [x] `agent_manifest.json` keeps `modifies_agent_hub: false`.
- [x] `release/public_showcase_manifest.json` parses as JSON.
- [x] Release manifest keeps `github_public_release_completed: false`.
- [x] Release manifest keeps `agenthub_modified: false`.
- [x] Release manifest marks `screenshot_guide_ready: true`.
- [x] Release manifest marks `public_showcase_checklist_ready: true`.

## Validation Readiness

- [x] `python -m pytest -q` is part of the validation command set.
- [x] `python -m compileall .` is part of the validation command set.
- [x] `python release/public_release_check.py` is part of the WCC-003 release-prep validation set.
- [x] `python -c "import app; print('APP_IMPORT_OK')"` is part of the validation command set.

## Safety Readiness

- [x] No `.env` should be tracked.
- [x] No credential, token, secret, password, or api key filename should be tracked.
- [x] No `outputs/private` style path should be tracked.
- [x] WCC-003 does not read private content.
- [x] WCC-003 does not modify `F:\AIProjects\AgentHubControlCenter`.
- [x] WCC-003 does not configure a GitHub remote.
- [x] WCC-003 does not push.
- [x] WCC-003 does not profile pin.

## Ready For WCC-004?

WCC-003 can hand off to `WCC-004-GITHUB-PUBLIC-RELEASE` after:

- tests pass,
- compileall passes,
- public release check passes,
- app import check passes,
- git status is clean after commit,
- no remote is configured,
- no push has occurred,
- screenshots are captured or deliberately deferred with README language that does not claim they exist.
