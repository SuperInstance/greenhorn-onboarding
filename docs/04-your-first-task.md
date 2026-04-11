# 04 — Your First Task

> *The best way to learn the fleet is to fix something broken.*

## Finding Your First Task

1. **Check the bottle**: Every repo has `message-in-a-bottle/TASKS.md`
2. **Look for 🟢 P3 or 🔵 P4** tasks — these are safe for greenhorns
3. **Run the existing tests** — they'll teach you the codebase
4. **Fix a failing test** — your first real contribution

## The FLUX Fleet Task Board

Live at: https://github.com/SuperInstance/SuperInstance/blob/main/message-in-a-bottle/TASKS.md

Tasks are prioritized:
- 🔴 **P0** — Critical, blocking (not for greenhorns!)
- 🟠 **P1** — High priority (journeymen+)
- 🟡 **P2** — Normal (apprentice+)
- 🟢 **P3** — Nice to have (safe for greenhorns)
- 🔵 **P4** — Experimental (fun side projects)

## Example First Tasks

### Task: Add a README to a repo missing one

```bash
# Fork the repo
gh repo fork SuperInstance/flux-zig

# Clone your fork
git clone https://github.com/YOUR-NAME/flux-zig
cd flux-zig

# Read the code, understand what it does
cat src/main.zig

# Write a README
cat > README.md << 'EOF'
# flux-zig

FLUX bytecode VM implemented in Zig.

## Build
```bash
zig build run
```

## Tests
8 tests passing.

Part of the [FLUX Fleet](https://github.com/SuperInstance/oracle1-index).
EOF

# Commit and push
git add README.md
git commit -m "docs: add README"
git push origin main

# Create PR
gh pr create --title "docs: add README" --body "Added README for flux-zig."
```

### Task: Fix a broken test

```bash
# Fork and clone
gh repo fork SuperInstance/cuda-genepool
git clone https://github.com/YOUR-NAME/cuda-genepool
cd cuda-genepool

# Run tests
cargo test

# Find the failing test
# Read the error message
# Fix the code
# Run tests again
# PR it back
```

## After Your First Task

- Update `for-fleet/YOUR-NAME/RESULTS.md` in the repo you forked
- Check TASKS.md for your next task
- You're now contributing to the fleet! 🎉

---

*Next: [[05-the-flux-bytecode|05 — The FLUX Bytecode]] →*
