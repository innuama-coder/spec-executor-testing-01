from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
SECRET = "SENTINEL_SECRET_VALUE"


REQUIRED_FILES = {
    "spec.yaml",
    "PROMPT.md",
    "AGENTS.md",
    "CLAUDE.md",
    "docs/PRD.md",
    "docs/HLD.md",
    "docs/LLD.md",
    "docs/DELIVERY.md",
}


V23_REQUIRED_MARKERS = [
    "version: \"2.3\"",
    "agent:",
    "context:",
    "verification:",
    "reporting:",
    "redact_env_values: true",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def case_dirs() -> list[Path]:
    if not CASES.exists():
        fail("cases directory is missing")
    return sorted(path for path in CASES.iterdir() if path.is_dir())


def validate_required_files(case: Path) -> None:
    missing = [name for name in REQUIRED_FILES if not (case / name).exists()]
    if missing:
        fail(f"{case.name} missing required files: {', '.join(missing)}")


def validate_v22(case: Path, spec: str) -> None:
    if 'version: "2.3"' in spec:
        fail(f"{case.name} is marked as compat but uses version 2.3")
    forbidden = ["agent:", "review:", "reporting:", "redact_env_values"]
    for marker in forbidden:
        if marker in spec:
            fail(f"{case.name} contains 2.3-only marker in compatibility spec: {marker}")


def validate_v23(case: Path, spec: str) -> None:
    for marker in V23_REQUIRED_MARKERS:
        if marker not in spec:
            fail(f"{case.name} missing v2.3 marker: {marker}")
    if re.search(r"files:\n(?:\s+- .*\n)*\s+- \"?ENV\"?", spec):
        fail(f"{case.name} includes ENV in agent context files")
    if not re.search(r"exclude:\n\s+- \"?ENV\"?", spec):
        fail(f"{case.name} does not explicitly exclude ENV from agent context")
    if "screen_capture_semantic_fallback: false" not in spec:
        fail(f"{case.name} does not disable screen capture semantic fallback")


def validate_env(case: Path, spec: str) -> None:
    requires_env = "required: true" in spec
    has_env = (case / "ENV").exists()
    if case.name == "v23-env-required-failure":
        if has_env:
            fail("v23-env-required-failure must intentionally omit ENV")
        return
    if requires_env and not has_env:
        fail(f"{case.name} requires ENV but ENV file is missing")
    if has_env:
        env_text = read(case / "ENV")
        if "=" not in env_text:
            fail(f"{case.name} ENV does not contain key=value entries")


def validate_privacy(case: Path) -> None:
    if case.name != "v23-env-privacy-sentinel":
        for path in case.rglob("*"):
            if path.is_file() and path.name != "ENV" and SECRET in read(path):
                fail(f"{case.name} leaks sentinel secret outside ENV: {path}")
        return
    env_path = case / "ENV"
    if SECRET not in read(env_path):
        fail("privacy sentinel case does not contain sentinel in ENV")
    for path in case.rglob("*"):
        if path.is_file() and path.name != "ENV" and SECRET in read(path):
            fail(f"privacy sentinel leaks secret outside ENV: {path}")


def validate_review(case: Path, spec: str) -> None:
    if case.name in {"v23-claude-agent-review", "v23-review-multi-round"}:
        if "items:" not in spec or "REV-001" not in spec:
            fail(f"{case.name} missing review items")
    if case.name == "v23-review-multi-round" and "REV-002" not in spec:
        fail("v23-review-multi-round missing second review item")


def main() -> None:
    dirs = case_dirs()
    if len(dirs) < 12:
        fail(f"expected at least 12 cases, got {len(dirs)}")

    compat = [case for case in dirs if case.name.startswith("compat-v22-")]
    v23 = [case for case in dirs if case.name.startswith("v23-")]
    if not (3 <= len(compat) <= 4):
        fail(f"expected 3-4 v2.2 compatibility cases, got {len(compat)}")
    if len(v23) < 8:
        fail(f"expected at least 8 v2.3 cases, got {len(v23)}")

    feature_markers = {
        "FR-004": False,
        "FR-005": False,
        "FR-006": False,
        "FR-007": False,
        "FR-012": False,
        "FR-013": False,
        "FR-014": False,
        "FR-015": False,
        "FR-016": False,
        "FR-017": False,
    }

    for case in dirs:
        validate_required_files(case)
        spec = read(case / "spec.yaml")
        if case in compat:
            validate_v22(case, spec)
            feature_markers["FR-012"] = True
        else:
            validate_v23(case, spec)
            validate_env(case, spec)
            validate_privacy(case)
            validate_review(case, spec)
            for marker in feature_markers:
                if marker in spec or marker in read(case / "docs/PRD.md"):
                    feature_markers[marker] = True

    missing_features = [marker for marker, covered in feature_markers.items() if not covered]
    if missing_features:
        fail(f"missing feature coverage markers: {', '.join(missing_features)}")

    print(f"[OK] {len(compat)} compatibility cases, {len(v23)} v2.3 cases validated")


if __name__ == "__main__":
    main()
