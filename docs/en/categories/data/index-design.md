# Is Your Index Designed—or Just Added After It Got Slow?

> Type: Structure  
> Category: Data  
> Audience: Engineers who added an index last week and forgot why

---

## 🔍 The Real Question

Is your index structure **proactively shaped by read intent**—or is it just a patch?

If your answer is “we’ll monitor and add indexes later,”  
you’re already behind.

---

## ⚠️ Common Index Design Failures

- Over-indexing → writes slow down, SSD cries  
- Under-indexing → filters applied in memory, not in scan  
- Wrong order → index exists but isn’t used  
- No compound index where one is needed  
- Index for one feature breaks another query

---

## ✅ Good Index Design Happens When…

- You start from **access patterns**, not just schema  
- Read paths are traced from UI → API → DB  
- You think in terms of “what question are we answering”  
- You challenge: “Do we need this query fast at all?”

---

## 🧠 Litmus Tests

- Can you name the top 3 queries this index serves?  
- Do you know which indexes are *hurting* insert/update performance?

---

## ❓ FAQ

- **Q: Isn’t this DB admin work?**  
  **A:** Only if your schema is read-only.

- **Q: Can’t we just rely on the query planner?**  
  **A:** The planner optimizes. It doesn’t prioritize.

---

## 🔗 Related Perspectives

- [Is Your Index Strategy Designed—Or Just Inherited?](indexing-strategy.md)
- [Are Your Indexes Aligned with Query Paths?](../performance/indexing-paths.md)
- [Have You Designed Query Performance—or Just Hoped the DB “Handles It”?](../performance/db-index-optimization.md)
- [Is Your Validation Actually Enforced—or Just Wished For?](../domain/domain-validation.md)
