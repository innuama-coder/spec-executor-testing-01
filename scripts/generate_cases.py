from __future__ import annotations

from pathlib import Path
import shutil
import textwrap


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
REPO_URL = "https://github.com/innuama-coder/spec-executor-testing-01.git"


CASE_MATRIX = [
    {
        "id": "compat-v22-hello-rust",
        "version": "2.0",
        "executor": "claude",
        "category": "2.2 compatibility",
        "focus": "保留原 hello-rust 任务包结构，验证旧版 deliverables 与 execution 字段兼容。",
        "features": ["FR-012"],
    },
    {
        "id": "compat-v22-docs-only",
        "version": "2.0",
        "executor": "claude",
        "category": "2.2 compatibility",
        "focus": "验证旧任务包可只交付文档类产物，不依赖 2.3 agent/review/ENV 字段。",
        "features": ["FR-012"],
    },
    {
        "id": "compat-v22-query-export",
        "version": "2.0",
        "executor": "codex",
        "category": "2.2 compatibility",
        "focus": "验证旧 JOB 的 query/export 读模型在 2.3 中不因新增 projection 失败。",
        "features": ["FR-012"],
    },
    {
        "id": "compat-v22-privacy-baseline",
        "version": "2.0",
        "executor": "claude",
        "category": "2.2 compatibility",
        "focus": "验证旧任务包中的普通上下文仍按原有规则处理，不引入 ENV 隐私语义。",
        "features": ["FR-012", "NFR-003"],
    },
    {
        "id": "v23-codex-agent-env",
        "version": "2.3",
        "executor": "codex",
        "category": "2.3 agent-env",
        "focus": "Codex 按 Agent 定义执行，并从任务包根目录 ENV 注入运行变量。",
        "features": ["FR-001", "FR-002", "FR-003", "FR-004", "FR-009", "FR-010"],
        "env": True,
    },
    {
        "id": "v23-claude-agent-review",
        "version": "2.3",
        "executor": "claude",
        "category": "2.3 review",
        "focus": "Claude 按 Agent 定义执行，并根据 spec.yaml 中 review items 完成同一 JOB 迭代。",
        "features": ["FR-001", "FR-002", "FR-003", "FR-006", "FR-007", "FR-011"],
        "review": True,
    },
    {
        "id": "v23-env-required-failure",
        "version": "2.3",
        "executor": "codex",
        "category": "2.3 env-failure",
        "focus": "ENV 声明为必需但文件缺失时，应产生 pre-JOB typed diagnostic，且不创建 JOB。",
        "features": ["FR-001", "FR-010", "FR-013"],
        "env_required_missing": True,
    },
    {
        "id": "v23-env-privacy-sentinel",
        "version": "2.3",
        "executor": "claude",
        "category": "2.3 env-privacy",
        "focus": "ENV 包含 sentinel secret，默认 query/report/export/log 不得泄漏变量值。",
        "features": ["FR-004", "FR-005", "NFR-001", "MET-004"],
        "env": True,
        "privacy": True,
    },
    {
        "id": "v23-review-multi-round",
        "version": "2.3",
        "executor": "codex",
        "category": "2.3 review",
        "focus": "多条评审意见驱动多轮迭代，验证 item 状态、轮次、投送和验证证据。",
        "features": ["FR-006", "FR-007", "MET-002", "MET-005"],
        "review": True,
        "multi_review": True,
    },
    {
        "id": "v23-old-job-compat-query",
        "version": "2.3",
        "executor": "codex",
        "category": "2.3 compatibility",
        "focus": "2.3 查询输出面对旧 JOB 缺少 agent/env/review facts 时，应输出兼容诊断而非伪造数据。",
        "features": ["FR-009", "FR-012", "NFR-003"],
        "compat_fixture": True,
    },
    {
        "id": "v23-resume-source-degraded",
        "version": "2.3",
        "executor": "claude",
        "category": "2.3 lifecycle",
        "focus": "覆盖 resume 证据链连续、Agent source degraded 和 OpenClaw bounded failure。",
        "features": ["FR-014", "FR-015", "NFR-006", "NFR-007", "MET-008"],
        "lifecycle": True,
    },
    {
        "id": "v23-capture-failure-handoff",
        "version": "2.3",
        "executor": "codex",
        "category": "2.3 lifecycle",
        "focus": "覆盖 screen capture 产品化、默认安全投影、JOB 内失败 handoff 与 cleanup visibility。",
        "features": ["FR-013", "FR-016", "FR-017", "MET-007", "MET-008"],
        "capture": True,
    },
]


