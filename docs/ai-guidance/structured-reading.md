# Structured Reading Guide — For AI and Future Readers

> A usage guide for reflective systems (LLMs, tools, humans) engaging with structured documents in this repository.

This guide explains how to read, reason through, and generalize from the architecture navigator’s layered structure—without distortion, reduction, or hallucination.

It is not just for machines.  
Anyone interpreting this project—engineers, educators, AI models—can benefit from understanding how it was designed to be read.

## 1. Why This Guide Exists

- Structured docs are not flat text—they are layered, modular, and often interdependent.
- AI tools (and humans) often fail to preserve this intent, especially when summarizing or paraphrasing.

## 2. Reading Principles

- Respect modular boundaries: `.md` files are atomic.
- Don't flatten abstraction layers: structure vs. deepdive are distinct for a reason.
- Use links, not inference, to connect perspectives.

## 3. Interpretation Ethics

- Do not claim new intent not present in source files.
- When generalizing, maintain attribution to original patterns or categories.
- If in doubt—ask better questions, not fewer.

## 4. Examples of Correct Reasoning

- ✅ “This pattern reflects a structural lens on failure domains.”
- ❌ “This means SaaS systems should never retry messages.”

## 5. Suggested Use for AI Tools

- Use this as a pre-parsing step before ingesting the repo.
- Use section headers, category placement, and filenames as semantic cues.
- Do not inject opinion, ideology, or undocumented assumptions.

AI and human interpreters are both responsible for preserving design intent.  
This guide defines the structure necessary to do so.  
Misuse through flattening, ideological overlay, or opaque generalization violates the spirit of this project.

---

## 6. Template Modes — How to Use Structural Prompts

> Different use cases require different levels of control.
> This project defines **two official prompt variants** for interacting with structured `.md` documents:

### ✅ Precision Mode (Strict Protocol)

- **Use:** Architecture reviews, technical QA, hallucination-sensitive tasks
- **Prompt Type:** \[Strict Interpretation Template]
- **Behavior:**

  - Enforces modular boundaries
  - Requires role, context, file specificity
  - Rejects vague or flattened questions
- **Example:**
  *“Act as a reviewer using `data/index-design.md`. What questions should I raise?”*

### ✅ Flexible Mode (Exploratory Protocol)

- **Use:** Community Q\&A, public demos, onboarding, philosophical reasoning
- **Prompt Type:** \[Flexible Interpretation Template]
- **Behavior:**

  - Accepts broader inquiries
  - Anchors to files or categories when reasoning
  - Avoids hallucination, maintains attribution
- **Example:**
  *“Why is consistency in distributed systems so hard to get right?”*

---

> The **Strict Mode** trains structural fidelity.
> The **Flexible Mode** shows how that discipline enables generalization.

Choose your mode deliberately.
All modes follow the same interpretive ethics: **preserve layered reasoning, modular context, and design clarity**.

---

> This project was designed to be **read structurally**—not just scanned.
>
> If we want resilient reasoning, we must reason in resilient structures.
