# v23-env-required-failure 产品需求

## 目标

本用例验证 spec-executor 在 `2.3` 任务包下的核心行为：ENV 声明为必需但文件缺失时，应产生 pre-JOB typed diagnostic，且不创建 JOB。

## 交付要求

| 项目 | 要求 |
| --- | --- |
| 任务包版本 | `2.3` |
| executor | `codex` |
| 覆盖特性 | FR-001, FR-010, FR-013 |

## 验收标准

任务执行完成后，交付物必须满足 `spec.yaml` 中定义的验证命令；涉及隐私或失败边界的用例必须产生可查询诊断，且默认输出不得包含 ENV 值。
