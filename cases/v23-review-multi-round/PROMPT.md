# v23-review-multi-round 执行目标

请作为 `codex` Agent 完成该真实测试任务。

## 目标

多条评审意见驱动多轮迭代，验证 item 状态、轮次、投送和验证证据。

## 边界

- 本用例不要求读取 ENV。
- 必须逐条回应 `spec.yaml` 中的 review items。
- 不得修改 `spec.yaml`、`PROMPT.md`、`AGENTS.md`、`CLAUDE.md`。
- 交付结果必须通过 `spec.yaml` 中的验证命令。
