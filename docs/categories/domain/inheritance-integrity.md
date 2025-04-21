# Is Your Inheritance a Design Model—or Just a Field Merger?

> Type: Structure  
> Category: Domain  
> Audience: Anyone who thinks "extends" means "understands"

---

## 🤔 Why This Matters

Inheritance looks like reuse.  
But in systems, it’s often just **a silent entanglement.**

Used wrong, inheritance isn’t a structure—it’s a **trapdoor**.

---

## 🚨 Danger Signs

- A subclass exists, but adds no real behavior—just fields  
- Parent and child differ in validation rules  
- Removing the parent breaks half the unrelated services  
- You're not sure what the subtype *means*, just that it shares some columns

---

## ✅ Better Structures

- Use composition unless **the subtype behaves differently**  
- If two models share shape but not meaning, keep them separate  
- Make inheritance explicit at the behavior level (`execute()`, `isAllowed()`)  
- Document: “why does this extend that?”

---

## 🧠 Real Question

Does this inheritance reflect **shared semantics**—or just **data gravity**?

Are you modeling a reality, or **avoiding effort**?

---

## ❓ FAQ

- **Q: But the shape is the same. Isn’t reuse natural?**  
  **A:** The shape is irrelevant. The meaning isn’t.

- **Q: Should I always avoid inheritance?**  
  **A:** No. Just don’t use it because your ORM makes it easy.

---

## 🔗 Related Perspectives

- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](domain-permissions.md)
- [Is the Lifecycle of Your Data Clear—Or Just Assumed?](../data/lifecycle-clarity.md)
- [Can Your System Even Represent an Invalid State?](invalid-states.md)
- [Does Your API Design Prevent Breaking Changes?](../api/api-compatibility-strategy.md)
