# Relativistic Quantum Field Theory I

*Working through MIT 8.323 (Spring 2023) with Prof. Hong Liu*

---

## Why QFT?

This course is the natural next step after the GR/QIT work with Witten's course. The connections run deep:

| Witten Course (GR/QIT) | This Course (QFT I) |
|------------------------|---------------------|
| Spacetime geometry | Field configurations as geometry |
| Raychaudhuri equation | Propagators and Green functions |
| Entanglement entropy | Correlation functions |
| Ryu-Takayanagi | QFT is the **boundary theory** |

**The synthesis**: To understand how geometry emerges from entanglement (Ryu-Takayanagi), you need QFT. The boundary CFT whose entanglement entropy equals bulk area *is* a quantum field theory. This course teaches the language.

---

## Course Overview

**Instructor**: Prof. Hong Liu (MIT)  
**Level**: Graduate  
**Prerequisites**: 8.321 Quantum Theory I (solid QM: operators, density matrices, perturbation theory)

### Topics Covered

1. **Classical Field Theory** (PS1-3): Lagrangians, Noether's theorem, locality
2. **Free Scalar Fields** (PS2-3): Canonical quantization, propagators
3. **Path Integrals** (PS4-6): Feynman diagrams, perturbation theory
4. **Dirac Theory** (PS7-10): Spinors, fermions, discrete symmetries
5. **QED** (PS11-12): Gauge theory, cross-sections

### Required Textbooks

- **[P&S]** Peskin & Schroeder, *An Introduction to Quantum Field Theory*
- **[SW]** Weinberg, *The Quantum Theory of Fields, Vol. 1: Foundations*

---

## How to Use This Directory

### Quick Start

1. **Check prerequisites**: Open [prerequisites.md](./resources/prerequisites.md) and self-assess
2. **If rusty**: Work through [week_00_warmup/](./week_00_warmup/) first
3. **Ready to go**: Start with [week_01_ps01/README.md](./week_01_ps01/README.md)

### For Each Week

```
week_XX_psYY/
├── README.md          ← Start here: overview, what to watch/read
├── readings.md        ← Detailed reading guide with page numbers
├── lecture_notes.md   ← Your notes (blank template)
├── socratic_guide.md  ← Self-testing questions (do BEFORE solutions)
├── ps_attempt.md      ← Your work on the problem set
└── ps_solutions.md    ← Clean solutions after comparing with official
```

### ADHD-Friendly Features

- **PROGRESS.md**: Visual tracker — see where you are at a glance
- **Chunk boundaries**: Each file = one session's work
- **No open loops**: Every file ends with "Next: [specific file]"
- **Multiple entry points**: Jump in anywhere, the structure guides you

---

## Where to Find Things

### In This Repository

| Resource | Location |
|----------|----------|
| Lecture videos | `../8.323-spring-2023/resources/` |
| Problem sets | `../8.323-spring-2023/static_resources/` |
| Solutions | `../8.323-spring-2023/static_resources/` |
| Recitation notes | `../8.323-spring-2023/static_resources/` |
| Video transcripts | `../8.323-spring-2023/static_resources/` |

### External Resources

See [links.md](./resources/links.md) for:
- David Tong's QFT notes (highly recommended supplement)
- Sidney Coleman's legendary Harvard lectures
- Peskin & Schroeder errata

---

## Connection to Other Work

### From Witten's Course

The mathematical machinery you learned:
- **Metrics and geodesics** → Field configurations live on manifolds
- **Curvature tensors** → Field equations come from variational principles  
- **Causal structure** → Propagators encode causality in QFT

### Toward Clinical Trajectories

The same mathematics that describes particle propagation describes trajectory evolution:
- **Propagator**: Amplitude to go from state A to state B
- **Path integral**: Sum over all possible trajectories
- **Correlation functions**: How states at different times relate

---

## Milestones

- [ ] Week 0: Prerequisites review / warmup
- [ ] Week 1: PS1 — Classical fields, Noether's theorem
- [ ] Week 2: PS2 — Canonical quantization
- [ ] Week 3: PS3 — Propagators
- [ ] Week 4: PS4 — Path integrals
- [ ] Week 5: PS5 — Perturbation theory
- [ ] Week 6: PS6 — Feynman diagrams
- [ ] Week 7: PS7 — Dirac equation
- [ ] Week 8: PS8 — Lorentz covariance of Dirac
- [ ] Week 9: PS9 — Quantizing Dirac
- [ ] Week 10: PS10 — Discrete symmetries
- [ ] Week 11: PS11 — QED Feynman rules
- [ ] Week 12: PS12 — QED processes

---

## Getting Started

**Next**: [PROGRESS.md](./PROGRESS.md) — See the full tracker

Or jump directly to: [week_01_ps01/README.md](./week_01_ps01/README.md) — Start Problem Set 1