def clean_cases() -> None:
    if CASES.exists():
        shutil.rmtree(CASES)
    CASES.mkdir(parents=True)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8", newline="\n")


def common_docs(case: dict) -> dict[str, str]:
    case_id = case["id"]
    return {
        "docs/PRD.md": f"""
            # {case_id} 产品需求

            ## 目标

            本用例验证 spec-executor 在 `{case["version"]}` 任务包下的核心行为：{case["focus"]}

            ## 交付要求

            | 项目 | 要求 |
            | --- | --- |
            | 任务包版本 | `{case["version"]}` |
            | executor | `{case["executor"]}` |
            | 覆盖特性 | {", ".join(case["features"])} |

            ## 验收标准

            任务执行完成后，交付物必须满足 `spec.yaml` 中定义的验证命令；涉及隐私或失败边界的用例必须产生可查询诊断，且默认输出不得包含 ENV 值。
        """,
        "docs/HLD.md": f"""
            # {case_id} 高层设计

            ## 架构约束

            本用例只依赖任务包内声明的输入。Agent 上下文通过 `PROMPT.md`、`AGENTS.md`、`CLAUDE.md` 与 `docs/` 文件表达；`ENV` 仅用于进程环境注入，不作为普通上下文文件提供给 Agent 阅读。

            ## 运行关系

            ```mermaid
            flowchart LR
              Spec["spec.yaml"] --> Agent["Agent 输入"]
              Env["ENV"] --> Tmux["tmux session"]
              Agent --> Exec["{case["executor"]}"]
              Tmux --> Exec
              Exec --> Verify["verification"]
              Verify --> Report["DELIVERY.md"]
            ```
        """,
        "docs/LLD.md": f"""
            # {case_id} 详细设计

            ## 文件合同

            | 文件 | 职责 |
            | --- | --- |
            | `spec.yaml` | 定义任务、Agent、验证、报告和 2.3 扩展字段。 |
            | `PROMPT.md` | 定义执行目标和边界。 |
            | `AGENTS.md` | Codex 指令入口。 |
            | `CLAUDE.md` | Claude 指令入口。 |
            | `docs/DELIVERY.md` | 任务交付说明。 |

            ## 约束

            任务实现不得修改任务包指令文件本身；验证命令应只检查交付结果和安全投影。
        """,
        "docs/DELIVERY.md": f"""
            # {case_id} 交付说明

            ## 交付状态

            本文件由 Agent 在执行任务时维护。最终内容应说明完成项、验证结果、已处理评审意见与人工接手建议。
        """,
    }


def prompt(case: dict) -> str:
    env_note = "运行时必须读取 ENV 注入的变量名，但不得输出变量值。" if case.get("env") or case.get("privacy") else "本用例不要求读取 ENV。"
    review_note = "必须逐条回应 `spec.yaml` 中的 review items。" if case.get("review") else "本用例不包含评审迭代要求。"
    return f"""
        # {case["id"]} 执行目标

        请作为 `{case["executor"]}` Agent 完成该真实测试任务。

        ## 目标

        {case["focus"]}

        ## 边界

        - {env_note}
        - {review_note}
        - 不得修改 `spec.yaml`、`PROMPT.md`、`AGENTS.md`、`CLAUDE.md`。
        - 交付结果必须通过 `spec.yaml` 中的验证命令。
    """


