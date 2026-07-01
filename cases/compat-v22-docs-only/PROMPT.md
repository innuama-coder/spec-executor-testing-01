# compat-v22-docs-only 执行目标

请作为 `claude` Agent 完成该真实测试任务。

## 目标

验证旧任务包可只交付文档类产物，不依赖 2.3 agent/review/ENV 字段。

## 边界

- 本用例不要求读取 ENV。
- 本用例不包含评审迭代要求。
- 不得修改 `spec.yaml`、`PROMPT.md`、`AGENTS.md`、`CLAUDE.md`。
- 交付结果必须通过 `spec.yaml` 中的验证命令。
