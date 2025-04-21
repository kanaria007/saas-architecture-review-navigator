# Does Your API Design Prevent Breaking Changes?

> Type: Structure  
> Category: API  
> Audience: Engineers defining public interfaces, backend/FE integration contracts, or versioning policies

---

## 🧠 What This Perspective Covers

APIs aren’t functions—they’re **promises**.

And promises must not break.

- Field removals, enum expansions, nullability changes—small tweaks can ruin real systems  
- Compatibility is about trust: client code expects you to change carefully

---

## 🚨 Breaking Change Patterns

- Removing or renaming response fields without fallback  
- Changing default values or error structures  
- Expanding enums without guarding old clients  
- Using same endpoint name for incompatible behavior

---

## ✅ Better Compatibility Design

- Define schema evolution policy (additive, backward-safe)  
- Document “deprecated-but-present” as a lifecycle stage  
- Use explicit versioning in API path or header  
- Maintain changelog with client-visible impact annotations  
- Validate compatibility in CI using schema diffing

---

## ⚠️ Key Principle

Stability is not about freezing.  
It’s about **changing predictably**—and visibly.

---

## ❓ FAQ

- **Q: Can’t we just fix clients when something breaks?**  
  **A:** Not if the clients are mobile apps, third parties, or live dashboards.

- **Q: Should we version every change?**  
  **A:** No—but you should *track* every change.

---

## 🔗 Related Perspectives

- [Is the API Schema Coherent Across the System?](api-schema-coherence.md)
- [Is Your API Permission Design Explicit and Secure?](api-permission-control.md)
- [Is the Release Strategy Defined and Aligned With Change Impact?](../release/release-strategy-planning.md)
- [Is Component Reuse Helping or Hurting Your UI?](../ui/component-reuse-impact.md)
