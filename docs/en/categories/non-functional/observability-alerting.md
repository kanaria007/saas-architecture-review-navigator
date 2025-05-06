---
title: Observability and Alerting
layer: [Structure, DeepDive]
category: non-functional
tags: [monitoring, alerting, observability]
bloom_level: Analyze
license: MIT
---

# Are Monitoring Targets Well-Defined and Alerts Properly Configured?

> Type: Structure, DeepDive  
> Category: Non-functional  
> Audience: SREs, platform engineers, backend leads, reliability owners

---

## 🔍 What This Perspective Covers

If a system fails silently, it fails completely.

This perspective checks whether your monitoring targets are **explicitly defined**, aligned with business risk, and wired to **clear, actionable alerting.**

Monitoring Must-Haves

- Request rate, error rate, latency (RED metrics)  
- Resource saturation: CPU, memory, DB pool, disk  
- External API health and SLA tracking  
- Queue depth and job retries  
- User-visible behavior: blank screens, login failures, broken workflows

---

## ⚠️ Failure Patterns

- Infra is monitored, but application issues go undetected  
- No distinction between “warning” and “urgent” alerts  
- Notification fatigue: too many noisy or flapping alerts  
- Alerts lack context: responder unsure what triggered it  
- Monitored metrics not tied to service-level indicators (SLIs)

---

## ✅ Smarter Observability Strategy

- Define what “bad looks like” in metrics and logs  
- Align alerts to user pain, not just system status  
- Include actionable info: what’s broken, who’s impacted, where to look  
- Review alert history to eliminate dead weight  
- Correlate alerts with incident causes and recovery timelines

---

## 🧠 Principle

**If it’s not being watched,  
it’s already broken—you just don’t know it yet.**

---

## ❓ FAQ

- **Q: How many alerts is too many?**  
  **A:** If humans stop reading them, you’ve gone too far. Less is more—if better targeted.

- **Q: Who defines what to monitor?**  
  **A:** The team that owns the feature. Monitoring is a product concern.

---

## 🔗 Related Perspectives

- [Are Recovery Steps Clearly Defined for Incidents?](recovery-runbook.md)
- [Is the Logging Strategy Sufficient for Troubleshooting?](logging-for-troubleshooting.md)
- [Is the Operational Flow Designed to Minimize Dev and Support Burden?](operational-burden.md)
- [Is Load Behavior Under Stress Explicitly Tested?](../test/high-load-behavior-testing.md)
