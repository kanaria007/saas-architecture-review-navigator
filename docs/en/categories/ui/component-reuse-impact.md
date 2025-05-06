---
title: Component Reuse and UI Fragility
layer: [Structure]
category: ui
tags: [component-design, reuse, ui-risk]
bloom_level: Evaluate
license: MIT
---

# Is Component Reuse Helping or Hurting Your UI?

> Type: Structure  
> Category: UI  
> Audience: Frontend engineers, designers, or architects working on component-based design systems

---

## 🔍 What This Perspective Covers

Component reuse is not always virtuous.  
When overdone, it creates:

- Tight coupling across pages  
- Unexpected regressions when shared logic shifts  
- Unclear ownership: “Who owns this state?”

---

## ⚠️ Harmful Reuse Patterns

- Component behavior changes break other screens  
- Business-specific behavior embedded in “common” components  
- Global styling overrides cause layout fragility  
- Designers can’t update visuals without risking cross-app changes

---

## ✅ Better Reuse Strategies

- Split “generic” from “business” logic in components  
- Use adapter/wrapper patterns to preserve local override  
- Treat common components as APIs—not just code reuse  
- Write contract-based snapshot tests for shared UI  
- Version shared packages even inside monorepos

---

## 🧠 Core Principle

Reusable is not the same as **safe to reuse**.

---

## ❓ FAQ

- **Q: Isn’t DRY always good?**  
  **A:** Not if it creates shared risk across pages.

- **Q: Can’t design systems enforce consistency?**  
  **A:** Yes—but also create risk amplification.

---

## 🔗 Related Perspectives

- [Is the Impact Scope of This Change Clearly Understood?](../test/impact-scope-analysis.md)
- [Does Your API Design Prevent Breaking Changes?](../api/api-compatibility-strategy.md)
- [Is the API Schema Coherent Across the System?](../api/api-schema-coherence.md)
- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](../domain/domain-permissions.md)
