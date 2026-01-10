# Classical Mechanics Review for QFT

*Lagrangians, Hamiltonians, and the variational principle*

---

## Overview

Quantum field theory begins with **classical field theory**. The first few weeks of the course extend the mechanics you know (particles) to fields (functions defined everywhere in space). The structure is parallel:

| Particle Mechanics | Field Theory |
|-------------------|--------------|
| Position $q(t)$ | Field $\phi(x, t)$ |
| Lagrangian $L(q, \dot{q})$ | Lagrangian density $\mathcal{L}(\phi, \partial_\mu \phi)$ |
| Action $S = \int L \, dt$ | Action $S = \int \mathcal{L} \, d^4x$ |
| Euler-Lagrange equation | Field equations |
| Noether's theorem (symmetries → conservation) | Same! |

---

## 1. The Lagrangian Formulation

### The Lagrangian

For a particle, the Lagrangian is:

$$L(q, \dot{q}, t) = T - V = \frac{1}{2}m\dot{q}^2 - V(q)$$

where $T$ is kinetic energy and $V$ is potential energy.

### The Action

The action is the integral of the Lagrangian over time:

$$S[q] = \int_{t_1}^{t_2} L(q, \dot{q}, t) \, dt$$

Note: $S$ is a **functional** — it takes a whole path $q(t)$ and returns a number.

### Hamilton's Principle

**The physical path is the one that makes the action stationary.**

$$\delta S = 0$$

"Stationary" means that small variations in the path don't change $S$ (to first order).

### The Euler-Lagrange Equation

Requiring $\delta S = 0$ leads to:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right) - \frac{\partial L}{\partial q} = 0$$

**Example**: Free particle, $L = \frac{1}{2}m\dot{q}^2$
- $\frac{\partial L}{\partial \dot{q}} = m\dot{q}$
- $\frac{\partial L}{\partial q} = 0$
- Euler-Lagrange: $\frac{d}{dt}(m\dot{q}) = 0 \Rightarrow m\ddot{q} = 0$

This is Newton's second law for a free particle!

### Multiple Degrees of Freedom

For coordinates $q_i$, the equations are:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = 0 \quad \text{for each } i$$

---

## 2. Symmetries and Conservation Laws

### Cyclic Coordinates

A coordinate $q_i$ is **cyclic** if $L$ doesn't depend on it explicitly:

$$\frac{\partial L}{\partial q_i} = 0$$

Then the Euler-Lagrange equation gives:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) = 0$$

The quantity $p_i = \frac{\partial L}{\partial \dot{q}_i}$ (called the **conjugate momentum**) is conserved!

### Noether's Theorem

**Every continuous symmetry of the Lagrangian corresponds to a conserved quantity.**

| Symmetry | Conserved Quantity |
|----------|-------------------|
| Time translation | Energy |
| Space translation | Momentum |
| Rotation | Angular momentum |
| Phase rotation (complex fields) | Charge |

### How It Works

If $L$ is invariant under $q \to q + \epsilon \delta q$ (for small $\epsilon$), then there's a conserved **Noether current**.

For a simple case: if $\delta L = 0$ under the transformation, the conserved quantity is:

$$Q = \frac{\partial L}{\partial \dot{q}} \delta q$$

### QFT Preview

In field theory, Noether's theorem gives **conserved currents** $j^\mu$:

$$\partial_\mu j^\mu = 0$$

The conserved **charge** is $Q = \int j^0 \, d^3x$.

---

## 3. The Hamiltonian Formulation

### The Legendre Transform

The Hamiltonian formulation uses position $q$ and momentum $p$ (not velocity $\dot{q}$).

**Conjugate momentum**: $p = \frac{\partial L}{\partial \dot{q}}$

**Hamiltonian**: $H(q, p) = p\dot{q} - L$

(You need to express $\dot{q}$ in terms of $p$ and $q$.)

### Example: Free Particle

- $L = \frac{1}{2}m\dot{q}^2$
- $p = \frac{\partial L}{\partial \dot{q}} = m\dot{q}$, so $\dot{q} = p/m$
- $H = p \cdot \frac{p}{m} - \frac{1}{2}m\left(\frac{p}{m}\right)^2 = \frac{p^2}{m} - \frac{p^2}{2m} = \frac{p^2}{2m}$

The Hamiltonian is the total energy!

### Hamilton's Equations

The equations of motion in Hamiltonian form:

$$\dot{q} = \frac{\partial H}{\partial p}, \quad \dot{p} = -\frac{\partial H}{\partial q}$$

These are first-order (unlike the second-order Euler-Lagrange equation).

---

## 4. Poisson Brackets

### Definition

For any functions $f(q, p)$ and $g(q, p)$, the **Poisson bracket** is:

$$\{f, g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}$$

For multiple coordinates:

$$\{f, g\} = \sum_i \left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)$$

### Fundamental Brackets

$$\{q_i, q_j\} = 0, \quad \{p_i, p_j\} = 0, \quad \{q_i, p_j\} = \delta_{ij}$$

