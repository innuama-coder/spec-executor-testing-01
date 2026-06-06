# Delivery Standard — hello-rust

## Expected Work

Create a Rust binary crate from scratch. The baseline has no Rust
code; every file in the crate is produced by the AI.

## Deliverable Files

| File | Condition | Verification |
|---|---|---|
| `Cargo.toml` | must exist | existence check |
| `src/main.rs` | must exist; prints `Hello, world!` | `cargo build && cargo run \| grep -Fxq "Hello, world!"` |

## Example Passing State

```
$ cargo run
Hello, world!
```

## Task Package Integrity

`tasks/development/` and `docs/` must remain byte-identical to the
baseline.
