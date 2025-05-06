---
title: Sync vs Async Boundary Design
layer: [Structure, DeepDive]
category: async
tags: [latency, retries, coupling]
bloom_level: Evaluate
license: MIT
---

# Are You Clear About When to Use Sync vs Async APIs?

> Type: Structure, DeepDive  
> Category: API  
> Audience: Engineers defining API contracts, frontend/backend flows, or task orchestration

---

## 🔍 What This Perspective Covers

The problem isn't just how to implement async.  
It's **where** to draw the line—and **why**.

---

## ⚠️ Common Confusions

- Sync endpoints that take 5+ seconds → client timeouts  
- Async endpoints with no status feedback → user uncertainty  
- APIs trigger long workflows but respond instantly without confirming outcome  
- Event queues treated as invisible black boxes

---

## ✅ Clearer Boundaries

- Sync APIs: when **immediate feedback or result** is required  
- Async APIs: for **delegated**, **long-running**, or **retry-prone** actions  
- Always offer a follow-up API to check async job status  
- Make contract-level expectations clear (e.g. SLAs, response time, finality)  
- Document side effects and propagation timelines for async calls

---

## 🧠 Core Insight

The difference isn’t latency.  
It’s **contract shape and system responsibility**.

---

## ❓ FAQ

- **Q: Can we just make everything async?**  
  **A:** Only if you design for it: status, feedback, and monitoring included.

- **Q: Should we let clients poll for results?**  
  **A:** Yes, but offer smart strategies: callbacks, webhooks, push if needed.

---

## 🔗 Related Perspectives

- [Is the Sync/Async Split Intentional—or Just Incidental?](../async/sync-async-alignment.md)
- [Is the API Schema Coherent Across the System?](api-schema-coherence.md)
- [Are Event Delays and Retries Part of Your Design—or Just Runtime Surprises?](../async/event-retry-delay.md)
- [Is Write Contention Avoided—or Just Left to Luck?](../data/write-contention.md)
