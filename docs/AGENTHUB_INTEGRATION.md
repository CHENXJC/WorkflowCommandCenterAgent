# AgentHub Integration Notes

## Portfolio Role

WorkflowCommandCenterAgent is the AI project execution command center in the portfolio matrix.

Its role is to help generate Codex-ready project instructions, reuse workflow packs, create execution checklists, track demo delivery status, maintain prompt/rule records, and export delivery reports.

Recommended AgentHub display:

- Display name: Workflow Command Center Agent
- Chinese name: AI 工作流指令中台
- Category: workflow-orchestration
- Subcategory: project-execution-command-center
- Status: agenthub-ready-local
- Current checkpoint: WCC-002-AGENTHUB-READINESS
- Next action: WCC-003-GITHUB-SHOWCASE-PREP

## Difference From AgentHubControlCenter

AgentHubControlCenter = portfolio visibility / agent registry.

WorkflowCommandCenterAgent = project execution / Codex instruction command center.

AgentHubControlCenter should eventually answer "what agents exist, what status are they in, and what should happen next?"

WorkflowCommandCenterAgent should answer "what exact instruction, workflow pack, checklist, or delivery report should I use to execute the next project step?"

These projects are complementary, but they should remain separate at WCC-002:

- AgentHubControlCenter is the portfolio-level control center.
- WorkflowCommandCenterAgent is the execution-template and project-command layer.
- WCC-002 prepares metadata for future visibility without changing the hub.

## Why WCC-002 Does Not Modify AgentHubControlCenter

WCC-002 is an AgentHub-readiness checkpoint, not an integration checkpoint.

The safe sequence is:

1. Stabilize WorkflowCommandCenterAgent's local metadata contract.
2. Document the future integration contract.
3. Validate the manifest and release status locally.
4. Only later decide whether AgentHubControlCenter should read this project.

This avoids mixing a new project's readiness work with changes to the existing hub repo.

## Future Integration Method

A future integration checkpoint can let AgentHubControlCenter read or mirror selected fields from:

- `agent_manifest.json`
- `release/public_showcase_manifest.json`
- `PROJECT_STATUS.md`

Recommended first integration mode:

- Manual registry entry using selected manifest fields.
- No private file scanning.
- No automatic cross-repo writes.
- No GitHub publishing assumptions.

Recommended later integration mode:

- A small manifest loader in AgentHubControlCenter.
- A registry row or virtual row for WorkflowCommandCenterAgent.
- A detail panel showing capabilities, validation status, and next action.

## AgentHub-Readable Fields

Fields AgentHubControlCenter can use later:

- `agent_name`
- `display_name`
- `chinese_name`
- `category`
- `subcategory`
- `role_in_portfolio`
- `current_checkpoint`
- `status`
- `lifecycle_stage`
- `hub_ready`
- `modifies_agent_hub`
- `launch_command`
- `local_path`
- `github_repo`
- `github_showcase_ready`
- `profile_pin_status`
- `demo_mode`
- `privacy_mode`
- `core_capabilities`
- `key_modules`
- `ui_tabs`
- `validation_commands`
- `last_validation`
- `integration_notes`
- `next_recommended_action`

## Future AgentHubControlCenter Files To Consider

Do not modify these files during WCC-002. They are listed only for a future explicit integration task.

Likely future files:

- `F:\AIProjects\AgentHubControlCenter\data\agent_registry.csv`
- `F:\AIProjects\AgentHubControlCenter\app.py`
- `F:\AIProjects\AgentHubControlCenter\agent_hub\registry_loader.py`
- `F:\AIProjects\AgentHubControlCenter\agent_hub\portfolio_matrix.py`
- `F:\AIProjects\AgentHubControlCenter\agent_hub\ui_helpers.py`
- `F:\AIProjects\AgentHubControlCenter\PROJECT_STATUS.md`
- `F:\AIProjects\AgentHubControlCenter\README.md`

## WCC-002 Boundary

WCC-002 completed only internal readiness work inside `F:\AIProjects\WorkflowCommandCenterAgent`.

It did not:

- Modify `F:\AIProjects\AgentHubControlCenter`
- Configure a GitHub remote
- Push to GitHub
- Complete a GitHub public release
- Mark profile pin status as ready
- Read private data or credentials
