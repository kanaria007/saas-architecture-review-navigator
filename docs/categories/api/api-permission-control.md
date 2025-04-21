# Is Your API Permission Design Explicit and Secure?

> Type: Structure  
> Category: API  
> Audience: Engineers handling multi-tenant auth, RBAC, or endpoint security

---

## 🧠 What This Perspective Covers

APIs are often wide open—not because of malice,  
but because permission logic is missing, scattered, or implied.

- Security = access control + clarity  
- Especially in B2B SaaS, per-role API behavior must be intentional

---

## 🚨 Risk Patterns

- UI hides buttons, but API accepts all requests  
- Permission logic split across UI, controller, domain  
- No test coverage for unauthorized access  
- No centralized definition of who can do what

---

## ✅ Stronger API Permission Design

- Use domain-layer methods like `Document.canView(user)` to encapsulate business rules  
- At use-case or controller layer, assert permission explicitly at the start  
- Define role → permission → action mappings (e.g. in enums or policies)  
- Avoid "soft-deny": reject unauthorized access early and loudly  
- Audit all permission decisions in logs

---

## ⚠️ Principle

You can’t debug what you never defined.  
**Permission must be part of the architecture—not just the UI.**

---

## ❓ FAQ

- **Q: Can’t we just trust the frontend to hide restricted actions?**  
  **A:** Never. The client can lie.

- **Q: What if permission rules keep changing?**  
  **A:** Use policy-based access patterns to isolate volatility.

---

## 🔗 Related Perspectives

- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](../domain/domain-permissions.md)
- [Are Security Risks Considered?](../non-functional/security-risks.md)
- [Does Your System Prevent Privilege Escalation?](privilege-escalation-risk.md)
- [Is Your Auth Implementation Predictable, Testable, and Isolated?](../security/authn-authz-implementation.md)
