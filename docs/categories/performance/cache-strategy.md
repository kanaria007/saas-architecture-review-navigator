# Is Caching Helping—or Just Hiding Slowness?

> Type: DeepDive  
> Category: Performance  
> Audience: Engineers using cache layers, CDN, or performance tuning techniques

---

## 🧠 What This Perspective Covers

Caching is powerful.  
Which is why it’s dangerous.

- It can make performance look good—until it expires  
- It can mask structural inefficiencies in schema or query design  
- It can add fragility when staleness isn’t tolerable

---

## 🚨 Anti-Patterns

- Over-aggressive caching of incomplete or inconsistent data  
- No cache invalidation on updates → stale reads  
- Cache as the “real source of truth” in some endpoints  
- Deployment clears cache → first N users suffer  
- Caching what’s cheap, not what’s slow

---

## ✅ Better Cache Strategy

- Cache what’s *expensive* and stable—not just popular  
- Pair every cache with an invalidation trigger or TTL  
- Use “stale-while-revalidate” patterns where freshness is soft  
- Treat cache *misses* as observability events  
- Separate layers: CDN vs app cache vs local object memoization

---

## 🧠 Key Principle

Cache is not a fix.  
It’s a **bet**—that reads will outweigh writes, and that risk is acceptable.

---

## ❓ FAQ

- **Q: Should we cache everything “just in case”?**  
  **A:** That’s not safety. That’s entropy.

- **Q: Can cache be the primary data source?**  
  **A:** Only if you're also designing the failure modes.

---

## 🔗 Related Perspectives

- [Is Your Index Strategy Designed—Or Just Inherited?](../data/indexing-strategy.md)
- [Has the Need for Performance Testing Been Assessed?](../test/performance-test-plan.md)
- [Is Your Index Designed—or Just Added After It Got Slow?](../data/index-design.md)
- [Is Your Schema Over-Normalized—or Just Not Thinking About It?](../data/normalization-balance.md)
