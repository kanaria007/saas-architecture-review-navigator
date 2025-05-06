---
title: Migration Impact and Risk
layer: [Structure]
category: data
tags: [migration, schema-evolution, compatibility]
bloom_level: Apply
license: MIT
---

# Is Schema Migration Treated as a Design Phase—or Just a Release Task?

> Type: Structure  
> Category: Data  
> Audience: Backend engineers who “just add a column real quick”

---

## 🔍 What’s Actually Being Asked

Not “will it work.”

But:

- Will it **silently break something**?
- Will it **disrupt downstream jobs**?
- Will it **leave inconsistent rows** if interrupted?

Schema change is not a git commit.  
It’s a multi-actor system event—with failure modes.

---

## ⚠️ What Goes Wrong

- Adding NOT NULL fields without defaults  
- Dropping columns used by legacy ETLs  
- Index rebuilds triggering downtime  
- Migrating while background jobs are still running  
- Test data masks the fact that prod is huge

---

## ✅ Healthy Migration Design Includes:

- Simulation on prod-size data  
- Clear rollback plan for partial state  
- Notifications for systems affected by schema contracts  
- Observability before, during, and after deploy  
- Deployment strategy that decouples schema from feature switches

---

## 🧠 Design Mindset

A migration is a **durable mutation of shared reality**.  
That’s not deployment. That’s surgery.

---

## ❓ FAQ

- **Q: It’s just a column. Why so serious?**  
  **A:** Because the column isn’t alone. It has integrations, assumptions, and costs.

- **Q: Isn’t this handled by ORM tools?**  
  **A:** ORMs write SQL. They don’t design consequences.

---

## 🔗 Related Perspectives

- [Is a Rollback Strategy in Place for Critical Changes?](../release/rollback-strategy.md)
- [Is Your Index Strategy Designed—Or Just Inherited?](indexing-strategy.md)
- [Is Cross-Service Consistency Guaranteed—or Just Hoped For?](../async/cross-service-consistency.md)
- [Is Your Index Designed—or Just Added After It Got Slow?](index-design.md)
