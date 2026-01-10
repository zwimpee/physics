# Quantum Mechanics Review for QFT

*The key concepts you need before quantizing fields*

---

## Overview

QFT is "second quantization" — we quantize classical fields just like we quantized classical mechanics. The patterns you know from QM will reappear at a higher level:

| QM Concept | QFT Analog |
|------------|------------|
| Wave function $\psi(x)$ | Field operator $\hat{\phi}(x)$ |
| $[\hat{x}, \hat{p}] = i\hbar$ | $[\hat{\phi}(x), \hat{\pi}(y)] = i\hbar\delta(x-y)$ |
| Harmonic oscillator $a, a^\dagger$ | Mode operators $a_k, a_k^\dagger$ for each momentum |
| Energy eigenstates $|n\rangle$ | Particle number states $|n_k\rangle$ |
| Ground state $|0\rangle$ | Vacuum $|0\rangle$ (no particles) |

---

## 1. The Quantum Framework

### States and Operators

**State**: A vector $|\psi\rangle$ in a Hilbert space $\mathcal{H}$.

**Observable**: A Hermitian operator $\hat{O}$ acting on $\mathcal{H}$.

**Measurement**: Yields eigenvalues of $\hat{O}$. After measuring eigenvalue $o$, state collapses to $|o\rangle$.

**Expectation value**: $\langle O \rangle = \langle \psi | \hat{O} | \psi \rangle$

### The Canonical Commutation Relations

The fundamental relation between position and momentum:

$$[\hat{x}, \hat{p}] = i\hbar$$

This is the **quantization condition**. In classical mechanics, $\{x, p\} = 1$. The rule is:

$$\text{Quantization: } \{,\} \to \frac{1}{i\hbar}[,]$$

This same pattern will quantize fields.

### Schrödinger vs. Heisenberg Pictures

**Schrödinger picture**: States evolve, operators fixed.
$$i\hbar \frac{d}{dt}|\psi(t)\rangle = H|\psi(t)\rangle$$

**Heisenberg picture**: Operators evolve, states fixed.
$$\frac{d\hat{O}}{dt} = \frac{1}{i\hbar}[\hat{O}, H]$$

In QFT, we mostly use the **Heisenberg picture** — fields are operators that depend on spacetime: $\hat{\phi}(x, t)$.

---

## 2. The Harmonic Oscillator

### Why This Matters

The harmonic oscillator is the **prototype for QFT**. A free quantum field is an infinite collection of independent harmonic oscillators, one for each momentum mode.

### The Setup

Hamiltonian: $H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2$

Define creation/annihilation operators:

$$a = \sqrt{\frac{m\omega}{2\hbar}}\left(x + \frac{ip}{m\omega}\right), \quad a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(x - \frac{ip}{m\omega}\right)$$

### Key Relations

**Commutator**: $[a, a^\dagger] = 1$

**Hamiltonian**: $H = \hbar\omega\left(a^\dagger a + \frac{1}{2}\right)$

**Number operator**: $N = a^\dagger a$ counts excitation level

### Action on States

$$a|n\rangle = \sqrt{n}|n-1\rangle \quad \text{(annihilation)}$$
$$a^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle \quad \text{(creation)}$$

**Ground state**: $a|0\rangle = 0$ (nothing to annihilate)

**Excited states**: $|n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}}|0\rangle$

**Energy spectrum**: $E_n = \hbar\omega(n + \frac{1}{2})$

### QFT Preview

In QFT:
- Each momentum mode $\vec{k}$ has its own oscillator with operators $a_{\vec{k}}, a_{\vec{k}}^\dagger$
- $a_{\vec{k}}^\dagger$ creates a particle with momentum $\vec{k}$
- $a_{\vec{k}}$ destroys a particle with momentum $\vec{k}$
- The vacuum $|0\rangle$ is the ground state of ALL oscillators

---

## 3. Angular Momentum and Spin

### Why This Matters

Fermions (like electrons) have spin. The Dirac equation describes spin-1/2 particles. You need to be comfortable with:
- Pauli matrices
- Spin states $|\uparrow\rangle$, $|\downarrow\rangle$
- Spinor representations

### Angular Momentum Algebra

The generators of rotations satisfy:

$$[J_i, J_j] = i\hbar \epsilon_{ijk} J_k$$

Equivalently: $[J_x, J_y] = i\hbar J_z$ (and cyclic permutations).

### Spin-1/2

**Operators**: $S_i = \frac{\hbar}{2}\sigma_i$ where $\sigma_i$ are Pauli matrices:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Key properties**:
- $\sigma_i^2 = I$
- $\sigma_i \sigma_j = i\epsilon_{ijk}\sigma_k$ for $i \neq j$
- $\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$

