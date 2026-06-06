# AGENTS.md — hello-rust (codex executor)

> Loaded by spec-executor 2.0 when `executor: codex`. Copied to
> the worktree root during StartingExecutor. PROMPT.md is sent as
> the first user message via `send_input`.

## Task

Create a Rust binary crate from scratch. The repository has no Rust
code as baseline — produce `Cargo.toml` and `src/main.rs` such that
`cargo run` prints `Hello, world!` to standard output.

## Constraints

- Create `Cargo.toml` and `src/main.rs` at the repo root.
- Standard library only. No external dependencies.
- Do not modify `tasks/development/`, `docs/`, `spec.yaml`,
  `README.md`, `.gitignore`.
- No `rust-toolchain.toml`.
- The final `main` body should be `println!("Hello, world!")`.

## Self-Verification (mandatory)

```
cargo build
cargo run
```

## Definition of Done

1. `Cargo.toml` exists and defines a binary crate.
2. `src/main.rs` exists and prints `Hello, world!`.
3. `cargo run` prints `Hello, world!` and exits 0.
4. `tasks/development/` is byte-identical to the baseline.

## Out of Scope

- Refactoring, comments, tests, benchmarks, examples.
- Adding CI, README, or `LICENSE` files.
- Switching to library + integration-test layout.
