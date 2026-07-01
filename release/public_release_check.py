"""Public showcase release checks for WorkflowCommandCenterAgent.

This script performs local checks only. It does not configure remotes, push,
publish, read secrets, or modify any external project.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SENSITIVE_PATTERNS = (
    ".env",
    "credentials",
    "token",
    "secret",
    "password",
    "api_key",
)
SCREENSHOTS = (
    "screenshots/01_command_center_home.png",
    "screenshots/02_project_starter_generator.png",
    "screenshots/03_workflow_packs.png",
    "screenshots/04_checklist_manager.png",
    "screenshots/05_project_status_tracker.png",
    "screenshots/06_prompt_rule_library.png",
    "screenshots/07_delivery_report_generator.png",
    "screenshots/08_export_center.png",
)
REQUIRED_FILES = (
    "README.md",
    "PROJECT_STATUS.md",
    "agent_manifest.json",
    "release/public_showcase_manifest.json",
    "docs/SCREENSHOTS_GUIDE.md",
    "docs/PUBLIC_SHOWCASE_CHECKLIST.md",
    "docs/WCC_003_GITHUB_SHOWCASE_PREP.md",
    "docs/WCC_004_GITHUB_PUBLIC_RELEASE.md",
)


def main() -> int:
    checks: list[tuple[str, str, str]] = []

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        checks.append(_result(path.exists(), "PASS", "FAIL", f"Required file exists: {relative_path}"))

    agent_manifest = _load_json(ROOT / "agent_manifest.json", checks)
    release_manifest = _load_json(ROOT / "release" / "public_showcase_manifest.json", checks)
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""

    for screenshot in SCREENSHOTS:
        path = ROOT / screenshot
        checks.append(_result(path.exists(), "PASS", "FAIL", f"Screenshot exists: {screenshot}"))
        checks.append(_result(_is_png(path), "PASS", "FAIL", f"Screenshot is PNG: {screenshot}"))
        checks.append(_result(screenshot in readme, "PASS", "FAIL", f"README references screenshot: {screenshot}"))

    if release_manifest:
        is_release_stage = release_manifest.get("release_stage") == "github-public-release"
        checks.append(
            _result(
                release_manifest.get("github_public_release_completed") is True if is_release_stage else release_manifest.get("github_public_release_completed") is False,
                "PASS",
                "FAIL",
                "Release completion flag matches release stage",
            )
        )
        checks.append(
            _result(
                release_manifest.get("agenthub_modified") is False,
                "PASS",
                "FAIL",
                "Release manifest marks AgentHubControlCenter as not modified",
            )
        )
        checks.append(
            _result(
                release_manifest.get("screenshots_ready") is True,
                "PASS",
                "FAIL",
                "Release manifest marks screenshots ready",
            )
        )
        checks.append(
            _result(
                release_manifest.get("screenshot_count") == len(SCREENSHOTS),
                "PASS",
                "FAIL",
                "Release manifest screenshot count is 8",
            )
        )
        checks.append(
            _result(
                release_manifest.get("public_showcase_checklist_ready") is True,
                "PASS",
                "FAIL",
                "Release manifest marks public showcase checklist ready",
            )
        )
        checks.append(
            _result(
                release_manifest.get("profile_pin_status") == "not_pinned",
                "PASS",
                "FAIL",
                "Release manifest marks profile pin as not_pinned",
            )
        )

    if agent_manifest:
        checks.append(
            _result(
                agent_manifest.get("modifies_agent_hub") is False,
                "PASS",
                "FAIL",
                "Agent manifest marks modifies_agent_hub as false",
            )
        )
        checks.append(
            _result(
                agent_manifest.get("hub_ready") is True,
                "PASS",
                "FAIL",
                "Agent manifest marks hub_ready as true",
            )
        )
        checks.append(
            _result(
                agent_manifest.get("github_showcase_ready") is True,
                "PASS",
                "FAIL",
                "Agent manifest marks github_showcase_ready as true",
            )
        )
        checks.append(
            _result(
                agent_manifest.get("profile_pin_status") == "not_pinned",
                "PASS",
                "FAIL",
                "Agent manifest marks profile pin as not_pinned",
            )
        )

    tracked_files = _git_ls_files()
    risky_files = [
        path
        for path in tracked_files
        if _is_sensitive_filename(path) or _is_private_output_path(path)
    ]
    checks.append(_result(not risky_files, "PASS", "FAIL", f"No risky tracked filenames: {risky_files or 'none'}"))

    remotes = _git_remote().strip()
    remote_detail = "configured" if remotes else "not configured yet"
    checks.append(("PASS", "Git remote state acceptable for current stage", remote_detail))

    fail_count = sum(1 for status, _, _ in checks if status == "FAIL")
    warning_count = sum(1 for status, _, _ in checks if status == "WARNING")

    for status, label, detail in checks:
        print(f"{status}: {label} - {detail}")

    summary_status = "PASS" if fail_count == 0 else "FAIL"
    print(f"SUMMARY: {summary_status} ({fail_count} fail(s), {warning_count} warning(s))")
    return 0 if fail_count == 0 else 1


def _load_json(path: Path, checks: list[tuple[str, str, str]]) -> dict[str, object] | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        checks.append(("FAIL", f"JSON file missing: {path.relative_to(ROOT)}", "not found"))
        return None
    except json.JSONDecodeError as exc:
        checks.append(("FAIL", f"JSON file parses: {path.relative_to(ROOT)}", str(exc)))
        return None

    checks.append(("PASS", f"JSON file parses: {path.relative_to(ROOT)}", "valid JSON"))
    return payload


def _git_ls_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def _git_remote() -> str:
    result = subprocess.run(
        ["git", "remote", "-v"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout if result.returncode == 0 else ""


def _is_png(path: Path) -> bool:
    if not path.exists() or not path.is_file():
        return False
    with path.open("rb") as handle:
        return handle.read(8) == b"\x89PNG\r\n\x1a\n"


def _is_sensitive_filename(path: str) -> bool:
    normalized = path.lower()
    name = Path(normalized).name
    return any(pattern in name for pattern in SENSITIVE_PATTERNS)


def _is_private_output_path(path: str) -> bool:
    normalized = path.lower()
    return normalized.startswith("outputs/") or "/outputs/private" in normalized or "outputs/private" in normalized


def _result(condition: bool, ok_status: str, bad_status: str, label: str) -> tuple[str, str, str]:
    status = ok_status if condition else bad_status
    detail = "ok" if condition else "needs attention"
    return status, label, detail


if __name__ == "__main__":
    raise SystemExit(main())
