# SaaS Architecture Review Navigator

> A structured, field-tested design perspective navigator  
> for SaaS architects, engineers, and reviewers.  
> **50+ perspectives / 12 categories / 2 structural levels** — all mapped and linked.

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

- 🔍 Design risk it addresses  
- ✅ Good examples and practices  
- ⚠️ Typical failure patterns  
- ❓ Key FAQ  
- 🔗 Related perspectives

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

---

## 🧩 Structural Levels

- **Structure**: architectural separation, clarity, responsibility  
- **DeepDive**: failure handling, tradeoffs, operational edge cases

Use the sidebar or top navigation to explore perspectives by category or concept.

---

## 💬 Meta

- Created by [Kanaria](https://zenn.dev/kanaria007)  
- Authored in Japanese, translated to English via AI  
- Licensed under MIT  
- Contributions welcome (see [CONTRIBUTING.md](contributing.md))

---

## 🧠 Design Philosophy

> This is not a tutorial.  
> It is a design navigator.  
> Built to help teams **ask better questions** before code is written.
