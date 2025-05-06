# SaaS Architecture Review Navigator

> Why this Navigator exists: [Read the Manifesto](./manifesto.md)
>
> A structured, field-tested design perspective navigator for SaaS architects, developers, and reviewers
> Now with AI-guided structural reading protocols (Strict / Flexible) to enable hallucination-free `.md` document reasoning.
> **50+ perspectives / 12 + 1 categories / 2 structural levels** — fully mapped, English-translated, and production-aligned.

[![Docs](https://img.shields.io/badge/docs-online-green)](https://kanaria007.github.io/saas-architecture-review-navigator/)
[![GitHub stars](https://img.shields.io/github/stars/kanaria007/saas-architecture-review-navigator.svg)](https://github.com/kanaria007/saas-architecture-review-navigator/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue.svg)](https://github.com/kanaria007/saas-architecture-review-navigator/pulls)

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

In addition, the Human category offers cognitive frameworks for:

- Structuring sustainable personal and team growth
- Designing mentorship models
- Building self-directed learning architectures

(These guides do not strictly follow the technical checklist format; they support long-term capability development across engineering organizations.)

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
| `human` | Growth frameworks, self-reflection templates, mentorship architecture |

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

## 🧠 Navigator Philosophy

> This is not a tutorial. It is a navigator.  
> Designed to help teams **ask better questions** before they write code.

Each perspective file is intentionally minimal but powerful:

- 🔍 What it asks or reveals
- ⚠️ Common mistakes or fragilities
- ✅ Patterns and recommendations
- 🧠 Design principles
- ❓ FAQ
- 🔗 Links to other views

---

## 🌐 Docs Site & Navigation

Explore the live documentation site here:  
📘 [SaaS Review Navigator Site](https://kanaria007.github.io/saas-architecture-review-navigator/)

- [Navigation Map](./docs/en/navigation-map.md)
- [Structure vs DeepDive](./docs/en/structure-vs-deepdive.md)

---

## 📘 For AI tools and structured readers:

This project includes a grammar-based prompt protocol that teaches LLMs how to interpret layered `.md` files structurally.

Start with the high-level guide here:
> ✅ [Structured Reading Guide](./docs/ai-guidance/structured-reading.md)

For implementation, reuse, or adaptation, see:
> 📦 [Prompt Protocol Set (README)](./docs/ai-guidance/tools/README.md)

This protocol has been tested with GPT-4o across 100+ architectural documents,  
achieving >95% structural fidelity with no hallucinated summaries or invented file names.

---

## 🛠 Run Locally

```bash
pip install mkdocs-material mkdocs-awesome-pages-plugin mkdocs-git-revision-date-localized-plugin
mkdocs serve --config-file mkdocs.en.yml
```

---

## 🤝 Want to Contribute?

We're looking for:

- New perspectives from your experience
- FAQ and edge cases
- Translation or adaptation
- Clarification or fixes

AI assistance is welcome — if curated and aligned with the project’s structure and philosophy.

Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines and the [perspective template](./docs/en/perspective-template.md) to get started.

---

## 🧑‍💻 Language and Translation Note

This project was originally authored in Japanese, and translated and refined using AI tools (e.g., ChatGPT).  
If you spot awkward expressions or unclear phrasing, feel free to submit a PR or open an issue — your help is always welcome.

---

## 📁 Repository Structure

``` text
docs/
  ├─ ai-guidance/  # ai guidance
  └─ ja/           # Japanese content
  └─ en/           # English content
README.md
LICENSE
CONTRIBUTING.md
mkdocs.yml
```

---

## 🔓 License

All contents are released under the **MIT License**.  
Use, fork, share, or extend freely. Attribution is welcome.

### Reuse Notice

This project is MIT licensed, but its value lies in **how it is meant to be read and used**.

The documentation is structurally authored to support reasoning, reflection, and failure prevention.  
If reused or embedded, please retain this **structural reading grammar** to preserve its design integrity.

---

## 🛠 Maintainers & Source

Created by [kanaria007 (Zenn)](https://zenn.dev/kanaria007)  
Original articles and use cases:
https://zenn.dev/kanaria007/articles/101e51dbcf2135

### 📢 For Enterprise or Research Users

If you are evaluating this framework for integration into AI systems, educational platforms, or cognitive tools:

- Please be aware that **the structural reading protocol is part of the core value**.
- This is not a content dump, but a reasoning scaffold.
- If you plan to embed, adapt, or benchmark it, we encourage contacting the author or referencing the AI-guidance documentation to ensure correct application.

📬 Contact: canaria.island.kanaria007@gmail.com (for research, stewardship, or feedback)
