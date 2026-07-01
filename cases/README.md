# spec-executor 真实任务包用例集

本目录用于验证 spec-executor 2.3.0 的 Agent Task Lifecycle 能力，并保留 4 个 2.2.x 兼容用例。用例均为可被 `spec-executor run` 直接消费的任务包。

## 用例矩阵

| 用例 | 版本 | executor | 分类 | 覆盖目标 | 需求覆盖 |
| --- | --- | --- | --- | --- | --- |
| `compat-v22-hello-rust` | `2.0` | `claude` | 2.2 compatibility | 保留原 hello-rust 任务包结构，验证旧版 deliverables 与 execution 字段兼容。 | FR-012 |
| `compat-v22-docs-only` | `2.0` | `claude` | 2.2 compatibility | 验证旧任务包可只交付文档类产物，不依赖 2.3 agent/review/ENV 字段。 | FR-012 |
| `compat-v22-query-export` | `2.0` | `codex` | 2.2 compatibility | 验证旧 JOB 的 query/export 读模型在 2.3 中不因新增 projection 失败。 | FR-012 |
| `compat-v22-privacy-baseline` | `2.0` | `claude` | 2.2 compatibility | 验证旧任务包中的普通上下文仍按原有规则处理，不引入 ENV 隐私语义。 | FR-012, NFR-003 |
| `v23-codex-agent-env` | `2.3` | `codex` | 2.3 agent-env | Codex 按 Agent 定义执行，并从任务包根目录 ENV 注入运行变量。 | FR-001, FR-002, FR-003, FR-004, FR-009, FR-010 |
| `v23-claude-agent-review` | `2.3` | `claude` | 2.3 review | Claude 按 Agent 定义执行，并根据 spec.yaml 中 review items 完成同一 JOB 迭代。 | FR-001, FR-002, FR-003, FR-006, FR-007, FR-011 |
| `v23-env-required-failure` | `2.3` | `codex` | 2.3 env-failure | ENV 声明为必需但文件缺失时，应产生 pre-JOB typed diagnostic，且不创建 JOB。 | FR-001, FR-010, FR-013 |
| `v23-env-privacy-sentinel` | `2.3` | `claude` | 2.3 env-privacy | ENV 包含 sentinel secret，默认 query/report/export/log 不得泄漏变量值。 | FR-004, FR-005, NFR-001, MET-004 |
| `v23-review-multi-round` | `2.3` | `codex` | 2.3 review | 多条评审意见驱动多轮迭代，验证 item 状态、轮次、投送和验证证据。 | FR-006, FR-007, MET-002, MET-005 |
| `v23-old-job-compat-query` | `2.3` | `codex` | 2.3 compatibility | 2.3 查询输出面对旧 JOB 缺少 agent/env/review facts 时，应输出兼容诊断而非伪造数据。 | FR-009, FR-012, NFR-003 |
| `v23-resume-source-degraded` | `2.3` | `claude` | 2.3 lifecycle | 覆盖 resume 证据链连续、Agent source degraded 和 OpenClaw bounded failure。 | FR-014, FR-015, NFR-006, NFR-007, MET-008 |
| `v23-capture-failure-handoff` | `2.3` | `codex` | 2.3 lifecycle | 覆盖 screen capture 产品化、默认安全投影、JOB 内失败 handoff 与 cleanup visibility。 | FR-013, FR-016, FR-017, MET-007, MET-008 |

## 使用方式

```bash
spec-executor run --spec cases/v23-codex-agent-env/spec.yaml --workspace ./workspace
```

## 约束

- `ENV` 文件只用于 tmux session 环境变量注入，不得作为 Agent 上下文文件读取。
- 默认 query/report/export/log 不得输出 `ENV` 中的变量值。
- review items 必须在同一 JOB 内形成迭代输入、修复证据和验证结果。
- 2.2 兼容用例不得要求 2.3 专属字段存在。
