# spec-executor-testing-01 — hello-rust

spec-executor 2.0 测试用例：从零构建 Rust binary crate，`cargo run` 输出 `Hello, world!`。

## 目录

- `tasks/development/spec.yaml` — spec-executor 2.0 入口
- `tasks/development/CLAUDE.md` / `AGENTS.md` / `PROMPT.md` — 任务包
- `docs/DELIVERY.md` — 验收标准说明

## 运行

```
spec-executor run --spec tasks/development/spec.yaml --workspace ./workspace
```
