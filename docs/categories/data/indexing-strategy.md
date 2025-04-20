# Is Your Index Strategy Designed—Or Just Inherited?

> Type: Structure  
> Category: Data  
> Audience: Backend engineers who haven’t looked at `EXPLAIN` in months

---

## 🧠 Why This Isn’t Just a Database Problem

Indexes shape the *access patterns* of your entire system.  
They’re not infra. They’re interface.

---

## 🚨 What Goes Wrong

- Indexes exist for writes that never get queried  
- Queries rely on fields without indexes → performance death spiral  
- Composite indexes exist... but the field order is wrong  
- Nobody knows which queries matter, so everything is “kind of slow”

---

## ✅ Good Index Design Practices

- Define **hot paths**—core queries that must stay fast  
- Validate indexes against real query plans (`EXPLAIN`, `analyze`)  
- Design composite indexes in **query usage order**  
- Revisit indexes after schema changes—not just at crisis time

---

## 🔍 Litmus Tests

- Can you name the top 3 most performance-critical queries in your system?  
- Do those queries align with current indexes?  
- When did someone last prune unused indexes?

---

## ❓ FAQ

- **Q: Isn’t this for the DBA to handle?**  
  **A:** Not if your schema is your product. You own what you ship.

- **Q: Should we index every field just in case?**  
  **A:** That’s not safety. That’s entropy.

---

## 🔗 Related Perspectives

- [ ] Access pattern-driven schema  
- [ ] Hot path identification  
- [ ] Post-migration index validation  
