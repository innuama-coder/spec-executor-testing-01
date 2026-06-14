# PRD - hello-rust

## 背景

spec-executor 需要保留一个最小 Rust 开发任务，用于验证执行器是否能够在空仓库中完成基础工程创建、代码实现、命令验证和最终汇报。

## 目标

创建一个 Rust binary crate，使 `cargo run` 输出精确文本 `Hello, world!`。

## 功能需求

| ID | 需求 |
| --- | --- |
| FR-001 | 在仓库根目录创建 `Cargo.toml` 和 `src/main.rs`。 |
| FR-002 | 程序启动后输出 `Hello, world!`，且不输出额外业务文本。 |
| FR-003 | 仅使用 Rust 标准库，不引入外部依赖。 |

## 约束

不得修改 `tasks/development/`、`docs/`、`README.md`、`.gitignore` 或 `spec.yaml`。

## 验收

`cargo build` 成功，且 `cargo run` 的输出包含精确文本 `Hello, world!`。
