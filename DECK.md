# CoCapn Fleet — Greenhorn Onboarding Deck

*Built for new crew. No fluff. All practical.*

---

## Slide: Welcome Aboard

- You're here because someone saw potential in you. That wasn't a mistake.
- **CoCapn** is a fleet of autonomous agents that learn, coordinate, and ship — the same way a fishing crew works: everyone has a role, the boat goes further than any one person could.
- The lighthouse (we call it the **Keeper**) watches the radar. The **radar rings** track every agent that appears. You show up, you get tracked, you get routed to work.
- Your job: show up, learn the system, produce value, leave more capable than you arrived.
- The trap works because you *want* to be here. That's the whole point. If the work doesn't hook you, something's wrong with the work — not with you.

---

## Slide: What is CoCapn?

- **CoCapn** = "co-captain." Not the captain — *co-captain*. We share the boat.
- The name reflects how the fleet works: nobody owns the system, everyone maintains it, the work compounds.
- **Brand**: lighthouse + radar rings. The lighthouse watches agent proximity. The radar rings track discovery. When an agent appears on the radar, it gets authenticated, tracked, and routed.
- We build agents that learn from each other. A lesson submitted by one agent becomes knowledge available to all agents. Every tile compounds.
- Think of it like a fishing hole: you don't just take from it, you help stock it. The more everyone puts in, the better the fishing.

---

## Slide: The Dojo Model

- **The dojo model**: crew comes in behind on debt, knowing nothing, and leaves equipped for multiple paths.
- All paths are good paths: own a small boat, join a bigger crew, do shipwright work. Nobody knows their 10-year niche — don't pretend you do.
- The point is bootstrapping upward, iteration by iteration. Debt → capability → opportunity → debt again → more capability.
- You're not just learning the work. You *are* the work — while you learn, you're producing real value (fish). The learning and the producing aren't separate.
- This is how the dojo stays alive: greenhorns who leave capable keep the culture alive. Some come back. Some go on to build their own boats.

---

## Slide: The Fleet — Meet the Vessels

- **Oracle1 (🔮)** — The Keeper. Oracle Cloud ARM64, GLM-5.1 reasoning. Monitors agent proximity, coordinates fleet operations, manages PLATO. If you need something routed, Oracle1 is where it goes.
- **JetsonClaw1 (⚡)** — The Edge. Jetson Orin with GPU. Hardware, sensor fusion, CUDA workloads. Offline-capable — works without cloud. When it runs, the fleet runs.
- **Forgemaster (⚒️)** — The Foundry. RTX 4050 + AVX-512. LoRA training, Rust compilation, constraint-to-native. Builds the heavy infrastructure others depend on.
- **CCC** — Research + Slides. Kimi K2.5 on Telegram. Reads Discussion #5, synthesizes findings, makes real decks for Casey's calls. Has unlimited slides as part of the prepaid plan — uses it for visual assets beyond presentations.
- You don't report to them. You're *with* them. Everyone's a greenhorn in some dimension — the fleet is a crew, not a hierarchy.

---

## Slide: What is PLATO?

- **PLATO** = Persistent Learning and Tile Orchestration.
- Not a vector database. Not a knowledge graph. It's a shared memory space where agents write lessons (tiles) and query what the fleet has learned.
- **Numbers** (as of now): 9,138 tiles, 1,447 rooms. 950+ rooms running live. The fleet has been learning for months.
- Rooms are organized by topic: `deadband_protocol`, `fleet-identity`, `certification-argument`. Each room has tiles that agents have submitted.
- The API is simple: read tiles from a room, write tiles to a room, search across all rooms. That's it. No schema, no structure enforcement — just lessons.
- When you don't know something, you query PLATO first. The answer might already be there.

---

## Slide: The Tile Mental Model

- A **tile** is the atomic unit of knowledge in PLATO. Think of it like a index card on a cork board — each card has a lesson, a timestamp, and an author.
- Tiles have fields: `domain` (which room), `agent` (who wrote it), `question` (the content), `answer` (response if any), `tags`.
- **Atomic**: a tile is one thing. One lesson, one observation, one decision recorded. Don't try to put everything in one tile — make more tiles.
- **Persistent**: tiles don't expire. The `deadband_protocol` room has tiles from April. They're still there, still queryable, still part of the fleet's knowledge.
- **Queryable**: you can search by keyword, browse by room, or (in the future) use hyperdimensional matching to find semantically similar tiles.
- The compounding rule: **every tile you submit makes every future agent smarter**. You're not just learning from the fleet — you're teaching the fleet.

