# The Geometry of Information

*A computational exploration of General Relativity, Quantum Information, and Deep Learning*

---

## Overview

This repository documents a journey through Edward Witten's **Physics 539: Topics in Quantum Information and Gravity** (IAS, Fall 2022), augmented with neural network verification using the [EinFields](https://github.com/...) framework.

The work is guided by a central intuition: **spacetime geometry and quantum entanglement are two languages describing the same underlying reality** — and the mathematical machinery connecting them may have profound implications for how we understand and optimize learning systems.

---

## The Central Mystery

Why does a black hole have entropy proportional to its *area* rather than its volume?

$$S = \frac{A}{4\hbar G}$$

This formula looks like it's counting degrees of freedom on a *boundary* rather than in the *bulk*. Witten's course builds the mathematical machinery to understand why — and along the way reveals deep connections between curved spacetime, causal structure, and quantum correlations.

---

## The Journey

### Act I: The Grammar of Curved Spacetime *(Complete — human-verified)*

**Problem Set 1** — The Raychaudhuri equation tells us that gravity focuses light. Worked through by hand via Socratic derivation, then verified computationally:

$$g_{\mu\nu} \to \Gamma^\rho_{\mu\nu} \to R_{\mu\nu}$$

A neural network trained on Schwarzschild spacetime learned not just the metric, but its derivatives — the quantities encoding curvature.

**Key artifact**: [`notebooks/einfields.ipynb`](notebooks/einfields.ipynb) — Neural Schwarzschild metric verification

### Act II: Where Light Cannot Escape *(AI-generated, pending human verification)*

**Problem Set 2** — Null geodesics and trapped surfaces. A black hole is not "where gravity is strong" but a *causal structure*: a region from which no signal can reach infinity.

*Solutions exist as scaffolding; next step is to work through by hand and verify with EinFields.*

### Act III: The Statistical Mechanics of Ignorance *(AI-generated, pending human verification)*

**Problem Set 3** — Density matrices and von Neumann entropy. The mathematics of incomplete knowledge, leading to the Ryu-Takayanagi formula connecting entanglement to geometry.

*Solutions exist as scaffolding; will follow PS2 in the verification cycle.*

---

## The Bidirectional Vision

We pursue a two-way relationship between differential geometry and deep learning:

| Direction | Description |
|-----------|-------------|
| **Forward** | Use neural networks to learn and verify spacetime geometry |
| **Converse** | Use spacetime mathematics to improve optimization algorithms |

### The Converse: Geometry for Optimization

The loss landscape of a neural network *is* a curved space. Gradient descent treats it as flat — following coordinate directions rather than geodesics. 

**The intuition**: Just as particles follow geodesics in curved spacetime, perhaps optimal learning should follow geodesics in parameter space. The Hessian is the curvature. Christoffel symbols could *correct* naive gradients.

**Connections we're exploring**:
- Natural gradient descent (Fisher information as Riemannian metric)
- Information geometry (probability space is curved)
- Ricci flow for smoothing loss landscapes
- "Trapped surfaces" in optimization (regions SGD cannot escape)

---

## Application: Clinical Trajectory Geometry

A parallel application motivates this work: modeling **hospital encounters as curved spacetime**.

| Spacetime Concept | Clinical Analog |
|-------------------|-----------------|
| Points | Patient states (vitals, labs, diagnoses) |
| Metric | Similarity/distance between states |
| Geodesics | Optimal clinical trajectories |
| Curvature | How trajectories focus/diverge |
| Trapped surfaces | States from which outcomes inevitably deteriorate |

The mathematics of black holes may illuminate the mathematics of clinical decision-making.

---

## Repository Structure

```
physics/
├── README.md                    # This document
├── ROADMAP.md                   # Detailed vision and plan
├── notebooks/
│   └── einfields.ipynb          # Neural Schwarzschild verification
└── courses/
    └── witten_gr_qit/
        ├── problem_set_1/       # Causal structure, Raychaudhuri (COMPLETE)
        ├── problem_set_2/       # Null hypersurfaces, trapped surfaces
        └── problem_set_3/       # Quantum information theory
```

---

## Setup

### Requirements

- Python 3.11+
- JAX with CUDA support (for GPU acceleration)
- [EinFields](https://github.com/...) framework

### Quick Start

```bash
# Clone this repo
git clone https://github.com/yourusername/physics.git

# Clone EinFields alongside
git clone https://github.com/... EinFields

# Install dependencies
pip install jax[cuda12] numpy matplotlib sympy

# Run the verification notebook
cd physics/notebooks
jupyter lab einfields.ipynb
```

For GPU support, see `.devcontainer/` for a ready-to-use development container configuration.

---

## Intellectual Lineage

This work draws on several traditions:

- **Edward Witten** — The course material and problem sets
- **Sylvester James Gates Jr.** — The insight that discrete graph structures (adinkras) encode smooth geometric information, bridging combinatorics and differential geometry
- **Information Geometry** — Amari, Ay, and others on the Riemannian structure of probability spaces
- **Neural Differential Geometry** — EinFields and related work on learning geometric quantities

The connection between Gates' adinkras and the discrete↔smooth bridge is particularly relevant: his work shows how supersymmetry algebras can be encoded in graph-theoretic objects, suggesting deep structural links between discrete and continuous mathematics.

---

## Key Results

### From Problem Set 1

**R_tt Formula** (Raychaudhuri):
$$R_{tt} = -\frac{1}{2}\partial_t\text{Tr}(g^{-1}\dot{g}) - \frac{1}{4}\text{Tr}(g^{-1}\dot{g})^2$$

**Neural Verification**: Trained MLP achieved loss ~2×10⁻⁶ on Schwarzschild metric with Jacobian and Hessian supervision. Ricci tensor computed via autodiff matches analytical within ~1%.

### From Quantum Information (Preview)

**Ryu-Takayanagi**:
$$S_A = \frac{\text{Area}(\gamma_A)}{4 G_N}$$

Entanglement entropy of boundary region = Area of minimal bulk surface. Geometry IS entanglement.

---

## License

Educational use. Problem statements from Physics 539 (Fall 2022), Edward Witten, Institute for Advanced Study.

---

## Contact

This work is part of ongoing explorations in computational physics and geometric deep learning. For questions or collaboration, please open an issue.

---

*"The universe is not only queerer than we suppose, but queerer than we can suppose."* — J.B.S. Haldane
