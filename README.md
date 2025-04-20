# SaaS Architecture Review Navigator

> A structured, field-tested design perspective navigator for SaaS architects, developers, and reviewers  
> **52 perspectives / 9 categories / 2 structural levels** — fully mapped, English-translated, and production-aligned.

---

## 🧭 What Is This?

This repository is a **checklist + knowledge navigator** for SaaS architecture design.  
It helps teams avoid blind spots and ensure design quality by reviewing critical perspectives across:

- Domain design
- Data modeling
- API/schema/interface contracts
- Performance & scalability
- Event-driven & asynchronous systems
- Authorization & security
- Testing and release operations
- Availability and failure handling
- Non-functional/operational requirements

Each perspective is a Markdown file (e.g. `docs/categories/api/authz-strategy.md`) with:

- 🔍 Design risks and examples  
- ✅ Good practices and mitigation  
- ⚠️ Design principles  
- ❓ FAQs  
- 🔗 Related perspectives  

---

## 🗂 Category Overview

| Category | Description |
|----------|-------------|
| `domain` | Domain modeling, validation, permission logic |
| `data` | Schema structure, index, consistency, migrations |
| `api` | Interface design, versioning, security |
| `performance` | Latency, throughput, scaling, bottlenecks |
| `async` | Async design, retries, fallback patterns |
| `test` | Testing boundaries, load testing, acceptance |
| `release` | Rollout, rollback, impact control |
| `availability` | Failover, backup, recovery |
| `non-functional` | Logging, monitoring, security, operations |
| `ui` | UX/performance, component reuse, notifications |

---

## 📚 Structural Levels

| Level | Description | Who Should Read |
|-------|-------------|-----------------|
| `Structure` | Architectural clarity and separation of concerns | Junior-mid engineers, reviewers |
| `DeepDive` | High-complexity edge cases (failures, tradeoffs, ops) | Tech leads, SREs, architects |

---

## 🚀 How to Use

### 1. Design Phase
Use the category list to check for blind spots.  
Each `.md` file gives you examples, failure modes, and questions to answer in your spec.

### 2. Review Prep
Mark relevant perspectives in your pull request or spec template.  
Link to `.md` files as shared criteria for structured review.

### 3. Incident/Postmortem
Browse `availability/` or `non-functional/` to audit failure handling quality.

---

## 🧠 Design Axes & Perspective Guides

See `/docs/` for deeper cross-cutting guides across multiple perspectives:

- [Navigation Map (Full Index)](./docs/navigation-map.md)

---

## 📁 Repository Structure

```
docs/
  ├─ index-perspectives.md
  ├─ consistency-perspectives.md
  ├─ recovery-perspectives.md
  ├─ load-handling.md
  ├─ test-perspectives.md
  └─ navigation-map.md
  └─ /categories/
              ├─ domain/
              ├─ data/
              ├─ api/
              ├─ performance/
              ├─ async/
              ├─ test/
              ├─ release/
              ├─ availability/
              ├─ non-functional/
              └─ ui/
README.md
LICENSE
CONTRIBUTING.md
mkdocs.yml
```

---

## 🔓 License

All contents are released under the **MIT License**.  
Use, fork, share, or extend freely. Attribution is welcome.

---

## 🛠 Maintainers & Source

Created by [Kanaria (Zenn)](https://zenn.dev/kanaria007)  
Original articles and use cases:  
https://zenn.dev/kanaria007/articles/101e51dbcf2135

---

## 🧭 Want to Contribute?

See `CONTRIBUTING.md`.  
Pull requests for improvement, new perspectives, or formatting corrections are welcome.
