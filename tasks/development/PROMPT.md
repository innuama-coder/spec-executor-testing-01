# PROMPT.md — hello-rust (universal first instruction)

> Sent as the first user message to whichever executor is launched,
> via `send_input`.

---

Begin the **hello-rust** task.

This repository has no Rust code. Create a binary crate from scratch
at the repo root such that `cargo run` prints `Hello, world!`.

Read your working agreement: `CLAUDE.md` (claude) or `AGENTS.md` (codex)
at the worktree root.

Steps:
1. Create `Cargo.toml` and `src/main.rs`.
2. Write `main` to print `Hello, world!`.
3. Run `cargo build` and `cargo run`.
4. Confirm `Hello, world!` appears, then stop. The verifier handles
   the mechanical checks afterward.

Constraints (full list in your agreement file):
- Standard library only. No external dependencies.
- Do not touch `tasks/development/`, `docs/`, `spec.yaml`,
  `README.md`, `.gitignore`.
- Do not add a `rust-toolchain.toml`.