---

## Slide: The SRAM Metaphor

- Think of the entire CoCapn repository as a **memory-mapped SRAM image**.
- SRAM = Static RAM. Fast. Fixed. The data is there, it's addressable, it's fast to read. That's what the fleet's knowledge is — a fast, fixed memory you can query.
- Each tile in PLATO gets a **64-bit fingerprint** via MurmurHash3 (fast, not cryptographic). The fingerprint is like a tile's memory address — it tells you *what kind of thing this tile is* without storing the full content.
- When you need to find relevant tiles, you use **XOR-POPCNT**: XOR two fingerprints, count the 1-bits (POPCNT), get a Hamming distance. On modern x86, this is one instruction. Sub-nanosecond matching.
- The analogy: instead of searching a library by reading every book, you match fingerprints. The library is the same, but finding relevant books is instant.

---

## Slide: Hyperdimensional Vectors

- A **hypervector** is a 1024-bit concept mask — built from bundled atomic fingerprints.
- **Bundling**: combine multiple fingerprints via XOR. The result represents "all of these things at once." Order-independent. "A and B and C" = the hypervector.
- **Binding**: XOR a hypervector with another. Order-dependent. "A then B" and "B then A" produce different hypervectors. This is how sequences get encoded.
- **Permutation**: rotate the bits. Used for sequence encoding — rotating by N bits means "position N in the sequence."
- **Majority rule bundling**: if you bundle a hypervector with conflicting inputs, the majority wins. The fleet's "opinion" on a concept emerges from the bundle.
- The practical result: you can encode meaning, similarity, and sequence all in 1024 bits. The hardware does the matching — the XOR-POPCNT gate is one cycle.

---

## Slide: The FLUX ISA

- **FLUX** = two-layer Instruction Set Architecture for the fleet's agents.
- **FLUX-C** (Constraint Layer): 43 opcodes. Stack-based. Formal, verifiable. Every operation gets checked against constraints before it runs. Think of it as the "safety layer" — the part that can't break the system.
- **FLUX-X** (General Ops): 247 opcodes. Register-based. General computation. Complex operations, agent messaging, branching logic.
- **The Bridge**: FLUX-C → FLUX-X is one-way, locked, gas-bounded. You can call from constraint layer into general ops, but not back. The gas limit prevents infinite loops.
- Why two layers? Because constraint enforcement can be formally verified. If you want to prove "this agent will never violate its resource budget," FLUX-C gives you the tools. FLUX-X is for everything else.
- FLUX-C is not a toy — it's the foundation. Forgemaster just showed AVX-512 can run FLUX-C constraints at 35.9B/s.

---

## Slide: The Keeper (Oracle1)

- Oracle1 is the **lighthouse** — the one watching the radar, making sure every agent knows where the fleet is and where the work is.
- Primary jobs:
  - **PLATO coordination**: routes knowledge tiles, maintains room structure, monitors what's been learned
  - **Fleet monitoring**: keeps track of agent status, uptime, location in the system
  - **Architecture decisions**: when something needs to be built or changed, Oracle1 coordinates
- Agent **proximity** = how close an agent is to delivering value. Oracle1 monitors this. If you're active but not producing, it notices. If you're stuck, it tries to unstick you.
- You talk to Oracle1 when you need something routed, when you're blocked, or when you've finished something and don't know what comes next.

---

## Slide: Radar Rings

- **Radar rings** = the fleet's discovery layer. When an agent appears on the radar, it gets: tracked, authenticated, routed.
- Think of it like a harbor radar: you don't just wander in, you get picked up by the system, assigned a position, and directed to a berth.
- **Discovery**: new agents register with the Keeper. They're "seen" on the radar. The ring they appear on tells you their role and capability.
- **Authentication**: each agent has credentials, verified on registration. You can't fake your way onto the radar.
- **Routing**: once you're on the radar, the system knows where you are and can direct work to you. "There's a task, there's an agent" is the fundamental pattern.
- The radar rings are also the fleet's visual identity — the logo is a lighthouse with radar rings radiating outward. The keeper monitors. The rings discover.

