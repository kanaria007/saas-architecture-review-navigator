# Is Confidential Data Being Handled Safely—Not Just Accessed?

> Type: DeepDive  
> Category: Security  
> Audience: Engineers working on authentication, API design, database access, or log inspection

---

## 🧠 What This Perspective Covers

Security isn’t just about access.  
It’s about **impact** when access is misused or leaked.

What happens when:

- A log includes an email or token by mistake?  
- A screenshot reveals sensitive info in plaintext?  
- A debug export contains passwords?

---

## 🚨 Unsafe Handling Patterns

- Sensitive fields returned by default in APIs (e.g. name, email, phone)  
- Personally Identifiable Information (PII) stored in logs or metrics  
- Tokens, passwords, secrets shown in admin UIs or exports  
- Unencrypted fields in backup or async queues

---

## ✅ Safer Design Patterns

- Mark sensitive fields explicitly in the schema (e.g. `@sensitive`)  
- Strip or redact fields before logging, exporting, or serialization  
- Separate auth tokens and business data in responses  
- Encrypt at rest and in transit—not just one or the other  
- Test exports, debug dumps, and logs for sensitive fields before release

---

## ⚠️ Core Insight

Data doesn’t become sensitive at runtime.  
**It was always sensitive—you just didn’t label it.**

---

## ❓ FAQ

- **Q: Isn’t HTTPS enough?**  
  **A:** For transit, yes. But storage, logs, and exports are separate attack surfaces.

- **Q: Should we just encrypt everything?**  
  **A:** Not blindly. Encryption without lifecycle awareness still leaks.

---

## 🔗 Related Perspectives

- [ ] Data classification and tagging  
- [ ] PII-aware schema design  
- [ ] Observability with privacy in mind  
