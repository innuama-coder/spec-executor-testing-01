# spec-executor-testing-01 - hello-rust

Rust 入门开发型独立测试仓库。该仓库用于验证 spec-executor 是否能够驱动 Claude/Codex 在空仓库中创建 Rust binary crate，并完成最小可运行程序。

## 目录

- `docs/PRD.md`：产品需求。
- `docs/HLD.md`：高层设计。
- `docs/LLD.md`：详细设计。
- `docs/DELIVERY.md`：交付说明模板。
- `tasks/development/`：spec-executor task package。

## 运行

```bash
spec-executor run --spec tasks/development/spec.yaml --workspace ./workspace
```
