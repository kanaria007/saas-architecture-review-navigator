# Is Your Schema Over-Normalized—or Just Not Thinking About It?

> Type: Structure  
> Category: Data  
> Audience: Engineers who haven't asked “what's the query cost of this join?”

---

## ⚖️ This Isn’t About Rules. It’s About Tradeoffs.

Normalization isn’t “correct.”  
Denormalization isn’t “fast.”

They’re both **tools**—and every tool leaves scars.

---

## 🚨 Common Failure Modes

- Over-normalized schema causes N+1 joins or multi-hop fetches  
- Denormalized tables drift out of sync  
- Analytics pipelines require rehydration of flattened data  
- Small updates touch many rows due to duplication

---

## ✅ Healthy Balance Looks Like:

- Normalize for source-of-truth and update frequency  
- Denormalize for read paths—**when latency matters more than purity**  
- Use materialized views or cache layers **with intentional ownership**  
- Keep the duplication cost visible—don’t hide it in helper functions

---

## 🧠 Key Design Framing

Every duplication is a **sync contract**.  
Every join is a **latency tax**.  
You choose your poison—but own the symptoms.

---

## ❓ FAQ

- **Q: Should we always denormalize for performance?**  
  **A:** No. But don’t pretend joins are free.

- **Q: What if we need both forms?**  
  **A:** Then define the boundary—and who owns keeping them in sync.

---

## 🔗 Related Perspectives

- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](../domain/domain-permissions.md)
- [Is Caching Helping—or Just Hiding Slowness?](../performance/cache-strategy.md)
- [Is Your Index Strategy Designed—Or Just Inherited?](indexing-strategy.md)
- [Is Your Index Designed—or Just Added After It Got Slow?](index-design.md)
