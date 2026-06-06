# CLAUDE.md — hello-rust (claude executor)

> Loaded by spec-executor 2.0. Copied from `tasks/development/CLAUDE.md`
> to the worktree root during StartingExecutor. PROMPT.md is sent
> as the first user message via `send_input`.

## Mission

Create a Rust binary crate from scratch. This repository has no Rust
code as baseline — you must produce `Cargo.toml` and `src/main.rs`
such that `cargo run` prints `Hello, world!` to standard output.

## Working Agreement

- **Create** `Cargo.toml` and `src/main.rs` at the repo root.
  The baseline has neither file.
- **Standard library only.** No external dependencies.
- **Do not modify** `tasks/development/`, `docs/`, `spec.yaml`,
  `README.md`, `.gitignore`, or any file not related to the crate
  you are creating.
- **No `rust-toolchain.toml`.** Build with the resolved stable
  toolchain.
- **A single `println!("Hello, world!")` in `main`** is the target.
  No extra prints, no `eprint!`, no command-line arguments.

## Self-Verification

Run both from the worktree root before declaring done:
```
cargo build
cargo run
```

`cargo run` must print exactly `Hello, world!` and exit 0.

## Definition of Done

1. `Cargo.toml` exists and defines a binary crate.
2. `src/main.rs` exists and prints `Hello, world!`.
3. `cargo run` prints `Hello, world!` and exits 0.
4. `tasks/development/` is byte-identical to the baseline
   (verified by the spec).

## Out of Scope

- Tests, documentation comments, refactoring.
- Adding a `rust-toolchain.toml`.
- Modifying any file outside the crate you create.
- `Cargo.lock` (it is in `.gitignore` by convention for binary
  crates).
