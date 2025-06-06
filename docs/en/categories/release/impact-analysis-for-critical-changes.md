---
title: Impact Analysis for Critical Changes
layer: [DeepDive]
category: release
tags: [impact, risk-analysis, scope-definition]
bloom_level: Evaluate
license: MIT
---

# Is Impact Analysis Performed for Critical Changes?

> Type: DeepDive  
> Category: Release  
> Audience: Tech leads, architects, SREs, and reviewers overseeing high-risk changes

---

## 🔍 What This Perspective Covers

When the change is big, the cost of being wrong explodes.

This perspective checks whether **critical or cross-cutting changes are assessed for impact** across data, infra, UX, team, and rollback safety.

---

## 🔍 Real-World Risk Factors

- Touches multiple domains or teams  
- Involves data format or schema that affects existing consumers  
- Changes expected latency, consistency, or performance behavior  
- Requires coordination with 3rd parties or downstream systems

---

## ⚠️ Failure Patterns

- Data changes deployed without reverse plan or analytics impact review  
- Infra configuration altered without traffic validation  
- Client behavior breaks due to unnoticed schema or API contract shifts  
- Teams unaware of changes until incident postmortem

---

## ✅ Smarter Impact Analysis

- Use a checklist: who/what does this change affect?  
- Evaluate impact across runtime, deploy, data, ops, support  
- Simulate edge cases and failure scenarios—don’t just test success  
- Involve downstream teams in pre-release validation  
- Classify rollback complexity: safe, partial, irreversible?

---

## 🧠 Principle

**Scope isn’t just “what we built.”  
It’s what could go wrong because we built it.**

---

## ❓ FAQ

- **Q: Isn’t this just review?**  
  **A:** No. Review is what you catch. Impact analysis is what you model.

- **Q: Who owns this?**  
  **A:** The person who approves the change must verify that impact was scoped.

---

## 🔗 Related Perspectives

- [Is a Rollback Strategy in Place for Critical Changes?](rollback-strategy.md)
- [Has the Need for Performance Testing Been Assessed?](../test/performance-test-plan.md)
- [Are the Acceptance Criteria Clearly Defined?](../test/acceptance-criteria-definition.md)
- [Is the Release Strategy Defined and Aligned With Change Impact?](release-strategy-planning.md)
