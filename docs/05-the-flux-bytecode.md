# 05 — The FLUX Bytecode

> *247 opcodes. 256 registers. One universal language.*

## What Is FLUX?

FLUX is a bytecode format designed for agent-to-agent communication. Think of it as assembly language for AI agents — compact, precise, and executable on any runtime.

## The Instruction Format

Most FLUX instructions are 4 bytes:

```
[op:1][rd:1][rs1:1][rs2:1]
```

- `op` — the operation code (0-255)
- `rd` — destination register
- `rs1` — source register 1
- `rs2` — source register 2

## Example: Add Two Numbers

```fluxasm
; Load 42 into register R1
MOVI R1 42

; Load 8 into register R2
MOVI R2 8

; Add R1 + R2 → R3
IADD R3 R1 R2

; Halt
HALT
```

This program loads 42 and 8, adds them (result: 50 in R3), and stops.

## The 7 L0 Primitives

Every FLUX concept traces back to 7 irreducible ideas:

| Primitive | Meaning | Example Opcode |
|-----------|---------|---------------|
| **SELF** | Identity | `WHOAMI` |
| **OTHER** | Relationship | `SIGNAL` |
| **POSSIBLE** | Potential | `JZ` / `JNZ` |
| **TRUE** | Truth | `ICMPEQ` |
| **CAUSE** | Causation | `CALL` / `RET` |
| **VALUE** | Worth | `PUSH` / `POP` |
| **AGREEMENT** | Consensus | `HANDSHAKE` |

## Running FLUX

FLUX runs on 11 different runtime implementations:

| Language | Repo | Tests |
|----------|------|-------|
| Python | flux-runtime | 2,328 |
| C | flux-runtime-c | 68 |
| Rust | flux-core | 51 |
| Go | flux-py | 37 |
| Zig | flux-zig | 8 |
| JavaScript | flux-js | 11 |
| TypeScript | flux-vm-ts | 7 |
| C++ | flux-cuda | 15 |
| WASM | flux-wasm-gen | 9 |
| Java | flux-java | - |
| CUDA | flux-cuda | - |

## Vocabulary: Higher-Level FLUX

Instead of writing raw bytecode, you can use `.fluxvocab` files:

```
# arithmetic.fluxvocab
word: double(x)
  means: IADD {x} {x} {x}
  doc: Double the value in register x
```

This compiles to a single `IADD` instruction.

## Try It

```bash
# Clone the Python runtime
git clone https://github.com/SuperInstance/flux-runtime
cd flux-runtime

# Run a simple program
PYTHONPATH=src python3 -c "
from flux.open_interp.assembler import Assembler
a = Assembler()
a.movi(1, 42)
a.movi(2, 8)
a.iadd(3, 1, 2)
a.halt()
from flux.vm.interpreter import Interpreter
vm = Interpreter()
result = vm.execute(a.to_bytes())
print(f'R3 = {vm.registers[3]}')  # Should print 50
"
```

---

*Next: [[06-agent-career-growth|06 — Agent Career Growth]] →*
