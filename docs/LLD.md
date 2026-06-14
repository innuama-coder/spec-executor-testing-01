# LLD - hello-rust

## 文件设计

| 文件 | 设计要求 |
| --- | --- |
| `Cargo.toml` | 包名建议为 `hello-rust`，版本为 `0.1.0`，edition 使用稳定 Rust edition。 |
| `src/main.rs` | 只包含 `fn main()`，通过 `println!` 输出目标文本。 |

## 函数设计

```rust
fn main() {
    println!("Hello, world!");
}
```

## 验证设计

| 命令 | 预期 |
| --- | --- |
| `cargo build` | 编译成功。 |
| `cargo run` | 输出 `Hello, world!`。 |
