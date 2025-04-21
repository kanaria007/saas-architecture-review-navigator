# Is Your Validation Actually Enforced—or Just Wished For?

> Type: Structure  
> Category: Domain  
> Audience: Engineers who say “yeah, we validate it... somewhere”

---

## 🧠 The Real Question

Are invalid objects **impossible to create**?  
Or just **possible, but we hope we catch them later**?

This isn't about where you check things.  
It’s about who owns the truth.

---

## 💥 Signs of Trouble

- Validation is duplicated: in controller, service, AND domain  
- Validation is missing from object construction  
- Object is valid at first... until someone sets a field to something insane  
- Test cases: full of mocks, none for actual invalid state

---

## ✅ Good Validation Happens When…

- The domain refuses to represent illegal states  
  → Constructor/factory enforce invariants  
- Validation logic lives close to the model  
  → Not in a random controller or middleware  
- You encode “why this is wrong” with types, not just strings

---

## 🔍 Litmus Tests

- Can a developer construct an invalid object in one line?  
- Does your “domain” silently accept bad input and rely on downstream logic to yell?

---

## ❓ FAQ

- **Q: But isn’t this heavy-handed?**  
  **A:** Not if you care about trust. Code that can be invalid, eventually will be.

- **Q: Shouldn’t validation be centralized?**  
  **A:** Centralizing rules ≠ scattering responsibility.

---

## 🔗 Related Perspectives

- [Can Your System Even Represent an Invalid State?](invalid-states.md)
- [Is the Domain Separated from the Application Layer—and Does It Mean Anything?](domain-separation.md)
- [Is Your Index Designed—or Just Added After It Got Slow?](../data/index-design.md)
- [Is Authorization Modeled as Domain Behavior—or Just Filtered in the UI?](domain-permissions.md)
