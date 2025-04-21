# Is the Operational Flow Designed to Minimize Dev and Support Burden?

> Type: Structure  
> Category: Non-functional  
> Audience: Developers, SREs, support leads, system architects

---

## 🔍 What This Perspective Covers

A well-designed system doesn’t just run—it **heals, explains, and supports itself**.

This perspective checks whether **day-to-day operations are streamlined** to avoid excessive burden on development and customer support teams.

---

## 🔍 Friction Points to Watch

- Ops steps require manual DB queries or admin panels  
- Logs and alerts are too sparse or noisy for triage  
- Support needs engineering help for every user question  
- Recovery or retry requires full developer intervention  
- Feature flags or config changes require redeploys

---

## ⚠️ Failure Patterns

- “Ask the dev” becomes standard ops process  
- No self-serve tools for CS or QA teams  
- Observability exists but doesn’t explain user-facing issues  
- On-call fatigue due to repetitive low-impact alerts  
- Config drift due to manual toggle or DB edits

---

## ✅ Smarter Ops Flow Design

- Document what ops must do, not just how code works  
- Design admin/ops interfaces for non-engineers  
- Include observability for intent, not just error  
- Automate recovery where safe: retries, restores, rollbacks  
- Separate config from deploy: use remote toggles or control panels

---

## 🧠 Principle

**You’re not done designing  
until the system supports itself.**

---

## ❓ FAQ

- **Q: Isn’t some ops always manual?**  
  **A:** Yes. But repeatable actions should be automated or self-served.

- **Q: Who owns operational UX?**  
  **A:** The same team that owns the feature. Ownership includes usability—for humans.

---

## 🔗 Related Perspectives

- [Are Monitoring Targets Well-Defined and Alerts Properly Configured?](observability-alerting.md)
- [Is the Logging Strategy Sufficient for Troubleshooting?](logging-for-troubleshooting.md)
- [Are Recovery Steps Clearly Defined for Incidents?](recovery-runbook.md)
- [Is User Notification Prepared Where Needed?](../release/user-notification-preparation.md)
