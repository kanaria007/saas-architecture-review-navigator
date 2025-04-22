# What Happens When the External System Fails?

> Type: Structure  
> Category: Async  
> Audience: Engineers integrating with third-party systems, APIs, or partner platforms

---

## 🔍 What This Perspective Asks

- What *exactly* happens if an external system goes down?
- Is the failure **detected**, **logged**, and **degraded gracefully**?
- Who gets hurt—and how much?

---

## ⚠️ Common Failures

- Partner API goes down → internal queues fill silently  
- Retry storms → overload own systems  
- UX degrades (empty dashboards, broken buttons) with no user messaging  
- Errors silently swallowed because “async = eventually”

---

## ✅ Better Failure Handling

- Explicit fallbacks or UI states when partner APIs fail  
- Timeout and retry policies per integration—not global  
- Queue isolation for high-risk dependencies  
- Alert on external system latency/spike—not just failure  
- Document UX impact and expected behavior per integration

---

## 🧠 Core Principle

Async doesn’t mean **ignore the failure**.  
It means **control how the failure manifests.**

---

## ❓ FAQ

- **Q: We have retries. Isn’t that enough?**  
  **A:** Not if the user or system can’t tell what happened.

- **Q: Should we surface all integration failures?**  
  **A:** No. But you should choose *who* needs to know *what*—and when.

---

## 🔗 Related Perspectives

- [Can You Handle External Load Spikes Gracefully?](../performance/external-pressure-resilience.md)
- [Do You Have a Fallback Plan for Asynchronous Failures?](../data/fallback-strategy.md)
- [Is the Sync/Async Split Intentional—or Just Incidental?](sync-async-alignment.md)
- [Have You Deliberately Decided Whether You Need Distributed Transactions?](../data/distributed-transaction-design.md)
