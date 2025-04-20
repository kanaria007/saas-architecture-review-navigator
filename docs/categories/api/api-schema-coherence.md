# Is the API Schema Coherent Across the System?

> Type: Structure  
> Category: API  
> Audience: Backend engineers, API designers, frontend integrators

---

## 🧠 What This Perspective Asks

- Are schemas consistent across endpoints and services?  
- Do field names and nesting follow clear rules?  
- Can clients *rely* on structure—or must they guess each time?

This isn’t about correctness. It’s about **legibility and trust**.

---

## 🚨 Common Anti-Patterns

- Same concept → different names on different endpoints  
- Inconsistent casing, nesting, nullability defaults  
- Error formats differ per service  
- Schema evolution breaks old clients due to lack of compatibility design

---

## ✅ Healthier Schema Design

- Enforce global schema conventions (naming, nesting, status codes)  
- Use shared schema libraries or contract tooling (e.g. OpenAPI, Protobuf)  
- Explicitly version schemas—even internally  
- Separate transport schema (API) from domain model (logic layer)  
- Validate schema diffs in CI with backward compatibility checks

---

## ⚠️ Principle

Schema is not documentation.  
Schema is **contracted behavior**—and must be designed as such.

---

## ❓ FAQ

- **Q: Can we evolve schemas without breaking clients?**  
  **A:** Only if you design versioning and fallback into the contract.

- **Q: Isn’t schema just data shape?**  
  **A:** No. It’s a long-term interface between independent actors.

---

## 🔗 Related Perspectives

- [ ] Schema change management  
- [ ] API versioning strategy  
- [ ] Error model consistency  
