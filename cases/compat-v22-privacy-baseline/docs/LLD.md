# compat-v22-privacy-baseline 详细设计

## 文件合同

| 文件 | 职责 |
| --- | --- |
| `spec.yaml` | 定义任务、Agent、验证、报告和 2.3 扩展字段。 |
| `PROMPT.md` | 定义执行目标和边界。 |
| `AGENTS.md` | Codex 指令入口。 |
| `CLAUDE.md` | Claude 指令入口。 |
| `docs/DELIVERY.md` | 任务交付说明。 |

## 约束

任务实现不得修改任务包指令文件本身；验证命令应只检查交付结果和安全投影。
