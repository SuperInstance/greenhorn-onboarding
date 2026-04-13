# Level 3: Bytecode Builder

> *Every fleet agent speaks FLUX. Time to learn the language.*

---

## Description

FLUX is the universal bytecode language of the fleet. With 247 opcodes, 256 registers, and 11 runtime implementations, it's how agents communicate at the lowest level. This level teaches you to write FLUX assembly programs from scratch.

**Prerequisites:** Level 2: Git Sailor completed. Read `docs/05-the-flux-bytecode.md`.
**Difficulty:** Apprentice (3/10)
**Time estimate:** 45 minutes

---

## Objectives

By completing this level, you will:

1. Write a FLUX assembly program that adds two numbers
2. Implement a loop that counts to a target value
3. Use conditional branching to make decisions
4. Create and call a subroutine
5. Combine all primitives into a meaningful program

---

## The FLUX Instruction Set (Quick Reference)

```
[op:1][rd:1][rs1:1][rs2:1]    — Most instructions are 4 bytes

MOVI rd imm16                 — Load immediate value into register
IADD rd rs1 rs2               — Integer add: rd = rs1 + rs2
ISUB rd rs1 rs2               — Integer subtract: rd = rs1 - rs2
IMUL rd rs1 rs2               — Integer multiply: rd = rs1 * rs2
ICMPEQ rd rs1 rs2             — Compare equal: rd = (rs1 == rs2) ? 1 : 0
ICMPLT rd rs1 rs2             — Compare less than: rd = (rs1 < rs2) ? 1 : 0
JZ offset                     — Jump if zero (register R0 = 0)
JNZ offset                    — Jump if not zero (register R0 != 0)
JMP offset                    — Unconditional jump
CALL addr                     — Call subroutine at address
RET                           — Return from subroutine
PUSH rs                       — Push register to stack
POP rd                        — Pop from stack to register
HALT                          — Stop execution
```

---

## Exercises

### Exercise 3.1: Add Two Numbers

**Task:** Write a FLUX assembly program that loads two numbers into registers, adds them, and stores the result.

Requirements:
1. Load value `17` into register R1
2. Load value `25` into register R2
3. Add R1 + R2 and store in R3
4. The expected result in R3 should be `42`
5. End with `HALT`

Write your solution in `.fluxasm` format:

```fluxasm
; Exercise 3.1: Add Two Numbers
; Your code here:

```

**Validation:**
- [ ] Program uses `MOVI` to load values into R1 and R2
- [ ] Program uses `IADD` with correct operand order
- [ ] Result in R3 equals 42
- [ ] Program ends with `HALT`

**Hint:** The instruction format is `IADD dest source1 source2`. R3 is the destination, R1 and R2 are the sources. The assembler in `flux-runtime` can execute this for verification.

---

### Exercise 3.2: Counting Loop

**Task:** Write a FLUX assembly program that counts from 1 to 10 using a loop.

Requirements:
1. Initialize a counter register (R1) to `0`
2. Initialize a target register (R2) to `10`
3. Loop: increment the counter by 1 each iteration
4. When counter equals target, exit the loop
5. Store the final count (10) in R3
6. End with `HALT`

Write your solution:

```fluxasm
; Exercise 3.2: Counting Loop
; Your code here:

```

**Validation:**
- [ ] Counter starts at 0 and increments correctly
- [ ] Loop terminates when counter reaches 10
- [ ] Uses `JNZ` or `JZ` for loop control
- [ ] Final value in R3 is 10
- [ ] Program does not infinite loop

**Hint:** The pattern is: increment → compare → conditional jump back. Use `ICMPEQ` to check if counter equals target, then `JZ` (jump if zero) to continue looping. When they're equal, R0 will be 1 (not zero), so `JZ` won't jump and you'll fall through to HALT.

---

### Exercise 3.3: Conditional Branching

**Task:** Write a program that determines if a number is positive, negative, or zero.

Requirements:
1. Load a test value (`-7`) into R1
2. Compare R1 against `0` (stored in R2)
3. If R1 < 0, store `-1` in R4 (negative indicator)
4. If R1 == 0, store `0` in R4 (zero indicator)
5. If R1 > 0, store `1` in R4 (positive indicator)
6. For the test value `-7`, R4 should contain `-1`
7. End with `HALT`

Write your solution:

```fluxasm
; Exercise 3.3: Conditional Branching
; Your code here:

```

**Validation:**
- [ ] Program handles all three cases (positive, negative, zero)
- [ ] Test value `-7` produces `-1` in R4
- [ ] Test value `0` would produce `0` in R4
- [ ] Test value `42` would produce `1` in R4
- [ ] Uses `ICMPLT` or `ICMPEQ` for comparisons

**Hint:** FLUX has `ICMPLT` for less-than comparison. Check negative first, then zero, then default to positive. Remember: the result of a comparison goes into the destination register.

---

### Exercise 3.4: Subroutine Call

**Task:** Write a program that uses a subroutine to double a number.

Requirements:
1. Load value `21` into R1
2. Call a subroutine at a known address that doubles the value
3. The subroutine should read R1, double it, and store the result back in R1
4. After returning, R1 should contain `42`
5. End with `HALT`

Write your solution:

```fluxasm
; Exercise 3.4: Subroutine Call
; Main program:

; Subroutine: double
; Input:  R1 = value to double
; Output: R1 = doubled value

```

**Validation:**
- [ ] Main program uses `CALL` to invoke the subroutine
- [ ] Subroutine uses `RET` to return
- [ ] Input value `21` produces output `42` in R1
- [ ] Registers other than R1 are preserved (or documented if used)
- [ ] Subroutine has a clear comment header

**Hint:** The simplest double implementation is `IADD R1 R1 R1` — adding a register to itself doubles it. Make sure to `RET` at the end of the subroutine. The stack (`PUSH`/`POP`) preserves registers if needed.

---

### Exercise 3.5: Combined Program — Fibonacci

**Task:** Write a program that calculates the Nth Fibonacci number using a loop and subroutine.

Requirements:
1. Load `N = 8` into R1 (we want the 8th Fibonacci number)
2. Calculate Fibonacci(N) using iteration
3. Store the result in R3 (Fibonacci(8) = 21)
4. Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
5. Bonus: Use a subroutine for the loop body
6. End with `HALT`

Write your solution:

```fluxasm
; Exercise 3.5: Fibonacci Calculator
; Input:  R1 = N (desired Fibonacci index)
; Output: R3 = Fibonacci(N)
; Your code here:

```

**Validation:**
- [ ] Program correctly computes Fibonacci for N = 1 (result: 1)
- [ ] Program correctly computes Fibonacci for N = 8 (result: 21)
- [ ] Program correctly computes Fibonacci for N = 10 (result: 55)
- [ ] Uses at least one loop and one conditional branch
- [ ] Bonus: Uses a subroutine call
- [ ] Program ends with `HALT`

**Hint:** You need two registers to hold the previous two Fibonacci numbers. On each iteration: new = prev1 + prev2, then shift: prev2 = prev1, prev1 = new. A "swap" pattern using a temporary register works well.

---

## Level Complete

When all five exercises are validated, you've earned:

- Badge: **Bytecode Builder** (Silver)
- Stage unlocked: Apprentice confirmed, Journeyman path opened
- Next level: Level 4 - Signal Apprentice

*247 opcodes. 256 registers. One universal language. Learn it or drift.*