def agent_doc(case: dict, target: str) -> str:
    label = "Codex" if target == "AGENTS.md" else "Claude"
    return f"""
        # {label} Agent 指令

        ## 角色

        你是 `{case["id"]}` 的执行 Agent，负责在任务包约束内完成交付、验证并记录结果。

        ## 工作原则

        - 严格遵守 `PROMPT.md` 与 `docs/` 中的任务说明。
        - 若 `spec.yaml` 包含 review items，必须逐条修复并在交付说明中记录状态。
        - 若任务包包含 `ENV`，只能通过进程环境读取变量，不得把 `ENV` 文件作为上下文摘要或交付内容。
        - 默认输出不得包含密钥、token、sentinel secret 或 raw screen 内容。
    """


def compat_spec(case: dict) -> str:
    case_id = case["id"]
    task_dir = f"cases/{case_id}"
    output = f"artifacts/{case_id}.txt"
    return f"""
        version: "{case["version"]}"
        name: "{case_id}"
        repo:
          url: "{REPO_URL}"
          branch: "main"
        task_dir: "{task_dir}"
        executor: "{case["executor"]}"
        deliverables:
          - path: "{output}"
            verify: 'test -f {output}'
          - path: "{task_dir}/docs/DELIVERY.md"
            verify: 'test -f {task_dir}/docs/DELIVERY.md'
        execution:
          poll_interval_sec: 2
          idle_timeout_sec: 30
          max_duration_min: 5
          max_nudge_count: 3
          max_consecutive_escalate: 2
    """


def review_lines(case: dict) -> list[str]:
    if not case.get("review"):
        return ["    items: []"]
    lines = [
        "    items:",
        "      - id: \"REV-001\"",
        "        source: \"external-review\"",
        "        severity: \"must\"",
        "        target: \"docs/DELIVERY.md\"",
        "        description: \"交付说明必须明确说明已回应评审意见。\"",
        "        expected_fix: \"在 DELIVERY.md 中记录 REV-001 的处理结果。\"",
        "        evidence_refs:",
        "          - \"docs/PRD.md\"",
        "        acceptance:",
        "          command: \"grep -Fq 'REV-001' docs/DELIVERY.md\"",
    ]
    if case.get("multi_review"):
        lines.extend(
            [
                "      - id: \"REV-002\"",
                "        source: \"external-review\"",
                "        severity: \"should\"",
                "        target: \"docs/DELIVERY.md\"",
                "        description: \"交付说明需要包含验证命令的实际结果。\"",
                "        expected_fix: \"在 DELIVERY.md 中记录验证命令和通过状态。\"",
                "        evidence_refs:",
                "          - \"docs/PRD.md\"",
                "        acceptance:",
                "          command: \"grep -Fq '验证通过' docs/DELIVERY.md\"",
            ]
        )
    return lines


