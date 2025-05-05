---
title: Cross-Service Consistency
layer: [Structure, DeepDive]
category: async
tags: [consistency, eventual, orchestration]
bloom_level: Analyze
license: MIT
---

# Is Cross-Service Consistency Guaranteed—or Just Hoped For?

> Type: Structure, DeepDive
> Category: Async  
> Audience: Engineers working on service integration, microservice orchestration, or eventual consistency design

---

## 🔍 What This Perspective Covers

When one service updates state—  
how do you ensure the others agree?

- Event published ≠ event received  
- Downstream updates might arrive late, or not at all  
- State might “look” right, but be structurally divergent

---

## ⚠️ Failure Scenarios

- Event loss: system A updates, B never sees the change  
- Out-of-order delivery → B overwrites A’s latest data  
- Conflict resolution policies undefined → inconsistent recovery  
- No alerting for downstream update drift

---

## ✅ Design for Real Consistency

- Use event versioning and schema contracts  
- Track causal links: what triggered what?  
- Implement reconciliation jobs for long-term consistency  
- Prefer eventual over “pretend real-time” sync  
- Monitor consistency lag across services—not just delivery

---

## ⚠️ Key Shift

Don’t assume the system is consistent.  
**Design it to notice when it isn’t.**

---

## ❓ FAQ

- **Q: But we use event delivery guarantees. Isn’t that enough?**  
  **A:** Guarantees cover delivery, not correctness.

- **Q: Can’t we just trust retries?**  
  **A:** Not without idempotence and visibility.

---

## 🔗 Related Perspectives

- [Can Retried Events Introduce Inconsistent State?](../async/retry-consistency.md)
- [Is the Sync/Async Split Intentional—or Just Incidental?](sync-async-alignment.md)
- [Is the API Schema Coherent Across the System?](../api/api-schema-coherence.md)
- [Are Event Delays and Retries Part of Your Design—or Just Runtime Surprises?](event-retry-delay.md)