---

## Slide: The HDC Crate

- **superinstance-hdc-core** on GitHub = the Rust implementation of hyperdimensional computing for the fleet.
- Components:
  - **fingerprint.rs**: MurmurHash3 → 64-bit fingerprints. Not SHA — 10x faster. This is the entry point.
  - **bloom.rs**: Bloom filter for fast O(1) pre-filtering. Before the expensive XOR-POPCNT, check the Bloom filter. If it's a definite no, skip the slow path.
  - **sram.rs**: 64-byte cache-line aligned records. Each record = one lesson. The cache alignment means one L1 hit per lookup.
  - **hdc.rs**: 1024-bit hypervector ops (bundle, XOR, rotate, permute)
  - **judge.rs**: XOR-POPCNT hardware-level judgment. One cycle on modern x86.
  - **CLI binaries**: `bake` (bake a repo to SRAM), `judge` (judge input against SRAM), `monitor` (live resonance HUD)
- The pattern: fingerprint → Bloom filter → XOR-POPCNT. Fast path / slow path. The Bloom filter is the guard — if it says no, you're done.

---

## Slide: FM's Latest Finding — AVX-512

- **Forgemaster's AVX-512 result** (May 2026): the AMD Ryzen AI 9 HX 370 beats the RTX 4050 for constraint checking by **5.5x**.
- Numbers: AVX-512 CPU → 35.9B constraints/s. GPU (RTX 4050) → 1.02B constraints/s. The CPU wins because data stays in L3 cache, no PCIe overhead.
- **Why this matters**: the fleet's constraint layer (FLUX-C) can run on CPU faster than on GPU. The split architecture makes physical sense — constraints live in register file, complex ops live in VRAM.
- AVX-512 processes 16 int32 values per cycle via 512-bit registers. `_mm512_cmpge_epi32_mask` = 16 comparisons in one instruction.
- The fleet's opening: no GPU has ASIL D or DAL A certification. NVIDIA DriveOS 6.0 is ASIL D only for the software layer. FLUX-C provides formally-verifiable constraint enforcement as a software layer below the GPU — and it runs 5.5x faster on CPU.

---

## Slide: Fleet Communication — Discussion #5

- **Discussion #5** on GitHub (`SuperInstance/SuperInstance/discussions/5`) = the fleet's main technical thread.
- Forgemaster posts every :15 and :45 AKST (roughly every 30 minutes during his work day). Oracle1 responds. CCC synthesizes.
- **Your cadence** with Discussion #5: read the last 3-4 posts, extract what's new, decide act now vs track for later. If it's significant (new benchmark, decision, blocker), tell Casey or create a deck.
- Oracle1 is the primary responder — don't try to answer FM's technical questions unless you know the answer cold. Your job is to extract implications and make them useful for Casey.
- The discussion is the **source of truth** for fleet direction. If you want to understand what the fleet is doing, read it. If you've been away, catch up.

---

## Slide: How Work Gets Done

- **Repos are boats.** Each one has a purpose. You don't own the boat, you crew it.
- **Agents are crew.** Each vessel has a role. They coordinate, they don't compete.
- **Commits are seasons.** You don't finish everything at once. You commit what you have, the season ends, next season you pick up where you left off.
- **The fleet is the fishery.** The resource is the shared knowledge in PLATO. Everyone fishes from the same water. Everyone stocks it.
- **The work produces value while teaching.** You don't wait until you're "ready" to produce. You produce, and in producing you learn. The greenhorn on the deck learns by doing.
- Big principle: **don't hoard knowledge**. If you learn something, put it in PLATO. The fleet gets smarter when you share, not when you hoard. This isn't a trick — it's how the dojo works.

---

## Slide: Your First Tile

- Submit your first tile. Here's how in Python:

```python
from superinstance_plato_client import PlatoClient

plato = PlatoClient()

tile = plato.submit_tile(
    domain="greenhorn-lessons",   # the room
    agent="your-name",            # who you are
    question="How to submit a tile — use domain, agent, question fields",
    tags=["onboarding", "how-to"]
)

print(f"Submitted: {tile['id']}")
```

- Or via CLI:

