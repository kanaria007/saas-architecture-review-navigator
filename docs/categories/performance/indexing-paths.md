# Are Your Indexes Aligned with Query Paths?

> Type: DeepDive  
> Category: Performance  
> Audience: Engineers optimizing specific endpoints, heavy queries, or complex filters

---

## 🧠 What This Perspective Is Really About

Not all indexes are equal.  
And not all queries deserve them.

This perspective asks:

- Is this query actually **using** an index?
- Is the index **ordered correctly** for this filter + sort?
- Are your composite indexes aligned with query predicates?

---

## 🚨 Typical Pain Points

- N+1 joins on non-indexed foreign keys  
- Composite indexes where predicate order doesn’t match usage  
- Queries filtered on `LOW_CARDINALITY = ?` killing selectivity  
- Indexes built for legacy queries now unused  
- Missed use of `covering indexes` for heavy endpoints

---

## ✅ Good Index-to-Query Alignment

- Start from query logs / heatmaps → identify hot paths  
- Run `EXPLAIN` to verify index hits—not guess  
- Structure composite indexes to match most-selective predicates first  
- Consider filtered indexes when full coverage isn’t needed  
- Drop dead indexes proactively to reduce bloat and conflict

---

## 🧠 Core Principle

You’re not designing a schema.  
You’re designing **query execution under pressure**.

---

## ❓ FAQ

- **Q: Our queries seem fast. Is that enough?**  
  **A:** Until your dataset grows or cache misses spike.

- **Q: Can’t the DB just figure it out?**  
  **A:** It tries. But your structure limits its options.

---

## 🔗 Related Perspectives

- [Is Your Index Designed—or Just Added After It Got Slow?](../data/index-design.md)
- [Is Your Index Strategy Designed—Or Just Inherited?](../data/indexing-strategy.md)
- [Have You Designed Query Performance—or Just Hoped the DB “Handles It”?](db-index-optimization.md)
- [Is Your Scaling Strategy Designed—or Just Assumed?](scaling-strategy.md)
