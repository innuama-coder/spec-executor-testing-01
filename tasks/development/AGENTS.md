# AGENTS.md - hello-rust

## 工作协议

你正在执行 `spec-executor-testing-01` 的 Rust 入门开发任务。请读取 `docs/PRD.md`、`docs/HLD.md` 和 `docs/LLD.md` 后再实现。

## 任务目标

创建最小 Rust binary crate，使 `cargo run` 输出 `Hello, world!`。

## 约束

- 不引入外部依赖。
- 不新增 `rust-toolchain.toml`。
- 不修改任务包和工作文档。

## 完成标准

`cargo build` 通过，`cargo run` 输出符合 PRD。
