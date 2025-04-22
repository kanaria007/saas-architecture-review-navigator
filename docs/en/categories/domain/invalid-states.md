# Can Your System Even Represent an Invalid State?

> Type: Structure  
> Category: Domain  
> Audience: People who think enums solve everything

---

## 🔍 First Principle

If your system **can** represent something invalid,  
someone **will**.

---

## ⚠️ Common Leaks

- `User(status: Int)` with `7` as a possible value  
- `Task(state: String)` that can be `"completed"` and `"in-progress"` simultaneously  
- `Nullable<Boolean>` → Why is your system unsure if something is true or false?

---

## ✅ Structural Fixes

- Use enums, sealed types, and tagged unions with intent  
- Constructors should be unable to produce an invalid object  
- Optional? Only when **meaningful absence** is part of the domain  
- A domain model that “accepts everything” is just a list of hazards

---

## 🧠 What This Question Is Really About

This isn’t just “do you have validation.”  
It’s: **does your model forbid nonsense—or just quietly permit it?**

You don’t need more tests.  
You need fewer ways to go wrong.

---

## ❓ FAQ

- **Q: Isn’t this over-design?**  
  **A:** No. It’s pre-accident design.

- **Q: Can’t I validate later?**  
  **A:** Sure—after someone’s already been harmed.

---

## 🔗 Related Perspectives

- [Is Your Validation Actually Enforced—or Just Wished For?](domain-validation.md)
- [Is the Domain Separated from the Application Layer—and Does It Mean Anything?](domain-separation.md)
- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](domain-permissions.md)
- [Is the Lifecycle of Your Data Clear—Or Just Assumed?](../data/lifecycle-clarity.md)
