# Does Your System Prevent Privilege Escalation?

> Type: DeepDive  
> Category: API  
> Audience: Security architects, API reviewers, backend engineers in multi-tenant SaaS

---

## 🧠 What This Perspective Covers

Not all security breaches are intrusions.  
Some are misdesigns—where the system lets users access more than they should.

---

## 🚨 Common Escalation Paths

- “Readonly” roles can perform side effects through indirect APIs  
- Shared tenants leak access when tenant IDs aren't strictly checked  
- Admin-only endpoints get exposed via misconfigured gateways  
- Logic flaws confuse “ownership” with “visibility”

---

## ✅ Safer Authorization Design

- Use explicit permission checks at entrypoint—not deep inside logic  
- Validate resource ownership for every operation—not just access  
- Treat tenant boundaries as isolation contracts, not just filters  
- Audit for privilege elevation paths (e.g. role-switch, token leakage)  
- Test for “silent escalation” via combination of API calls

---

## ⚠️ Key Insight

Privilege escalation doesn’t feel like a bug.  
Which is why it **must be tested as a feature**.

---

## ❓ FAQ

- **Q: Can’t we rely on role-based checks alone?**  
  **A:** Not if actions depend on data ownership or context.

- **Q: Should every access path be tested manually?**  
  **A:** Automate for known paths. Red-team for the unknown ones.

---

## 🔗 Related Perspectives

- [Is Your API Permission Design Explicit and Secure?](api-permission-control.md)
- [Are Security Risks Considered?](../non-functional/security-risks.md)
- [Is the Impact Scope of This Change Clearly Understood?](../test/impact-scope-analysis.md)
- [Is Your Auth Implementation Predictable, Testable, and Isolated?](../security/authn-authz-implementation.md)
