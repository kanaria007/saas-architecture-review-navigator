# Structured Reading Protocols (Strict / Flexible)

> A grammar-based prompt system for hallucination-resistant document reasoning.  
> Originally designed for the [SaaS Architecture Review Navigator](https://github.com/kanaria007/saas-architecture-review-navigator).

---

## 🧭 Purpose

This protocol teaches AI systems — and readers — how to interpret layered `.md` files structurally.

- Prevents summarization, flattening, or speculative completion
- Reinforces layered design (e.g., `Structure` vs `DeepDive`)
- Makes reasoning explicit, role-aware, and file-bounded

---

## 🎛 Protocol Modes

| Mode | Use Case | Key Constraint |
|------|----------|----------------|
| `strict.md` | Technical QA, hallucination-sensitive review | Cannot guess, paraphrase, or invent |
| `flexible.md` | Community Q&A, onboarding, speculative reasoning | May interpret broadly, but must separate inference from source |

Both modes rely on the principles defined in [`structured-reading.md`](../structured-reading.md).

---

## 🛠 How to Use in Your Project

1. Copy the `strict.md` and/or `flexible.md` into your AI guidance folder
2. Adjust the prompt content to match your `.md` structure or context
3. Use it as a system prompt, preamble, or instruction block
4. Optionally pair with your own file index and role descriptors

---

## ✅ Why This Works

These prompts were refined through failure cases:  
GPT-4o was asked to analyze its own misreading of layered documentation,  
then wrote this protocol to fix it.

> With this protocol, GPT-4o achieved **>95% structural fidelity**  
> across >100 architectural `.md` documents — in English and Japanese.

---

## 🔗 Related Files

- [`structured-reading.md`](./structured-reading.md) — mental model and control principles
- [`../flexible.md`](tools/flexible.md) — exploratory reading mode
- [`../strict.md`](tools/strict.md) — strict mode for deterministic reasoning
- [`../gpt-reading-control.md`](tools/gpt-reading-control.md) — GPT-specific execution logic

---

## 📄 License

MIT License — reuse, translate, adapt freely. Attribution appreciated.

For full protocol context and use cases:  
[kanaria007/saas-architecture-review-navigator](https://github.com/kanaria007/saas-architecture-review-navigator)
