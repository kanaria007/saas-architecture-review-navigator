# Are Backend Bottlenecks Designed Out—or Just Discovered Later?

> Type: DeepDive  
> Category: Performance  
> Audience: Engineers responsible for architecture, resource allocation, or debugging production slowness

---

## 🔍 What This Perspective Covers

You can’t eliminate all bottlenecks.  
But you can **decide which ones are acceptable—and when.**

---

## ⚠️ Symptoms of Undesigned Bottlenecks

- Intermittent slowness under load, but no clear root cause  
- DB or storage tiers doing “just fine”—until cascading latency hits  
- Feature X suffers when Feature Y gets traffic  
- Shared background worker pool starving critical tasks  
- Nobody knows which task owns the CPU/memory spike

---

## ✅ Proactive Bottleneck Design

- Budget IOPS, CPU, memory per feature or queue  
- Assign explicit priority to background tasks  
- Isolate high-load tenants from shared infrastructure  
- Visualize workload mix over time—not just peak load  
- Include “slow path” UX impact in design reviews

---

## 🧠 Framing Shift

Bottlenecks aren’t failures.  
They’re **choices about who gets hurt first.**

Make that choice on purpose.

---

## ❓ FAQ

- **Q: Can’t we just scale up?**  
  **A:** If you don’t know what’s slow, scaling helps…until it doesn’t.

- **Q: Shouldn’t the infra team handle this?**  
  **A:** Infra can give you capacity. Only you know how it’s used.

---

## 🔗 Related Perspectives

- [Is Your Scaling Strategy Designed—or Just Assumed?](scaling-strategy.md)
- [Is API Latency Acceptable—and Understood?](api-response-latency.md)
- [Is Load Behavior Under Stress Explicitly Tested?](../test/high-load-behavior-testing.md)
- [Is Your Index Designed—or Just Added After It Got Slow?](../data/index-design.md)
