# Is the Release Strategy Defined and Aligned With Change Impact?

> Type: Structure  
> Category: Release  
> Audience: Tech leads, backend leads, SREs, and PMs planning production deployment

---

## 🧠 What This Perspective Covers

Release is not deployment.  
It is a negotiation with failure.

Even small changes can cause large damage if release strategy is not considered—  
especially under multi-tenant, distributed, or asynchronous conditions.

---

## ✅ Typical Use Cases

- Canary rollout to 5% tenants before global rollout  
- Feature toggle to decouple code merge from exposure  
- DB migration that is compatible across both old and new app versions  
- Stepwise exposure: staging → internal users → selected customers → all users

---

## 🔥 Common Failure Patterns

- All-or-nothing deploy with no rollback path  
- Feature exposure tied directly to deploy, no toggles or controls  
- DB schema changes without forward/backward compatibility  
- Downtime assumed as “unavoidable” due to monolithic migration  
- Release timing misaligned with business risk window (e.g. peak hours)

---

## 🛠 Better Release Strategy Design

- Classify the change: is it visible? breaking? reversible?  
- Design rollout method: toggle, staged, canary, delayed exposure  
- Include rollback mechanism *before* merge (infra and data both)  
- Define observability points: error surge? retry rate? latency spike?  
- Coordinate internally: who needs to know when and why

---

## 📘 FAQ

- **Q: Why not fix forward?**  
  **A:** That works only when blast radius is controlled and recovery is fast.

- **Q: Is staging enough?**  
  **A:** No. Only real traffic reveals integration cracks.

- **Q: Who owns release design?**  
  **A:** Every team must own it for what they ship.

---

## 🎯 Key Principle

Release ≠ Code Delivery  
**Release = Risk Framing + Controlled Exposure**

---

## 🔗 Related Perspectives

- [ ] High-load behavior test planning  
- [ ] Asynchronous system exposure strategy  
- [ ] Schema compatibility and zero-downtime rollout  
- [ ] Emergency rollback rehearsal