### Time Evolution

Hamilton's equations can be written as:

$$\dot{f} = \{f, H\}$$

for any function $f(q, p)$.

### Connection to Quantum Mechanics

The **quantization rule**:

$$\{f, g\}_\text{classical} \to \frac{1}{i\hbar}[\hat{f}, \hat{g}]_\text{quantum}$$

So $\{q, p\} = 1$ becomes $[\hat{q}, \hat{p}] = i\hbar$.

---

## 5. From Particles to Fields

### The Continuum Limit

Imagine a chain of masses connected by springs. As the spacing goes to zero:

- Discrete positions $q_n(t)$ → Continuous field $\phi(x, t)$
- Sum over $n$ → Integral over $x$
- Lagrangian $L$ → Lagrangian density $\mathcal{L}$

### Field Theory Lagrangian

For a classical field $\phi(x, t)$:

$$S = \int d^4x \, \mathcal{L}(\phi, \partial_\mu \phi)$$

where $d^4x = dt \, d^3x$ and $\partial_\mu = (\partial_t, \nabla)$.

### The Field Euler-Lagrange Equation

$$\partial_\mu \left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}\right) - \frac{\partial \mathcal{L}}{\partial \phi} = 0$$

### Example: Klein-Gordon Lagrangian

$$\mathcal{L} = \frac{1}{2}(\partial_\mu \phi)(\partial^\mu \phi) - \frac{1}{2}m^2\phi^2$$

Working out the Euler-Lagrange equation gives:

$$(\partial_\mu \partial^\mu + m^2)\phi = 0$$

or in components: $(\partial_t^2 - \nabla^2 + m^2)\phi = 0$ (the **Klein-Gordon equation**).

### Field Hamiltonian

Define conjugate momentum density:

$$\pi(x) = \frac{\partial \mathcal{L}}{\partial \dot{\phi}}$$

Hamiltonian density:

$$\mathcal{H} = \pi \dot{\phi} - \mathcal{L}$$

Total Hamiltonian:

$$H = \int d^3x \, \mathcal{H}$$

---

## 6. Noether's Theorem for Fields

### Spacetime Symmetries

| Symmetry | Conserved Current | Conserved Charge |
|----------|------------------|------------------|
| Time translation | $T^{0\nu}$ (energy-momentum tensor) | Energy $E$ |
| Space translation | $T^{i\nu}$ | Momentum $P^i$ |
| Lorentz boost | $M^{\mu\nu\rho}$ | Boost generators |

### Internal Symmetries

For a complex field $\phi \to e^{i\alpha}\phi$ (global U(1) symmetry):

$$j^\mu = i(\phi^* \partial^\mu \phi - \phi \partial^\mu \phi^*)$$

Conserved charge: $Q = \int d^3x \, j^0$

This is **electric charge** in QED!

---

## Self-Test Questions

1. **Euler-Lagrange**: For $L = \frac{1}{2}m\dot{x}^2 - \frac{1}{2}kx^2$, find the equation of motion.
   <details><summary>Answer</summary>$m\ddot{x} + kx = 0$ (simple harmonic oscillator)</details>

2. **Hamiltonian**: For the above $L$, find $H(x, p)$.
   <details><summary>Answer</summary>$p = m\dot{x}$, so $H = \frac{p^2}{2m} + \frac{1}{2}kx^2$</details>

3. **Poisson bracket**: Compute $\{x^2, p\}$.
   <details><summary>Answer</summary>$\{x^2, p\} = 2x\{x, p\} = 2x$</details>

4. **Noether**: If $L$ doesn't depend on time explicitly, what's conserved?
   <details><summary>Answer</summary>Energy (the Hamiltonian $H$)</details>

5. **Field equation**: For $\mathcal{L} = \frac{1}{2}\dot{\phi}^2 - \frac{1}{2}(\nabla\phi)^2$, find the field equation.
   <details><summary>Answer</summary>$\ddot{\phi} - \nabla^2\phi = 0$ (wave equation)</details>

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Euler-Lagrange | $\frac{d}{dt}\frac{\partial L}{\partial \dot{q}} = \frac{\partial L}{\partial q}$ |
| Conjugate momentum | $p = \frac{\partial L}{\partial \dot{q}}$ |
| Hamiltonian | $H = p\dot{q} - L$ |
| Hamilton's equations | $\dot{q} = \frac{\partial H}{\partial p}$, $\dot{p} = -\frac{\partial H}{\partial q}$ |
| Poisson bracket | $\{f, g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}$ |
| Canonical bracket | $\{q, p\} = 1$ |
| Field momentum | $\pi = \frac{\partial \mathcal{L}}{\partial \dot{\phi}}$ |
| Field E-L | $\partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} = \frac{\partial \mathcal{L}}{\partial \phi}$ |

---

**Next**: [../week_01_ps01/README.md](../week_01_ps01/README.md) — Start Problem Set 1
