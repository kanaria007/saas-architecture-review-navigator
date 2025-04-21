# Is Notification Design Translation-Ready?

> Type: Structure  
> Category: UI  
> Audience: Engineers and designers building email, in-app, or system notifications

---

## 🧠 What This Perspective Covers

Notifications aren’t copywriting.  
They are **structured communication** with:

- Audience  
- Timing  
- Action intent  
- Multilingual risks

---

## 🚨 Typical Issues

- Hardcoded messages baked into backend or scripts  
- Business terms untranslated or ambiguous  
- HTML + plaintext emails generated differently  
- No preview/test for multilingual rendering

---

## ✅ Notification Design Principles

- Design notifications as message objects—not ad hoc strings  
- Separate content, logic, and delivery transport  
- Include locale, audience, and fallback strategy in message contract  
- Use keys and structured templates for translation compatibility  
- Enable staging/testing flows for QA to verify wording and rendering

---

## ⚠️ Principle

Message is a **product**—  
it must be versioned, tested, and owned.

---

## ❓ FAQ

- **Q: Can devs write notification text directly?**  
  **A:** Only if the team can preview and test it before sending.

- **Q: Is translation the PM’s job?**  
  **A:** Language is everyone’s responsibility once the product is global.

---

## 🔗 Related Perspectives

- [Is the API Schema Coherent Across the System?](../api/api-schema-coherence.md)
- [Are the Acceptance Criteria Clearly Defined?](../test/acceptance-criteria-definition.md)
- [Is the Impact Scope of This Change Clearly Understood?](../test/impact-scope-analysis.md)
- [Is User Notification Prepared Where Needed?](../release/user-notification-preparation.md)
