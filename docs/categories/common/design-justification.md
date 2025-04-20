# Do You Know Why This Design Exists?

> Type: Structure  
> Category: Common  
> Audience: Reviewer / Lead Architect / Any Engineer Who Has Ever Said “It Works, I Guess”

---

## 🧭 This Isn’t About Best Practices

Every system is a graveyard of decisions.  
What worked once may break tomorrow—and what breaks may never be blamed on the real cause.

This isn’t a checklist item.  
It’s a survival instinct.

---

## 🔍 What We’re Really Asking

- Why this approach, and not the others?  
- What trade-offs did you **consciously accept**?  
- If someone replaces this tomorrow, will they know what not to break?

---

## 🧠 Patterns That Save You Later

- You wrote: “This design minimizes write amplification at the cost of occasional staleness.”  
  → That one sentence just saved someone 3 days of debugging.
- You noted the alternative: “We didn’t go with Option B due to memory constraints in multi-tenant scaling.”  
  → That tells ops, PM, and future-you something valuable.

---

## 🧨 When It’s Missing

- Design becomes cargo culted. No one knows why it exists, so no one knows when it can die.  
- Reviewers can’t give meaningful feedback. There’s no context to push against.  
- The system survives—but its reasons rot away.

---

## ❓ FAQ

- **Q: Isn’t this just documentation?**  
  **A:** No. Documentation explains *what*. This explains *why*. Different species.

- **Q: Can’t people figure it out from code?**  
  **A:** Not when they’re stressed. Or new. Or not you.

---

## 🪧 Related Perspectives

- [ ] Trade-off visibility  
- [ ] Architecture decision records (ADR)  
- [ ] Review hygiene and design clarity

