# Is the Domain Separated from the Application Layer—and Does It Mean Anything?

> Type: Structure  
> Category: Domain  
> Audience: Engineers pretending they’re writing “business logic”

---

## 📌 What’s Actually Being Asked Here

You’ve drawn a clean architecture diagram. Cool.  
Now answer this:

- Can the domain say **“no”** to the application?
- Can it reject invalid state transitions?
- Or is it just holding data and praying someone else checks it?

---

## 🧠 What Proper Separation Actually Enables

- Your business rules live **in the domain**, not scattered across services or controllers  
- Application orchestration becomes thin—and safer  
- Test coverage hits behavior, not just I/O mocks  
- You can change the app layer without corrupting the model

---

## 🚨 Patterns That Pretend to Be Separation (But Aren’t)

- Dumb domain models: `{ User(name: String, isAdmin: Boolean) }` → That’s a DTO wearing a mustache  
- Application layer calling `domain.validate()` → Then ignoring the result  
- Behavior checks in service classes → AKA: “just one more if-statement” until entropy takes over

---

## 🔍 Litmus Tests

- Can you create an invalid object via constructor or factory?  
  → If yes, your domain is a data bag, not a rulekeeper.  
- Is state transition explicit (`start()`, `cancel()`, `expire()`)?  
  → Or is it `status = 3` and vibes?

---

## ❓ FAQ

- **Q: But isn’t that too much logic in the domain?**  
  **A:** It’s only “too much” if you confuse “rules” with “routing.”

- **Q: Shouldn’t use cases control all flows?**  
  **A:** They should orchestrate. But orchestration ≠ judgment.

---

## 🔗 Related Perspectives

- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](domain-permissions.md)
- [Is Your Validation Actually Enforced—or Just Wished For?](domain-validation.md)
- [Can Your System Even Represent an Invalid State?](invalid-states.md)
- [Is the API Schema Coherent Across the System?](../api/api-schema-coherence.md)