**States**: 
$$|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

### QFT Preview

The Dirac equation involves **4-component spinors** (two spin states × particle/antiparticle). The gamma matrices $\gamma^\mu$ are 4×4 generalizations of Pauli matrices.

---

## 4. Perturbation Theory

### Why This Matters

Almost all QFT calculations are perturbative. You expand in a small coupling constant (like $e$ in QED) and compute corrections order by order.

### Time-Independent Perturbation Theory

If $H = H_0 + \lambda V$ where $H_0$ has known solutions:

**First-order energy**: $E_n^{(1)} = \langle n^{(0)} | V | n^{(0)} \rangle$

**First-order state**: $|n^{(1)}\rangle = \sum_{m \neq n} \frac{\langle m^{(0)} | V | n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} |m^{(0)}\rangle$

### Time-Dependent Perturbation Theory

For transitions between states due to a time-dependent perturbation:

**Transition amplitude**: 
$$c_{f\to i}(t) = -\frac{i}{\hbar} \int_0^t \langle f | V(t') | i \rangle e^{i\omega_{fi}t'} dt'$$

**Fermi's Golden Rule** (for constant perturbation):
$$\Gamma_{i \to f} = \frac{2\pi}{\hbar}|\langle f | V | i \rangle|^2 \delta(E_f - E_i)$$

### QFT Preview

Feynman diagrams are a systematic way to organize perturbation theory. Each diagram represents a term in the perturbative expansion.

---

## 5. The Heisenberg Picture in Detail

### Evolution of Operators

In the Heisenberg picture, operators carry time dependence:

$$\hat{O}_H(t) = e^{iHt/\hbar} \hat{O}_S e^{-iHt/\hbar}$$

The equation of motion is:

$$\frac{d\hat{O}_H}{dt} = \frac{1}{i\hbar}[\hat{O}_H, H]$$

### For the Harmonic Oscillator

Starting from $[a, H] = \hbar\omega a$, we get:

$$\frac{da}{dt} = \frac{1}{i\hbar}[a, H] = -i\omega a$$

Solution: $a(t) = a(0) e^{-i\omega t}$

And: $a^\dagger(t) = a^\dagger(0) e^{i\omega t}$

### QFT Preview

Field operators evolve in spacetime:
$$\hat{\phi}(x,t) = \int \frac{d^3k}{(2\pi)^3} \frac{1}{\sqrt{2\omega_k}} \left( a_k e^{-ikx} + a_k^\dagger e^{ikx} \right)$$

This is just a sum of harmonic oscillator modes!

---

## 6. Second Quantization Preview

### The Conceptual Leap

| First Quantization | Second Quantization |
|-------------------|---------------------|
| Fixed number of particles | Variable particle number |
| Wave function $\psi(x_1, ..., x_N)$ | Field operator $\hat{\psi}(x)$ |
| $x$ is an operator | $x$ is a label |
| $\psi$ is a function | $\hat{\psi}$ is an operator |

### Why "Second"?

1. **First quantization**: Classical mechanics → Quantum mechanics
   - Position/momentum become operators
   - Wave function is a number (probability amplitude)

2. **Second quantization**: Quantum mechanics → Quantum field theory
   - The field itself becomes an operator
   - Particle number is not fixed

### The Fock Space

Instead of fixed-$N$ Hilbert spaces, we work in **Fock space**:

$$\mathcal{F} = \mathcal{H}_0 \oplus \mathcal{H}_1 \oplus \mathcal{H}_2 \oplus \cdots$$

where $\mathcal{H}_N$ is the $N$-particle Hilbert space.

A general state can be a superposition of different particle numbers!

---

## Self-Test Questions

Before moving on, make sure you can answer these:

1. **Commutators**: Calculate $[a^2, a^\dagger]$ for the harmonic oscillator.
   <details><summary>Answer</summary>$[a^2, a^\dagger] = 2a$</details>

2. **Energy**: What is $\langle 2 | H | 2 \rangle$ for the harmonic oscillator?
   <details><summary>Answer</summary>$\hbar\omega(2 + 1/2) = \frac{5}{2}\hbar\omega$</details>

3. **Spin**: What is $\sigma_x \sigma_y \sigma_z$?
   <details><summary>Answer</summary>$\sigma_x \sigma_y \sigma_z = i I$</details>

4. **Heisenberg**: If $[A, H] = cA$ for constant $c$, what is $A(t)$?
   <details><summary>Answer</summary>$A(t) = A(0) e^{-ict/\hbar}$</details>

---

**Next**: [classical_mechanics_review.md](./classical_mechanics_review.md) — Lagrangians and Hamiltonians
