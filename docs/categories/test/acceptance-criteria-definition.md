# Are the Acceptance Criteria Clearly Defined?

> Type: Structure  
> Category: Test  
> Audience: Engineers, PMs, QA, and reviewers defining test scope or validating feature completion

---

## 🧠 What This Perspective Covers

You can’t test what you can’t define.  
And what’s undefined becomes a source of conflict.

---

## 🚨 Common Mistakes

- No written criteria → “Did we finish?” becomes subjective  
- Dev and PM disagree on edge case expectations  
- Bug tickets without clear reproduction = untestable  
- “Acceptance” depends on mood, not milestone

---

## ✅ Healthier Criteria Design

- Write acceptance as checklist or decision table—not vague bullets  
- Clarify: What’s in scope? What’s *not*?  
- Document required inputs, preconditions, and boundary cases  
- Include user impact and business justification for each  
- Review with QA *before* implementation

---

## ⚠️ Key Principle

Testing without criteria isn’t testing.  
It’s just **opinion validation.**

---

## ❓ FAQ

- **Q: Should PMs write acceptance tests?**  
  **A:** No—but they must define what “done” means.

- **Q: Can tests evolve after release?**  
  **A:** Yes—but changing the criteria = changing the contract.

---

## 🔗 Related Perspectives

- [ ] Testable requirement writing  
- [ ] Contract-driven QA  
- [ ] Edge case coverage discussion  
