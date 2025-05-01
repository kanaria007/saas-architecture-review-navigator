# 🛠 Contributing to SaaS Architecture Review Navigator

Thank you for considering a contribution.  
This project thrives on thoughtful insights, practical experience, and collaborative refinement.

---

## ✅ What You Can Contribute

We welcome contributions that strengthen the navigator as a **thinking tool**, not just a checklist.

- **New Perspectives**  
  Add a new `.md` file following the [Perspective Template](./docs/perspective-template.md).  
  Think in terms of:  
  > What design tension does this help resolve?

- **Improvements to Existing Perspectives**  
  Clarify, correct, or extend content.  
  For example:  
  - Better phrasing or logic  
  - Clearer examples or diagrams  
  - Stronger design justification

- **Real-World FAQ Additions**  
  If you’ve faced a recurring question in postmortems or design reviews—capture it here.

- **Translations**  
  Additional languages are welcome. Place translated content in a language-specific subfolder (e.g. `docs/ja/`).

- **AI-Assisted Writing (If Reviewed)**  
  You may use tools like ChatGPT or Grammarly to draft or revise content—**but human curation is required**.

---

## ❌ What We Avoid

To keep the navigator focused and coherent, we do not accept:

- Pure rewrites that reduce clarity  
- Style-only edits with no semantic gain  
- Alternate philosophy proposals (please fork instead)  
- SEO-driven or promotional content  
- Raw, unedited AI dumps

---

## 🧭 Contribution Principles

> This project is structured—but not dogmatic.

We encourage:

- Multiple phrasing styles, if they clarify insight  
- Similar perspectives with distinct trade-offs  
- Concrete examples drawn from real systems  
- Expansion of architectural reasoning—not just syntax or convention

---

## ✍️ Tone, Clarity, and Respect

This project originated in Japanese and was translated for global readability.  
We value:

- Precision over polish  
- Clarity over cleverness  
- Insight over opinion

---

## 🛠 Local preview

```bash
pip install \
  mkdocs-material \
  mkdocs-awesome-pages-plugin \
  mkdocs-git-revision-date-localized-plugin
mkdocs serve --config-file mkdocs.en.yml