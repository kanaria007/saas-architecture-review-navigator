# SaaS Architecture Review Navigator

> A structured, field-tested design perspective navigator  
> for SaaS architects, engineers, and reviewers.  
> **52 perspectives / 9 categories / 2 structural levels** — all mapped and linked.

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

- 🏷️ [`domain/`](./domain/) — abstraction, constraints, permissions
- 📦 [`data/`](./data/) — schema lifecycle, migration, indexing
- 🌐 [`api/`](./api/) — contract design, versioning, authz
- 🔁 [`event/`](./event/) — async design, retries, fallout zones
- 📊 [`performance/`](./performance/) — latency, scale, resource limits
- 🎨 [`ui/`](./ui/) — rendering cost, notification design
- 🧪 [`test/`](./test/) — boundary tests, load, acceptance
- 🚀 [`release/`](./release/) — rollout strategy, rollback design
- 🔰 [`availability/`](./availability/) — failure response, backup, recovery
- 🛡 [`non-functional/`](./non-functional/) — monitoring, security, ops

---

## 🧩 Structural Levels

- **Structure**: architectural separation, clarity, responsibility  
- **DeepDive**: failure handling, tradeoffs, operational edge cases

Use the sidebar or navigation to explore perspectives by category or concept.

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

