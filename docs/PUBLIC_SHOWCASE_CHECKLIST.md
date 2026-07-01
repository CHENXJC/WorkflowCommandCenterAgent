# Public Showcase Checklist

This checklist records WorkflowCommandCenterAgent's GitHub public showcase release state for WCC-004.

## README Readiness

- [x] README explains the project positioning.
- [x] README explains why this is not a simple prompt library.
- [x] README lists core capabilities.
- [x] README includes local run commands.
- [x] README explains demo data and local-first safety.
- [x] README states GitHub public release is completed.
- [x] README states profile pin is not applicable yet.
- [x] README points to the screenshot plan instead of claiming screenshots already exist.

## Screenshot Readiness

- [x] `docs/SCREENSHOTS_GUIDE.md` exists.
- [x] Screenshot plan covers Command Center, Project Starter, Workflow Packs, Checklist Manager, Project Status, Prompt Library, Delivery Report, and Export Center.
- [x] Actual screenshots have been captured.
- [x] README references all 8 screenshots.

## Manifest Readiness

- [x] `agent_manifest.json` parses as JSON.
- [x] `agent_manifest.json` keeps `hub_ready: true`.
- [x] `agent_manifest.json` keeps `modifies_agent_hub: false`.
- [x] `release/public_showcase_manifest.json` parses as JSON.
- [x] Release manifest keeps `github_public_release_completed: true`.
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
- [x] WCC-004 configures GitHub remote for the target public repo.
- [x] WCC-004 pushes to `origin/main`.
- [x] WCC-004 does not profile pin.

## WCC-004 Completion Gate

WCC-004 can be marked complete after:

- tests pass,
- compileall passes,
- public release check passes,
- app import check passes,
- git status is clean after commit,
- remote is configured to `https://github.com/CHENXJC/WorkflowCommandCenterAgent`,
- push has landed on `origin/main`,
- README page is accessible,
- all 8 screenshot raw URLs are accessible,
- Profile Pin remains not completed.
