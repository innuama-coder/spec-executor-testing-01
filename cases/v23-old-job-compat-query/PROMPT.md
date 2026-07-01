# v23-old-job-compat-query 执行目标

请作为 `codex` Agent 完成该真实测试任务。

## 目标

2.3 查询输出面对旧 JOB 缺少 agent/env/review facts 时，应输出兼容诊断而非伪造数据。

## 边界

- 本用例不要求读取 ENV。
- 本用例不包含评审迭代要求。
- 不得修改 `spec.yaml`、`PROMPT.md`、`AGENTS.md`、`CLAUDE.md`。
- 交付结果必须通过 `spec.yaml` 中的验证命令。
