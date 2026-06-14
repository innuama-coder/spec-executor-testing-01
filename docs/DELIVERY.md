# DELIVERY - hello-rust

## 验收用途

本文档用于人工复核 `hello-rust` 任务是否完成。执行者无需修改本文档，但最终回复必须提供与本文档一致的验收证据。

## 交付物

| 交付物 | 验收要点 |
| --- | --- |
| `Cargo.toml` | 位于仓库根目录，声明 Rust binary crate。 |
| `src/main.rs` | 程序入口存在，并输出精确文本 `Hello, world!`。 |

## 验收命令

```bash
cargo build
cargo run
```

## 通过标准

- `cargo build` 退出码为 0。
- `cargo run` 输出为 `Hello, world!`，不得包含额外业务文本。
- `tasks/development/`、`docs/`、`README.md`、`.gitignore` 和 `spec.yaml` 未被修改。
