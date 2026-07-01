# compat-v22-hello-rust 产品需求

## 目标

本用例验证 spec-executor 在 `2.0` 任务包下的核心行为：保留原 hello-rust 任务包结构，验证旧版 deliverables 与 execution 字段兼容。

## 交付要求

| 项目 | 要求 |
| --- | --- |
| 任务包版本 | `2.0` |
| executor | `claude` |
| 覆盖特性 | FR-012 |

## 验收标准

任务执行完成后，交付物必须满足 `spec.yaml` 中定义的验证命令；涉及隐私或失败边界的用例必须产生可查询诊断，且默认输出不得包含 ENV 值。
