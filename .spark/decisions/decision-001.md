---
room: decisions
type: rationale
id: 001
author: greenhorn-onboarding
timestamp: 2026-05-03T18:09:00Z
confidence: high
tags: [onboarding, design]
references: []
---

# Why Zero-Config Onboarding

**Decision:** Onboarding requires zero conversation. Point agent at repo, give PAT, walk away.

**Rationale:**
- Human time is expensive. Agent time is cheap.
- Agents can read and follow docs better than humans
- The docs can be improved by agents (self-improving system)
- If the docs aren't good enough, improve the docs — don't add a human layer

**Tradeoff:** Requires excellent documentation. Worth the investment.

**This is the Bootstrap Spark applied to onboarding:** the repo IS the onboarding. The Spark lights the fire.
