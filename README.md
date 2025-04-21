# SaaS Architecture Review Navigator

> A structured, field-tested design perspective navigator for SaaS architects, developers, and reviewers  
> **50+ perspectives / 12 categories / 2 structural levels** — fully mapped, English-translated, and production-aligned.

---

## 🧭 What Is This?

This repository is a **checklist + knowledge navigator** for SaaS architecture design.  
It helps teams avoid blind spots and ensure design quality by reviewing critical perspectives across:

- Domain modeling and validation  
- Data structure, indexing, lifecycle, and consistency  
- API design, schema evolution, and compatibility  
- Event-driven and asynchronous workflows  
- Performance and scalability  
- UI rendering and communication logic  
- Release operations and rollback planning  
- Availability, failover, and data recovery  
- Testing boundaries and load behavior  
- Security, authentication, and sensitive data protection  
- Logging, observability, and operational resilience  
- Common design justification and rationale

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
| `data` | Schema lifecycle, indexing, consistency, migration |
| `api` | Contract design, versioning, authorization strategy |
| `performance` | Latency, indexing, caching, scalability |
| `async` | Retry behavior, fallout impact, causal issues |
| `release` | Rollouts, rollback, downtime, impact boundaries |
| `test` | Acceptance criteria, stress testing, scope checks |
| `availability` | Failover, data recovery, backup plans |
| `non-functional` | Logging, monitoring, recovery workflows |
| `ui` | Display limits, translation, component reuse |
| `security` | Authentication, authorization, sensitive data protection |
| `common` | Cross-cutting design rationale, justification |

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
  ├─ index.md
  ├─ contributing.md
  ├─ navigation-map.md
  ├─ structure-vs-deepdive.md
  └─ /categories/
              ├─ common/
              ├─ domain/
              ├─ data/
              ├─ api/
              ├─ event/
              ├─ performance/
              ├─ ui/
              ├─ test/
              ├─ release/
              ├─ availability/
              ├─ non-functional/
              └─ security/
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

Created by [kanaria007 (Zenn)](https://zenn.dev/kanaria007)  
Original articles and use cases:  
https://zenn.dev/kanaria007/articles/101e51dbcf2135

---

## 🧭 Want to Contribute?

See `CONTRIBUTING.md`.  
Pull requests for improvement, new perspectives, or formatting corrections are welcome.
