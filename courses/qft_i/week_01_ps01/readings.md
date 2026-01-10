# Week 1 Reading Guide

*Detailed guide to P&S Chapter 2 and Tong Chapter 1*

---

## Primary Reading: Peskin & Schroeder Chapter 2

### Section 2.1: The Necessity of the Field Viewpoint (pp. 13-16)

**What to focus on**:
- The conceptual motivation: Why particles alone don't work relativistically
- The equal-time commutation relation idea
- Why we need fields that are operator-valued distributions

**Key equations**:
- None yet — this is motivation

**Don't worry about**:
- The specific quantization procedure (we'll return to this)

### Section 2.2: Elements of Classical Field Theory (pp. 16-21)

This is the **core reading** for Week 1.

**Pages 16-17: Lagrangian Field Theory**
- The action $S = \int d^4x \, \mathcal{L}$
- The field Euler-Lagrange equation
- **Key equation**: 
  $$\partial_\mu \left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)}\right) - \frac{\partial \mathcal{L}}{\partial \phi} = 0$$

**Pages 17-18: Hamiltonian Field Theory**
- Conjugate momentum $\pi(x) = \frac{\partial \mathcal{L}}{\partial \dot{\phi}}$
- Hamiltonian density $\mathcal{H} = \pi \dot{\phi} - \mathcal{L}$
- **Stop here for now** — the Poisson bracket discussion leads to quantization

**Pages 18-21: Noether's Theorem**
- **This is crucial** — read carefully
- Internal symmetries vs. spacetime symmetries
- The conserved current formula
- The stress-energy tensor $T^{\mu\nu}$
- **Key equation**:
  $$j^\mu = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} \Delta\phi - \mathcal{J}^\mu$$

### Reading Strategy

1. **First pass**: Read through once, don't stop at every equation
2. **Second pass**: Work through key derivations with pencil and paper
3. **Focus on**: The Noether current derivation — do it yourself!

---

## Secondary Reading: David Tong Chapter 1

**Link**: https://www.damtp.cam.ac.uk/user/tong/qft/one.pdf

Tong's notes are more pedagogical and include worked examples. Read this after P&S or alongside it.

### Section 1.1: Introduction

- Big picture motivation
- The Lagrangian formulation
- Good intuition-building

### Section 1.2: Lorentz Invariance

- Index notation conventions
- The metric $\eta_{\mu\nu}$
- Raising/lowering indices
- **Important**: Make sure you're comfortable with this notation!

### Section 1.3: Classical Field Theory

- The action and Euler-Lagrange equation
- Hamiltonian formalism
- Parallels P&S 2.2

### Section 1.4: Internal Symmetries

- Global vs. gauge symmetries (we only need global for now)
- U(1) symmetry example
- Conserved charges

### Section 1.5: Noether's Theorem

**Read carefully** — Tong explains this well
- The general derivation
- Examples: translation, rotation, phase rotation
- The stress-energy tensor

### Section 1.6: The Klein-Gordon Equation

- The paradigmatic scalar field theory
- $\mathcal{L} = \frac{1}{2}(\partial_\mu \phi)^2 - \frac{1}{2}m^2 \phi^2$
- Deriving the Klein-Gordon equation
- The stress-energy tensor for Klein-Gordon

---

## Key Concepts Checklist

After reading, you should understand:

### Formalism
- [ ] Why fields are the right framework for relativistic QM
- [ ] How to write an action from a Lagrangian density
- [ ] How to derive field equations from the action
- [ ] How to go from Lagrangian to Hamiltonian for fields

### Noether's Theorem
- [ ] The statement: continuous symmetry ↔ conserved current
- [ ] How to identify a symmetry transformation
- [ ] How to compute the Noether current
- [ ] Why $\partial_\mu j^\mu = 0$ implies a conserved charge

### The Stress-Energy Tensor
- [ ] What $T^{\mu\nu}$ represents physically
- [ ] How it arises from translation invariance
- [ ] The formula for $T^{\mu\nu}$ in terms of $\mathcal{L}$
- [ ] That $T^{00}$ is the energy density

### Notation
- [ ] Upper vs. lower indices
- [ ] The metric $\eta_{\mu\nu} = \text{diag}(1, -1, -1, -1)$
- [ ] Contraction: $A_\mu B^\mu = A^0 B^0 - A^i B^i$
- [ ] The 4-gradient: $\partial_\mu = (\partial_t, \nabla)$

---

## Worked Example: Klein-Gordon Field

**Lagrangian**:
$$\mathcal{L} = \frac{1}{2}\partial_\mu \phi \, \partial^\mu \phi - \frac{1}{2}m^2 \phi^2 = \frac{1}{2}\dot{\phi}^2 - \frac{1}{2}(\nabla\phi)^2 - \frac{1}{2}m^2\phi^2$$

**Field equation** (derive this!):

From $\partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} = \frac{\partial \mathcal{L}}{\partial \phi}$:

- $\frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} = \partial^\mu \phi$
- $\frac{\partial \mathcal{L}}{\partial \phi} = -m^2 \phi$

So: $\partial_\mu \partial^\mu \phi + m^2 \phi = 0$, i.e., $(\Box + m^2)\phi = 0$

**Conjugate momentum**:
$$\pi = \frac{\partial \mathcal{L}}{\partial \dot{\phi}} = \dot{\phi}$$

**Hamiltonian density**:
$$\mathcal{H} = \pi \dot{\phi} - \mathcal{L} = \dot{\phi}^2 - \frac{1}{2}\dot{\phi}^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2$$
$$= \frac{1}{2}\pi^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2$$

This is positive definite — energy is bounded below!

---

## Common Confusions

### Index Placement

$\partial_\mu \phi$ has a **lower** index (it transforms like a covector).  
$\partial^\mu \phi = \eta^{\mu\nu}\partial_\nu \phi$ has an **upper** index.

In Minkowski space with (+,-,-,-):
$$\partial_\mu \partial^\mu = \partial_t^2 - \nabla^2 = \Box$$

### The Sign of the Mass Term

The Klein-Gordon Lagrangian is $\mathcal{L} = \frac{1}{2}(\partial\phi)^2 - \frac{1}{2}m^2\phi^2$.

The minus sign makes this look like $T - V$ with $V = \frac{1}{2}m^2\phi^2 > 0$.

### Metric Convention

P&S uses the "mostly minus" convention: $\eta = \text{diag}(+,-,-,-)$.

Some books use "mostly plus": $\eta = \text{diag}(-,+,+,+)$.

**Stick with P&S convention** throughout this course.

---

**Next**: [socratic_guide.md](./socratic_guide.md) — Self-test your understanding
