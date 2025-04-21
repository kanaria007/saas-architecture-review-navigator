# Can Retried Events Introduce Inconsistent State?

> Type: DeepDive  
> Category: Data  
> Audience: Engineers working on async pipelines, retries, and eventual consistency

---

## 🚨 The Silent Disaster

Retries feel safe—until they aren’t.

- A retry re-applies the same state change → **duplicate mutation**
- A side effect (email, payment) gets triggered again → **user chaos**
- A compensating action runs twice → **data corruption**

---

## 🧠 The Real Question

When your event fires again—  
are you confident it won’t do something **wrong**?

Or are you just hoping the system “should handle it”?

---

## 🔍 Scenarios to Review

- Idempotency: enforced *where*? request layer? domain? DB?
- Event replays: do they mutate state again, or just confirm idempotence?
- Side effects: are they guarded by **delivery guarantees**, or just “probably won’t happen twice”?

---

## ✅ Safer Designs

- Use idempotency keys at system boundaries  
- Store event execution history to detect duplicates  
- Make side effects part of transactional outbox, not best-effort fire-and-forget  
- Prefer "confirm success" over "assume failure and retry"

---

## ❓ FAQ

- **Q: Aren’t retries necessary for reliability?**  
  **A:** Yes. But reliability without state integrity is just faster failure.

- **Q: What if retries *are* part of the domain logic?**  
  **A:** Then encode them explicitly. Don’t hide them behind infra.

---

## 🔗 Related Perspectives

- [Is Cross-Service Consistency Guaranteed—or Just Hoped For?](../async/cross-service-consistency.md)
- [Do You Have a Fallback Plan for Asynchronous Failures?](fallback-strategy.md)
- [Have You Deliberately Decided Whether You Need Distributed Transactions?](distributed-transaction-design.md)
- [Are Event Delays and Retries Part of Your Design—or Just Runtime Surprises?](../async/event-retry-delay.md)