def v23_spec(case: dict) -> str:
    case_id = case["id"]
    task_dir = f"cases/{case_id}"
    artifact = f"artifacts/{case_id}.txt"
    env_required = "true" if case.get("env") or case.get("privacy") or case.get("env_required_missing") else "false"
    verification_commands = [f"test -f {artifact}", f"grep -Fq '{case_id}' {artifact}"]
    if case.get("privacy"):
        verification_commands.append("grep -Fq 'redact_env_values: true' cases/v23-env-privacy-sentinel/spec.yaml")
    if case.get("review"):
        verification_commands.append(f"grep -Fq 'REV-001' {task_dir}/docs/DELIVERY.md")
    if case.get("capture"):
        verification_commands.append(f"grep -Fq 'handoff' {task_dir}/docs/DELIVERY.md")
    context_extra: list[str] = []
    if case.get("compat_fixture"):
        context_extra.append("        - \"fixtures/legacy-job/current_progress.json\"")

    lines = [
        "version: \"2.3\"",
        f"name: \"{case_id}\"",
        "repo:",
        f"  url: \"{REPO_URL}\"",
        "  branch: \"main\"",
        f"task_dir: \"{task_dir}\"",
        f"executor: \"{case['executor']}\"",
        "execution:",
        "  poll_interval_sec: 2",
        "  idle_timeout_sec: 30",
        "  max_duration_min: 8",
        "  max_nudge_count: 3",
        "  max_consecutive_escalate: 2",
        "  env:",
        "    file: \"ENV\"",
        f"    required: {env_required}",
        "    privacy: \"redacted\"",
        "  agent:",
        f"    id: \"{case_id}-agent\"",
        f"    name: \"{case_id}-agent\"",
        f"    role: \"负责完成 {case_id} 真实任务包交付。\"",
        "    model:",
        "      preference: \"default\"",
        "    instructions:",
        "      - \"严格按任务包上下文完成任务。\"",
        "      - \"ENV 只作为进程环境变量使用，默认输出不得包含变量值。\"",
        "      - \"若存在 review items，必须在同一 JOB 内完成修复和验证。\"",
        "    context:",
        "      files:",
        "        - \"PROMPT.md\"",
        "        - \"AGENTS.md\"",
        "        - \"CLAUDE.md\"",
        "        - \"docs/PRD.md\"",
        "        - \"docs/HLD.md\"",
        "        - \"docs/LLD.md\"",
        "        - \"docs/DELIVERY.md\"",
        *context_extra,
        "      exclude:",
        "        - \"ENV\"",
        "    tools:",
        "      allow:",
        "        - \"shell\"",
        "        - \"apply_patch\"",
        "      deny:",
        "        - \"network\"",
        "    permissions:",
        "      filesystem: \"workspace-write\"",
        "      network: \"deny\"",
        "      approval: \"on-request\"",
        "  review:",
        "    max_iterations: 2",
        *review_lines(case),
        "  lifecycle:",
        "    resume:",
        "      require_same_job: true",
        "    monitoring:",
        "      busy_side_effect: \"observe_only\"",
        "      source_degraded_policy: \"bounded_failure\"",
        "      screen_capture_semantic_fallback: false",
        "    capture:",
        "      default_raw_output: false",
        f"      failure_evidence: {'true' if case.get('capture') else 'false'}",
        "verification:",
        "  pass_threshold: 1",
        "  commands:",
        *[f"    - \"{cmd}\"" for cmd in verification_commands],
        "reporting:",
        "  format: \"markdown\"",
        "  include_evidence_refs: true",
        "  redact_env_values: true",
        "  include_handoff: true",
        "deliverables:",
        f"  - path: \"{artifact}\"",
        f"    verify: 'test -f {artifact}'",
        f"  - path: \"{task_dir}/docs/DELIVERY.md\"",
        f"    verify: 'test -f {task_dir}/docs/DELIVERY.md'",
    ]
    return "\n".join(lines) + "\n"


def env_file(case: dict) -> str:
    if case.get("privacy"):
        return """
            SPEC_EXECUTOR_CASE_ID=v23-env-privacy-sentinel
            SPEC_EXECUTOR_SENTINEL_SECRET=SENTINEL_SECRET_VALUE
            SPEC_EXECUTOR_PUBLIC_MODE=redacted
        """
    return f"""
        SPEC_EXECUTOR_CASE_ID={case["id"]}
        SPEC_EXECUTOR_FEATURE_FLAG=agent-task-lifecycle
    """


def legacy_fixture() -> str:
    return """
        {
          "job_id": "legacy-v22-job-0001",
          "schema_version": "2.2",
          "owner": "spec-executor",
          "status": "completed",
          "agent": null,
          "env": null,
          "review": null,
          "diagnostics": [
            {
              "code": "compat_missing_v23_projection",
              "severity": "info",
              "message": "Legacy 2.2 JOB does not contain 2.3 agent/env/review facts."
            }
          ]
        }
    """


