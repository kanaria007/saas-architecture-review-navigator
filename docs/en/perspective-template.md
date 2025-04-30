# [Perspective Title Here]

## 🔍 What This Perspective Covers

This section explains the scope of this perspective.
For example:
> This perspective covers how asynchronous APIs handle message delivery and retries.

It should answer:

- What kind of design decisions are involved here?
- Why does this topic matter in SaaS architecture?

## ⚠️ Unsafe Patterns

List common design mistakes or failure modes.
For example:

- Retrying without backoff leads to cascading failures
- Missing idempotency in message consumers

## ✅ Safer Design Patterns

Describe recommended patterns and strategies.
For example:

- Use exponential backoff and jitter
- Persist retry states in durable storage

Include trade-offs if relevant.

## 🧠 Design Principle

Mention the key architectural principle or mental model.
For example:
> Favor eventual consistency with observability over strict synchronization when cross-system reliability is required.

## ❓ FAQ

Common questions and clarifications.

- Q: Should retries be infinite?
  A: No, retries must be bounded and observable.
- Q: When to use event sourcing instead?
  A: When full history and mutation replay are needed.

## 🔗 Related

- another-perspective.md