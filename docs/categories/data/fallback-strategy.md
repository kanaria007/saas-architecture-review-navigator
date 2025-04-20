# Do You Have a Fallback Plan for Asynchronous Failures?

> Type: DeepDive  
> Category: Data  
> Audience: Engineers designing event pipelines, retries, and error handling

---

## 🧠 What This Is Actually About

Async failures aren’t rare.  
They’re just delayed.

So the question is:

- What happens when retries fail?
- What if downstream data is already inconsistent?
- How do you stop cascading retries from compounding failure?

---

## 🚨 Failure Patterns

- Retry loops that cause double-inserts  
- No dead letter queue—just silent drops  
- Inconsistent intermediate states during retries  
- Failures that reprocess already-corrected data

---

## ✅ Good Fallback Strategies

- Dead-letter queues with alerting and visibility  
- State versioning or timestamps to detect reprocessing conflicts  
- Explicit deduplication checks on mutation events  
- Manual override or quarantine paths for human repair

---

## ⚠️ Principle

Your system should **fail visibly, not repeatedly**.

And when it fails—  
it should do so in a way that helps you recover meaningfully.

---

## ❓ FAQ

- **Q: Can’t we just retry until it works?**  
  **A:** What if it never does?

- **Q: Should fallback always mean human involvement?**  
  **A:** No—but someone should know it happened.

---

## 🔗 Related Perspectives

- [ ] Retry control and backoff strategies  
- [ ] Observability in async workflows  
- [ ] Recovery paths for non-idempotent events  
