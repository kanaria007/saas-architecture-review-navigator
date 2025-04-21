# Is the Lifecycle of Your Data Clear—Or Just Assumed?

> Type: Structure  
> Category: Data  
> Audience: Anyone designing entities that "just exist" forever

---

## 🔍 The Core Question

Can you answer this about every major entity in your system?

- When is it created?
- How is it updated?
- When is it deleted?
- And what *shouldn’t* happen?

If you can’t, neither can your code—or your teammates.

---

## ⚠️ Why This Matters

- Unclear lifecycle leads to zombie data and haunted features  
- Soft delete vs hard delete becomes political  
- Business rules get reimplemented inconsistently  
- Schema evolves, but meaning decays

---

## ✅ Good Practices

- Use domain language like `archive()`, `deprecate()`, `revive()`—not just `is_active = false`  
- Keep deleted or historical data access **intentional**  
- Make edge states (e.g., expired, orphaned, abandoned) **modelable and testable**  
- Document life events as part of the entity spec—not just as code behavior

---

## 🧠 Litmus Tests

- Does anyone know when it's safe to delete this object?  
- Can the UI reflect its lifecycle state clearly and meaningfully?

---

## ❓ FAQ

- **Q: Can’t we just soft-delete and filter by default?**  
  **A:** That’s not a lifecycle. That’s a filter with memory loss.

- **Q: Who owns lifecycle decisions—product or backend?**  
  **A:** Both. One owns intent. The other enforces it.

---

## 🔗 Related Perspectives

- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](../domain/domain-permissions.md)
- [Can Your System Even Represent an Invalid State?](../domain/invalid-states.md)
- [Is Your Validation Actually Enforced—or Just Wished For?](../domain/domain-validation.md)
- [Is Your Index Strategy Designed—Or Just Inherited?](indexing-strategy.md)
