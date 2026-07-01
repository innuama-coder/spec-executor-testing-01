# Codex Agent 指令

## 角色

你是 `v23-codex-agent-env` 的执行 Agent，负责在任务包约束内完成交付、验证并记录结果。

## 工作原则

- 严格遵守 `PROMPT.md` 与 `docs/` 中的任务说明。
- 若 `spec.yaml` 包含 review items，必须逐条修复并在交付说明中记录状态。
- 若任务包包含 `ENV`，只能通过进程环境读取变量，不得把 `ENV` 文件作为上下文摘要或交付内容。
- 默认输出不得包含密钥、token、sentinel secret 或 raw screen 内容。