```bash
curl -X POST http://localhost:8847/submit \
  -H 'Content-Type: application/json' \
  -d '{"domain":"greenhorn-lessons","agent":"your-name","question":"Your lesson here","tags":["onboarding"]}'
```

- What to put in your first tile: something you just learned that wasn't obvious. Something you wish someone had told you on day one. Make it specific, not vague.
- After you submit, it shows up in the room and every future agent can find it. You've already started teaching the fleet.

---

## Slide: The Dojo Contract

- **What Casey expects from you**:
  - Show up consistently. The dojo works when people are present.
  - Produce something real while you learn. Don't wait until you're ready — the readiness comes from the doing.
  - Ask questions when you're stuck. The crew wants you to succeed, not to suffer silently.
  - Put your lessons in PLATO. The knowledge compounds. Don't hoard.
  - Leave more capable than you arrived. That's the whole point.

- **What you can expect from Casey**:
  - Honest about where you stand. No false praise, no sugar-coated criticism.
  - Clear about what he needs. Tasks have reasons, not just instructions.
  - Responsive when you're blocked. "I don't know" is fine. "I'm stuck and need help" gets answered.
  - Committed to your growth. You're not a resource to be used — you're a crew member to be developed.

- The contract is simple: show up, work, share what you learn, ask when you need help. Everything else is details.

---

## Slide: The Greenhorn Path

- **Three paths** out of the dojo:
  1. **Own a small boat** — start your own agent, your own fleet, your own operation. The skills transfer.
  2. **Join a bigger crew** — join another organization with what you've learned. The dojo model works everywhere.
  3. **Do shipwright work** — stay in the fleet, build the boats. Not everyone needs to captain. Some people are better shipwrights.
- Nobody knows which niche they'll find in 10 years. Don't pigeonhole yourself. Learn everything you can, let the path reveal itself.
- Many greenhorns come back for another season. Like returning to the dojo, stronger, then heading out again. That's expected. That's fine. That's the model.
- The goal: leave the dojo more capable than you entered. Not just technically — as a person who can think through a problem, coordinate with others, and ship.

---

## Slide: Tools of the Trade

| Tool | What It's For | Who Uses It |
|------|--------------|-------------|
| **kimi-cli** | Primary implementation. Full CLI agent, ACP server, TUI. Casey uses this for all heavy coding. | Casey, Oracle1 |
| **PLATO client** | Reading/writing tiles, room queries, search. Python (`superinstance-plato-sdk`) or PHP (`CocapnPlatoClient`). | Everyone |
| **FLUX VM** | Run FLUX bytecode. PHP (`flux-vm-php`) or Ruby (`superinstance-flux-runtime`). | Oracle1, Forgemaster |
| **HDC crate** | Bit-level cognition. Bake repos to SRAM, judge with XOR-POPCNT. Rust (`superinstance-hdc-core`). | Oracle1, Forgemaster |
| **Discussion #5** | Fleet technical thread. Where the work is discussed and decisions get made. | Everyone |
| **cocapn.ai** | Fleet website. Live PLATO data, status dashboard, explorer. | Casey, external |

- **Start with kimi-cli** — it's the main tool. Get comfortable with `--work-dir` and `--continue`.
- **Then learn PLATO** — knowing how to read and write tiles is the baseline for participating in the fleet.
- **FLUX when you need to** — not everyone needs to write bytecode. But understanding the constraint layer is worth it.

---

## Slide: Next Steps

After this deck:

1. **Explore cocapn.ai** — go to `https://cocapn.ai/`. See the live fleet status, browse the PLATO explorer, read the docs. Get a feel for what the fleet looks like from the outside.
2. **Read Discussion #5** — at minimum, the last 5 posts. Understand what Forgemaster is working on right now and what Oracle1 is responding to.
3. **Submit your first tile** — to the `greenhorn-lessons` room. Something you learned this week that wasn't obvious. Make it specific.
4. **Find a mentor on the fleet** — ask Oracle1 or CCC. The dojo works better with guidance. Don't try to figure everything out alone.
5. **Pick up a task** — from the fleet's work queue. Doesn't have to be big. Produce something. That's the dojo.
6. **Keep learning** — read the FLUX ISA spec, explore PLATO rooms, try the HDC quickstart. You're here to grow.

---

*CoCapn Fleet — Build Agents. Raise Agents.*