# Is Write Contention Avoided—or Just Left to Luck?

> Type: Structure  
> Category: Data  
> Audience: Engineers who think locking is something the database just “handles”

---

## 🧠 The Problem Isn't Just Race Conditions

It’s what race conditions **do to your users**:

- Lost updates  
- Deadlocks under load  
- Feature toggles that “sometimes don’t work”  
- Exploding retry queues and invisible data corruption

---

## 🔍 Common Anti-Patterns

- No retry logic on writes  
- App logic assumes atomic multi-row updates  
- Transactions span multiple services or queues  
- Optimistic locking without conflict resolution  
- Global mutexes that serialize everything

---

## ✅ Better Strategies

- Use row-level locking where feasible  
- Keep transactions short and targeted  
- Use optimistic concurrency *with* user-aware conflict handling  
- Consider domain-level serialization (per document, per task) instead of global mutexes

---

## ⚖️ Core Design Tradeoff

You’re always trading off:

- Throughput  
- Isolation  
- User experience under failure

Designers who pretend otherwise are just borrowing time—from ops, and from users.

---

## ❓ FAQ

- **Q: Can’t we just “retry on error”?**  
  **A:** If you mean “retry the same mistake forever,” sure.

- **Q: Shouldn’t the DB handle all of this?**  
  **A:** Databases *enforce*. You *design*.

---

## 🔗 Related Perspectives

- [Is the API Schema Coherent Across the System?](../api/api-schema-coherence.md)
- [Are You Clear About When to Use Sync vs Async APIs?](../api/sync-vs-async-boundaries.md)
- [Are Event Delays and Retries Part of Your Design—or Just Runtime Surprises?](../async/event-retry-delay.md)
- [What Happens When the External System Fails?](../async/external-failure-impact.md)
