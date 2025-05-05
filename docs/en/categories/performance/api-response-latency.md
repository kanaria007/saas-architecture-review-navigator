---
title: API Latency Profiling
layer: [Structure]
category: performance
tags: [latency, response-time, measurement]
bloom_level: Apply
license: MIT
---

# Is API Latency Acceptable—and Understood?

> Type: Structure  
> Category: Performance  
> Audience: Engineers designing APIs, monitoring behavior, or debugging UX issues

---

## 🔍 What’s Actually Being Asked

Not “is it fast?”  
But:

- Is the latency **acceptable** under current conditions?  
- Is it **predictable** under load?  
- Do you **know what contributes** to the delay?

---

## ⚠️ Typical Issues

- High latency only under load—but no alerts fire  
- Spikes caused by background tasks or queue congestion  
- DB roundtrips and N+1 queries hidden in controller logic  
- Cold caches after deploys or config changes  
- API clients adding retry loops, compounding the slowness

---

## ✅ Healthier Latency Design

- Define SLOs and plot real distribution, not averages  
- Include latency budget breakdown in API design docs  
- Use timeout budgeting to balance retries vs user experience  
- Log latency contributors per request (DB, cache, external API)

---

## 🧠 Design Framing

Latency is not a number.  
It’s a **conversation between client pain and backend design.**

---

## ❓ FAQ

- **Q: Our p95 is fine. Is that good enough?**  
  **A:** Not if your tail spikes hurt the user more than your average helps.

- **Q: Can we just throw more infra at it?**  
  **A:** You can. Until you can’t afford to.

---

## 🔗 Related Perspectives

- [Are Backend Bottlenecks Designed Out—or Just Discovered Later?](backend-bottlenecks.md)
- [Can You Handle External Load Spikes Gracefully?](external-pressure-resilience.md)
- [Has the Need for Performance Testing Been Assessed?](../test/performance-test-plan.md)
- [Is Load Behavior Under Stress Explicitly Tested?](../test/high-load-behavior-testing.md)
