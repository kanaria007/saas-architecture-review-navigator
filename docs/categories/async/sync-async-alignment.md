# Is the Sync/Async Split Intentional—or Just Incidental?

> Type: Structure  
> Category: Async  
> Audience: Engineers deciding API boundaries, workflow orchestration, or event-driven transitions

---

## 🧠 What This Design Perspective Really Asks

Not “is it async?”  
But:

- Is async the **right model** for this business moment?  
- Does async create **ambiguity** in user expectations or system contracts?

---

## 🚨 Poorly Aligned Sync/Async Patterns

- Long-running sync API → user waits → timeout → duplicate retries  
- Async job triggers UI update, but UX doesn't reflect delay  
- Side effects (emails, downstream updates) happen *outside* the transaction  
- Inconsistent status handling → “did it succeed or not?”

---

## ✅ Better Alignment Practices

- Sync: only when user needs **immediate confirmation** or result  
- Async: when work is **delegated**, **deterministic**, and **retriable**  
- Return status handles that reflect “in progress” vs “done”  
- Surface async state visibly to users—not just in logs  
- Timeouts and retries with idempotency guards

---

## ⚠️ Principle

Async ≠ later.  
Async = **a different kind of contract**—one you must make explicit.

---

## ❓ FAQ

- **Q: Can't we just go async to improve perf?**  
  **A:** Yes—if you also redesign user expectations.

- **Q: Should async jobs always notify completion?**  
  **A:** If the user or system needs to act on the result, yes.

---

## 🔗 Related Perspectives

- [ ] UX-aware async design  
- [ ] Async result reconciliation  
- [ ] Transactional boundaries in event workflows  