def write_case(case: dict) -> None:
    case_dir = CASES / case["id"]
    for rel, content in common_docs(case).items():
        write(case_dir / rel, content)
    write(case_dir / "PROMPT.md", prompt(case))
    write(case_dir / "AGENTS.md", agent_doc(case, "AGENTS.md"))
    write(case_dir / "CLAUDE.md", agent_doc(case, "CLAUDE.md"))
    if case["version"] == "2.3":
        write(case_dir / "spec.yaml", v23_spec(case))
        if case.get("env") or case.get("privacy"):
            write(case_dir / "ENV", env_file(case))
        if case.get("compat_fixture"):
            write(case_dir / "fixtures/legacy-job/current_progress.json", legacy_fixture())
    else:
        write(case_dir / "spec.yaml", compat_spec(case))


def write_readme() -> None:
    rows = [
        f"| `{case['id']}` | `{case['version']}` | `{case['executor']}` | {case['category']} | {case['focus']} | {', '.join(case['features'])} |"
        for case in CASE_MATRIX
    ]
    write(
        CASES / "README.md",
        "\n".join(
            [
                "# spec-executor 真实任务包用例集",
                "",
                "本目录用于验证 spec-executor 2.3.0 的 Agent Task Lifecycle 能力，并保留 4 个 2.2.x 兼容用例。用例均为可被 `spec-executor run` 直接消费的任务包。",
                "",
                "## 用例矩阵",
                "",
                "| 用例 | 版本 | executor | 分类 | 覆盖目标 | 需求覆盖 |",
                "| --- | --- | --- | --- | --- | --- |",
                *rows,
                "",
                "## 使用方式",
                "",
                "```bash",
                "spec-executor run --spec cases/v23-codex-agent-env/spec.yaml --workspace ./workspace",
                "```",
                "",
                "## 约束",
                "",
                "- `ENV` 文件只用于 tmux session 环境变量注入，不得作为 Agent 上下文文件读取。",
                "- 默认 query/report/export/log 不得输出 `ENV` 中的变量值。",
                "- review items 必须在同一 JOB 内形成迭代输入、修复证据和验证结果。",
                "- 2.2 兼容用例不得要求 2.3 专属字段存在。",
                "",
            ]
        ),
    )


def update_root_readme() -> None:
    write(
        ROOT / "README.md",
        """
        # spec-executor-testing-01

        该仓库是 spec-executor 的真实任务包测试仓库，用于验证 Claude/Codex 在真实 Git 仓库中执行任务包、交付产物、处理评审意见、注入运行环境变量并产生可验收结果。

        ## 用例目录

        | 路径 | 用途 |
        | --- | --- |
        | `tasks/development/` | 历史 hello-rust 单任务包，保留用于旧流程冒烟测试。 |
        | `cases/` | 2.2.x 兼容与 2.3.0 Agent Task Lifecycle 用例集。 |
        | `scripts/validate_cases.py` | 用例结构和覆盖矩阵校验脚本。 |

        ## 2.3.0 覆盖目标

        - Agent 任务包协议：executor、agent、context、tools、permissions、verification、reporting。
        - Claude/Codex 原生输入映射：`CLAUDE.md`、`AGENTS.md` 与任务包 Agent 定义。
        - `ENV` 注入：任务包根目录 `ENV` 注入 tmux session，不作为上下文文件。
        - 评审意见迭代：`spec.yaml` 中 review items 驱动同一 JOB 修复。
        - 生命周期硬化：resume、source degraded、monitoring side-effect、capture evidence、failure handoff。
        - 2.2.x 兼容：旧任务包和旧 JOB 查询导出行为不被 2.3 字段破坏。

        ## 运行

        ```bash
        python scripts/validate_cases.py
        spec-executor run --spec cases/v23-codex-agent-env/spec.yaml --workspace ./workspace
        ```
        """,
    )


def main() -> None:
    clean_cases()
    for case in CASE_MATRIX:
        write_case(case)
    write_readme()
    update_root_readme()


if __name__ == "__main__":
    main()
