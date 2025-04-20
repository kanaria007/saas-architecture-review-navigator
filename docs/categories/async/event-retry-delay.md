# Are Event Delays and Retries Part of Your Design—or Just Runtime Surprises?

> Type: Structure  
> Category: Async  
> Audience: Engineers building event-driven systems, workflows, or async pipelines

---

## 🧠 What This Perspective Covers

Async systems fail differently.  
They don’t crash. They **drift**.

- Retry loops that hide real failure  
- Invisible delays that break UX or violate SLAs  
- Side effects triggered multiple times without awareness

---

## 🚨 Common Anti-Patterns

- Retry forever on transient failures → permanent backlog  
- No delay compensation in UX → users spam reload  
- Events reordered → downstream consumers break silently  
- Delivery guarantee assumed, but never validated in test

---

## ✅ Stronger Event Flow Design

- Define max retry windows and dead-letter paths  
- Design for retry “echoes”: side effects should be idempotent  
- Use correlation IDs to trace event chains  
- Monitor queue latency separately from success/error metrics  
- Document SLA for delay-tolerant vs delay-critical events

---

## ⚠️ Core Principle

Async systems don’t fail loud.  
They fail **later and invisibly**—unless you design them not to.

---

## ❓ FAQ

- **Q: Isn’t retry always better than fail?**  
  **A:** Only if the retry is harmless.

- **Q: How do we know which events are sensitive to delay?**  
  **A:** Define UX expectations first. Then encode that into the pipeline.

---

## 🔗 Related Perspectives

- [ ] Async-side effect safety  
- [ ] Event delivery observability  
- [ ] SLA-aware event design  
