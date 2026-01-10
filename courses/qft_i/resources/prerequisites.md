# Prerequisites Self-Assessment

*Work through these sections to identify gaps before starting the course*

---

## How to Use This Document

1. For each topic, try to answer the "Can you..." questions
2. Mark your confidence: `[x]` = solid, `[~]` = shaky, `[ ]` = need review
3. For `[ ]` and `[~]` items, see the warmup materials in [week_00_warmup/](../week_00_warmup/)

**Honest self-assessment saves time.** It's better to spend a week on review than to struggle for months with shaky foundations.

---

## Quantum Mechanics

### Core Framework

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Write down the time-dependent and time-independent Schrödinger equations |
| [ ] | Explain what an operator is and how observables correspond to Hermitian operators |
| [ ] | Compute the commutator [A, B] for given operators |
| [ ] | State the uncertainty principle in terms of commutators |
| [ ] | Explain the difference between Schrödinger, Heisenberg, and interaction pictures |

### Quick Check

What is $[\hat{x}, \hat{p}]$?

<details>
<summary>Answer</summary>

$$[\hat{x}, \hat{p}] = i\hbar$$

If this surprised you or you're unsure why, see [qm_review.md](../week_00_warmup/qm_review.md).
</details>

### Harmonic Oscillator

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Write the Hamiltonian for the quantum harmonic oscillator |
| [ ] | Define the creation and annihilation operators $a^\dagger$ and $a$ |
| [ ] | Compute $[a, a^\dagger]$ |
| [ ] | Explain how $a^\dagger$ and $a$ connect energy eigenstates |
| [ ] | State the energy spectrum $E_n$ |

### Quick Check

Given $H = \hbar\omega(a^\dagger a + \frac{1}{2})$, what is $[H, a]$?

<details>
<summary>Answer</summary>

$$[H, a] = -\hbar\omega a$$

This is why $a$ is called the "lowering" or "annihilation" operator — it reduces the energy by $\hbar\omega$.
</details>

### Angular Momentum and Spin

| Confidence | Can you... |
|:----------:|------------|
| [ ] | State the commutation relations $[J_i, J_j] = i\hbar \epsilon_{ijk} J_k$ |
| [ ] | Explain what $J^2$ and $J_z$ eigenvalues mean |
| [ ] | Write the spin-1/2 matrices (Pauli matrices) |
| [ ] | Add angular momenta using Clebsch-Gordan coefficients (at least conceptually) |

### Perturbation Theory

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Set up non-degenerate perturbation theory to first order in energy |
| [ ] | State when you need degenerate perturbation theory |
| [ ] | Explain Fermi's Golden Rule (time-dependent perturbation) |

### Advanced Topics

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Define a density matrix and distinguish pure vs. mixed states |
| [ ] | Compute expectation values using $\text{Tr}(\rho O)$ |
| [ ] | Explain what path integrals are (at least conceptually) |
| [ ] | State what second quantization means (particles as excitations of fields) |

---

## Classical Mechanics

### Lagrangian Mechanics

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Write the Lagrangian $L = T - V$ for a system |
| [ ] | Derive equations of motion from the Euler-Lagrange equations |
| [ ] | Identify cyclic coordinates and their conserved momenta |
| [ ] | Explain the action principle (Hamilton's principle) |

### Quick Check

For a free particle with $L = \frac{1}{2}m\dot{x}^2$, what is the equation of motion?

<details>
<summary>Answer</summary>

The Euler-Lagrange equation gives $m\ddot{x} = 0$, i.e., $\ddot{x} = 0$.
</details>

### Hamiltonian Mechanics

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Perform a Legendre transformation from $L$ to $H$ |
| [ ] | Write Hamilton's equations $\dot{q} = \partial H/\partial p$, $\dot{p} = -\partial H/\partial q$ |
| [ ] | Compute Poisson brackets $\{f, g\}$ |
| [ ] | Explain the connection between Poisson brackets and commutators |

### Quick Check

What is $\{x, p\}$ in classical mechanics?

<details>
<summary>Answer</summary>

$$\{x, p\} = 1$$

And in quantum mechanics, $[\hat{x}, \hat{p}] = i\hbar$. The correspondence is $\{,\} \to \frac{1}{i\hbar}[,]$.
</details>

### Noether's Theorem

| Confidence | Can you... |
|:----------:|------------|
| [ ] | State Noether's theorem (symmetries ↔ conservation laws) |
| [ ] | Give examples: translation → momentum, rotation → angular momentum |
| [ ] | Apply Noether's theorem to a simple Lagrangian |

---

## Special Relativity

### Kinematics

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Write the Minkowski metric $\eta_{\mu\nu}$ and interval $ds^2$ |
| [ ] | Compute the invariant interval between two events |
| [ ] | Explain the difference between timelike, spacelike, and lightlike separations |
| [ ] | Transform coordinates under a Lorentz boost |

### Quick Check

What is the invariant mass of a particle with 4-momentum $p^\mu = (E, \vec{p})$?

<details>
<summary>Answer</summary>

$$m^2 = p_\mu p^\mu = E^2 - |\vec{p}|^2$$

(In natural units where $c = 1$.)
</details>

### 4-Vectors and Tensors

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Distinguish between upper ($V^\mu$) and lower ($V_\mu$) indices |
| [ ] | Raise and lower indices using the metric |
| [ ] | Contract indices to form scalars (e.g., $A_\mu B^\mu$) |
| [ ] | State the Lorentz transformation law for 4-vectors |

### Covariant Formulation

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Write the 4-momentum $p^\mu = (E, \vec{p})$ |
| [ ] | Write the 4-gradient $\partial_\mu = (\partial_t, \nabla)$ |
| [ ] | Explain what "Lorentz invariant" and "Lorentz covariant" mean |

---

## Mathematical Background

### Linear Algebra

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Work with complex vector spaces and inner products |
| [ ] | Diagonalize matrices and find eigenvalues/eigenvectors |
| [ ] | Distinguish Hermitian, unitary, and normal operators |
| [ ] | Use tensor product notation for multi-particle states |

### Complex Analysis

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Evaluate contour integrals using the residue theorem |
| [ ] | Find poles of a function |
| [ ] | Close contours in the upper/lower half-plane |

### Fourier Analysis

| Confidence | Can you... |
|:----------:|------------|
| [ ] | Write the Fourier transform and its inverse |
| [ ] | State the convolution theorem |
| [ ] | Use delta functions and their integral representations |

---

## Summary: How Ready Are You?

Count your confidence levels:

| Category | Solid [x] | Shaky [~] | Need Review [ ] |
|----------|-----------|-----------|-----------------|
| Quantum Mechanics | | | |
| Classical Mechanics | | | |
| Special Relativity | | | |
| Mathematical Background | | | |

### Recommendations

- **Mostly [x]**: Go directly to [week_01_ps01/](../week_01_ps01/). You're ready.
- **Some [~]**: Skim [week_00_warmup/](../week_00_warmup/) for the shaky topics, then start Week 1.
- **Many [ ]**: Work through [week_00_warmup/](../week_00_warmup/) carefully. Consider supplementing with:
  - Griffiths, *Introduction to Quantum Mechanics* (Ch. 1-4)
  - Goldstein, *Classical Mechanics* (Ch. 1-2, 8-9)
  - Jackson, *Classical Electrodynamics* (Ch. 11 for SR)

---

**Next**: 
- If ready: [../week_01_ps01/README.md](../week_01_ps01/README.md)
- If not: [../week_00_warmup/qm_review.md](../week_00_warmup/qm_review.md)
