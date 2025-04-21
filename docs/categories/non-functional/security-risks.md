# Are Security Risks Considered?  
> Type: Structure  
> Category: Non-functional  
> Audience: Security engineers, reviewers, backend/API owners

---

## 🧠 What This Perspective Covers

Security doesn’t come from good intentions.  
It comes from **explicit decisions about what’s protected, how, and by whom**.

This perspective checks whether **sensitive data, authentication, and authorization** are covered as active design concerns.

---

## 🔍 Typical Risk Vectors

- Personal information (PII) and financial data in logs or payloads  
- API endpoints lacking role-based or tenant-based access control  
- Weak session handling or token misuse  
- Inconsistent or unclear permission models between domains and UI  
- Secrets stored in code or misconfigured environment access

---

## 🚨 Failure Patterns

- "Hidden in UI" ≠ protected at API level  
- Sensitive fields exposed in logs or metrics  
- Permission logic duplicated and drifting in multiple services  
- JWTs or OAuth tokens not validated against revocation or scope  
- Security handled only at edge—not in application logic

---

## ✅ Smarter Security Design

- Map out sensitive data flow: where does it go, who can see it?  
- Define access control at multiple layers (domain, use-case, endpoint)  
- Use structured permission models: roles, scopes, policies  
- Log access to sensitive data with auditing intent  
- Treat secrets and credentials as infrastructure—not source code

---

## ⚠️ Principle

**Security is not a patch.  
It’s a set of enforced design boundaries.**

---

## ❓ FAQ

- **Q: Isn’t the frontend enough to hide sensitive fields?**  
  **A:** No. Anything rendered client-side must be protected server-side.

- **Q: Where should permissions live?**  
  **A:** Domain defines who can act. Use-case enforces it. Endpoint restricts access.

---

## 🔗 Related Perspectives

- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](../domain/domain-permissions.md)
- [Is Your API Permission Design Explicit and Secure?](../api/api-permission-control.md)
- [Does Your System Prevent Privilege Escalation?](../api/privilege-escalation-risk.md)
- [Is the Impact Scope of This Change Clearly Understood?](../test/impact-scope-analysis.md)
