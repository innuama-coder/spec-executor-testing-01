# compat-v22-privacy-baseline 执行目标

请作为 `claude` Agent 完成该真实测试任务。

## 目标

验证旧任务包中的普通上下文仍按原有规则处理，不引入 ENV 隐私语义。

## 边界

- 本用例不要求读取 ENV。
- 本用例不包含评审迭代要求。
- 不得修改 `spec.yaml`、`PROMPT.md`、`AGENTS.md`、`CLAUDE.md`。
- 交付结果必须通过 `spec.yaml` 中的验证命令。
