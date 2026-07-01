# v23-resume-source-degraded 产品需求

## 目标

本用例验证 spec-executor 在 `2.3` 任务包下的核心行为：覆盖 resume 证据链连续、Agent source degraded 和 OpenClaw bounded failure。

## 交付要求

| 项目 | 要求 |
| --- | --- |
| 任务包版本 | `2.3` |
| executor | `claude` |
| 覆盖特性 | FR-014, FR-015, NFR-006, NFR-007, MET-008 |

## 验收标准

任务执行完成后，交付物必须满足 `spec.yaml` 中定义的验证命令；涉及隐私或失败边界的用例必须产生可查询诊断，且默认输出不得包含 ENV 值。
