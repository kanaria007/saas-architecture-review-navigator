# SaaS Architecture Review Navigator

> Why this Navigator exists: [Read the Manifesto](../../manifesto.md)
>
> A structured, field-tested design perspective navigator  
> for SaaS architects, engineers, and reviewers.  
> **50+ perspectives / 12 + 1 categories / 2 structural levels** — all mapped and linked.

---

## 🧭 What Is This?

This navigator helps distributed system designers **avoid blind spots**  
by checking critical architecture perspectives across:

- Domain modeling  
- Data structure and consistency  
- API design and schema governance  
- Event-driven architecture  
- Performance and scalability  
- Authorization and security  
- Testing and release operations  
- Availability and failure handling  
- Operational/non-functional requirements

Each perspective is a focused, atomic `.md` file:

- 🔍 What this perspective asks or covers  
- ⚠️ Common failure patterns  
- ✅ Good practices and design strategies  
- 🧠 Design principles or mental models  
- ❓ Frequently asked questions  
- 🔗 Related perspectives

### 🧠 About the Human Category

The Human category deliberately goes beyond pure technical architecture.
It provides frameworks for:

- Structuring personal growth as an intentional system
- Building self-directed improvement loops
- Designing mentorship and leadership development pathways

Unlike other categories, these files do not strictly follow the "perspective checklist" format.
Instead, they serve as cognitive scaffolding—to accelerate the long-term, systemic growth of both individual engineers and engineering organizations.

---

## 🚀 How to Use

### 1. During Design Phase

Use the [Navigation Map](navigation-map.md) to explore critical perspectives.  
Start with relevant categories (domain, data, API, etc.) and review the questions before you write code.

### 2. While Reviewing Code or Specs

Point to relevant `.md` files directly in pull requests or review templates.  
They provide shared checklists to align authors and reviewers.

### 3. After Incidents or Failures

Check `availability/` or `non-functional/` for recovery, alerting, observability, and failover strategies.  
Use these perspectives in postmortems and RCA sessions.

---

## 📂 Categories

- 🧩 [`Common`](categories/common/design-justification.md) — design reasoning, tradeoff clarity  
- 🏷️ [`Domain`](categories/domain/domain-permissions.md) — abstraction, constraints, permissions  
- 📦 [`Data`](categories/data/lifecycle-clarity.md) — schema lifecycle, migration, indexing  
- 🌐 [`API`](categories/api/api-schema-coherence.md) — contract design, versioning, authz  
- 🔁 [`Event`](categories/async/sync-async-alignment.md) — async design, retries, fallout zones  
- 📊 [`Performance`](categories/performance/db-index-optimization.md) — latency, scale, resource limits  
- 🎨 [`UI`](categories/ui/component-reuse-impact.md) — rendering cost, notification design  
- 🧪 [`Test`](categories/test/impact-scope-analysis.md) — boundary tests, load, acceptance  
- 🚀 [`Release`](categories/release/release-strategy-planning.md) — rollout strategy, rollback design  
- 🔰 [`Availability`](categories/availability/failover-design.md) — failure response, backup, recovery  
- 🛡 [`Non-functional`](categories/non-functional/security-risks.md) — monitoring, security, ops  
- 🔐 [`Security`](categories/security/authn-authz-implementation.md) — authn/authz, sensitive data  
- 🧠 [`Human`](categories/human/growth-framework-design.md) — growth systems, reflection, mentorship

---

## 🧩 Structural Levels

- **Structure**: architectural separation, clarity, responsibility  
- **DeepDive**: failure handling, tradeoffs, operational edge cases

Use the sidebar or top navigation to explore perspectives by category or concept.

---

## 🧠 Design Philosophy

> This is not a tutorial.  
> It is a design navigator.  
> Built to help teams **ask better questions** before code is written.

Architecture is not only about structure.  
It is about **thinking in constraints, tradeoffs, and long-term system evolution**.

This project exists to help teams  
**ask sharper questions before committing to irreversible decisions.**

---

## 💬 Meta

- Created by [Kanaria](https://zenn.dev/kanaria007)  
- Originally authored in Japanese and carefully translated with AI assistance  
- Licensed under MIT  
- Contributions welcome (see [CONTRIBUTING.md](contributing.md))

> Note:  
> Category mappings differ slightly across languages by design.  
> For example, "Indexing Strategy" is treated under `data/` in English (schema lifecycle),  
> but under `performance/` in Japanese (query efficiency and runtime costs).  
> This reflects regional modeling emphasis and usage context.
