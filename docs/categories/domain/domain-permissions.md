# Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?

> Type: Structure  
> Category: Domain  
> Audience: Engineers who think "access control" is an API thing

---

## 🚨 Why This Exists

Authorization is a business rule.  
If your domain model can’t answer “Can this user do this?”,  
then it’s not protecting the system—it’s outsourcing it.

---

## 🔍 Symptoms of a Missing Model

- UI hides actions, but API still allows them  
- Authorization checks scattered across controllers  
- `canEdit` logic duplicated across multiple services  
- No clear source of truth for permission rules

---

## ✅ What Good Looks Like

- Domain exposes behaviors like `document.canBeApprovedBy(user)`  
- Application layer enforces via `requirePermission(user, Action.EDIT_DOCUMENT)`  
- Permission structure is visible, testable, and tied to business intent  
- Authorization decisions are made early—not after the response is built

---

## 🧠 Design Principle

Permission is **not** about hiding buttons.  
It’s about controlling access to *business consequences*.

---

## ❓ FAQ

- **Q: Should permission live in the domain?**  
  **A:** If it’s about what’s allowed based on business context, yes.

- **Q: Isn’t that duplicated with app-layer guards?**  
  **A:** Not if they speak the same policy, in different layers.

---

## 🔗 Related Perspectives

- [ ] Responsibility split: domain vs application  
- [ ] Policy-based permission models  
- [ ] Deny-by-default philosophy  
