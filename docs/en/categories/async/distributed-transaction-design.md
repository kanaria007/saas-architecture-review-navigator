---
title: Distributed Transaction Design
layer: [DeepDive]
category: async
tags: [transaction, coordination, boundary]
bloom_level: Analyze
license: MIT
---

# Have You Deliberately Decided Whether You Need Distributed Transactions?

> Type: DeepDive  
> Category: Async  
> Audience: Engineers dealing with microservices, cross-DB workflows, or async state

---

## 🔍 First, the Meta-Question

Distributed transactions aren’t always needed.  
But they **always need to be considered**.

If you skipped the question,  
you’ve made a decision—just not consciously.

- Will the system be OK if two updates succeed, and the third fails?  
- Is eventual consistency acceptable here?  
- Who detects and repairs drifted state?
- What’s the user experience in partial success cases?

---

## ⚠️ When It Goes Wrong

- Partial updates that look fine… until a user clicks “export”  
- Async retries that reapply incomplete state  
- Background jobs cleaning up state that was never finalized  
- System tests that don’t simulate failure modes

---

## ✅ Healthier Patterns

- **Explicit modeling of consistency boundaries**  
- Choose per-case: local txn / saga / outbox / retry-compensate  
- Store enough metadata to debug failure reconstruction  
- Document what it means for consistency to “eventually” happen

---

## 🧠 Core Philosophy

You’re not designing for “no failures.”  
You’re designing for **who pays the cost of failure—and when**.

---

## ❓ FAQ

- **Q: Isn’t this infra stuff?**  
  **A:** Only if your domain doesn’t care about truth.

- **Q: But we don’t need 2PC, right?**  
  **A:** Probably not. But have you designed around its absence?

---

## 🔗 Related Perspectives

- [Do You Have a Fallback Plan for Asynchronous Failures?](../async/fallback-strategy.md)
- [What Happens When the External System Fails?](../async/external-failure-impact.md)
- [Can Retried Events Introduce Inconsistent State?](../async/retry-consistency.md)
- [Is a Rollback Strategy in Place for Critical Changes?](../release/rollback-strategy.md)
