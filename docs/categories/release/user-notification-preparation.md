# Is User Notification Prepared Where Needed?

> Type: Structure  
> Category: Release  
> Audience: Product managers, designers, backend/frontend developers handling release or UX change

---

## 🧠 What This Perspective Covers

Not all changes are self-evident.  
Some require explanation. Others require trust.

Designing change delivery is as critical as designing the change itself.

---

## 🔔 Typical Scenarios

- UI or interaction pattern changes  
- API behavior that silently shifts (e.g., sort order, pagination)  
- Scheduled downtime or rollout impacting data visibility  
- Feature flags released per tenant or per user group

---

## 🚨 Failure Patterns

- Users are surprised by behavior shift (“it used to do this…”)  
- Docs not updated → support gets overloaded  
- Admin users unaware of configuration change impacts  
- Notification was added too late to coordinate translation/review

---

## ✅ Good Notification Planning

- Who needs to know? When? How early?  
- Embed messages into UI or release notes—not just email  
- If i18n needed, schedule translation before freeze  
- Ensure rollback path considers user state (e.g., partially migrated data)

---

## ⚠️ Principle

**Communication is a design dependency.**  
If left out, the system *will* behave unpredictably—for humans.

---

## ❓ FAQ

- **Q: Is this PM’s job?**  
  **A:** Yes—and also engineering’s responsibility to surface risk.

- **Q: Do we always notify?**  
  **A:** No. But when surprise is dangerous, silence is failure.

---

## 🔗 Related Perspectives

- [Is Downtime Minimized Where Unavoidable?](minimize-downtime.md)
- [Is Cross-Service Consistency Guaranteed—or Just Hoped For?](../async/cross-service-consistency.md)
- [What Happens When the External System Fails?](../async/external-failure-impact.md)
- [Is the Operational Flow Designed to Minimize Dev and Support Burden?](../non-functional/operational-burden.md)
