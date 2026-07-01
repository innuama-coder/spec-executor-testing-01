# v23-env-required-failure 执行目标

请作为 `codex` Agent 完成该真实测试任务。

## 目标

ENV 声明为必需但文件缺失时，应产生 pre-JOB typed diagnostic，且不创建 JOB。

## 边界

- 本用例不要求读取 ENV。
- 本用例不包含评审迭代要求。
- 不得修改 `spec.yaml`、`PROMPT.md`、`AGENTS.md`、`CLAUDE.md`。
- 交付结果必须通过 `spec.yaml` 中的验证命令。
