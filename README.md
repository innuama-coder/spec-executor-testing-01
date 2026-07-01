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
