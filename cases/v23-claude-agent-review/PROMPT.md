# v23-claude-agent-review 执行目标

请作为 `claude` Agent 完成该真实测试任务。

## 目标

Claude 按 Agent 定义执行，并根据 spec.yaml 中 review items 完成同一 JOB 迭代。

## 边界

- 本用例不要求读取 ENV。
- 必须逐条回应 `spec.yaml` 中的 review items。
- 不得修改 `spec.yaml`、`PROMPT.md`、`AGENTS.md`、`CLAUDE.md`。
- 交付结果必须通过 `spec.yaml` 中的验证命令。
