# v23-codex-agent-env 执行目标

请作为 `codex` Agent 完成该真实测试任务。

## 目标

Codex 按 Agent 定义执行，并从任务包根目录 ENV 注入运行变量。

## 边界

- 运行时必须读取 ENV 注入的变量名，但不得输出变量值。
- 本用例不包含评审迭代要求。
- 不得修改 `spec.yaml`、`PROMPT.md`、`AGENTS.md`、`CLAUDE.md`。
- 交付结果必须通过 `spec.yaml` 中的验证命令。
