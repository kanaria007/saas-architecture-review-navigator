# Can Your System Even Represent an Invalid State?

> Type: Structure  
> Category: Domain  
> Audience: People who think enums solve everything

---

## 🚨 First Principle

If your system **can** represent something invalid,  
someone **will**.

---

## 🧠 What This Question Is Really About

This isn’t just “do you have validation.”  
It’s: **does your model forbid nonsense—or just quietly permit it?**

You don’t need more tests.  
You need fewer ways to go wrong.

---

## 🔍 Common Leaks

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

## ❓ FAQ

- **Q: Isn’t this over-design?**  
  **A:** No. It’s pre-accident design.

- **Q: Can’t I validate later?**  
  **A:** Sure—after someone’s already been harmed.

---

## 🔗 Related Perspectives

- [ ] State machine enforcement  
- [ ] Eliminating ambiguity in domain states  
- [ ] Invalid-by-construction prevention  
