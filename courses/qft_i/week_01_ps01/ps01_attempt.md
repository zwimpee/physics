# Problem Set 1: Your Attempt

*Work through the problems before looking at solutions*

**Problem Set PDF**: [mit8_323_s23_pset01.pdf](../../8.323-spring-2023/static_resources/mit8_323_s23_pset01.pdf)

---

## Instructions

1. Work through each problem below
2. Show your work — partial credit for partial understanding
3. **Do not look at the solutions until you've made a genuine attempt**

---

## Problem 1: Review — Quantum Harmonic Oscillator in the Heisenberg Picture (25 points)

Consider the Hamiltonian for a unit mass harmonic oscillator with frequency $\omega$:

$$H = \frac{1}{2}(\hat{p}^2 + \omega^2 \hat{x}^2)$$

In the Heisenberg picture, $\hat{p}(t)$ and $\hat{x}(t)$ are dynamical variables which evolve with time. They obey the equal-time commutation relation:

$$[\hat{x}(t), \hat{p}(t)] = i$$

Here and below we set $\hbar = 1$.

### (a) 
Obtain the Heisenberg evolution equations for $\hat{x}(t)$ and $\hat{p}(t)$.

**Your Work:**



---

### (b)
Suppose the initial conditions at $t = 0$ are given by

$$\hat{x}(0) = \hat{x}, \quad \hat{p}(0) = \hat{p}$$

Find $\hat{x}(t)$ and $\hat{p}(t)$.

**Your Work:**



---

### (c)
It is convenient to introduce operators $\hat{a}(t)$ and $\hat{a}^\dagger(t)$ defined by

$$\hat{x}(t) = \frac{1}{\sqrt{2\omega}}(\hat{a}(t) + \hat{a}^\dagger(t)), \quad \hat{p}(t) = -i\sqrt{\frac{\omega}{2}}(\hat{a}(t) - \hat{a}^\dagger(t))$$

Show that $\hat{a}(t)$ and $\hat{a}^\dagger(t)$ satisfy the equal-time commutation relation:

$$[\hat{a}(t), \hat{a}^\dagger(t)] = 1$$

**Your Work:**



---

### (d)
Express the Hamiltonian in terms of $\hat{a}(t)$ and $\hat{a}^\dagger(t)$.

**Your Work:**



---

### (e)
Obtain the Heisenberg equations for $\hat{a}(t)$ and $\hat{a}^\dagger(t)$.

**Your Work:**



---

### (f)
Suppose the initial conditions at $t = 0$ are given by

$$\hat{a}(0) = \hat{a}, \quad \hat{a}^\dagger(0) = \hat{a}^\dagger$$

Find $\hat{a}(t)$ and $\hat{a}^\dagger(t)$.

**Your Work:**



---

### (g)
Express $\hat{x}(t)$, $\hat{p}(t)$ and the Hamiltonian $H$ in terms of $\hat{a}$ and $\hat{a}^\dagger$.

**Your Work:**



---

## Problem 2: Review — Lorentz Transformations (15 points)

### (a)
Prove that the four-dimensional $\delta$-function

$$\delta^{(4)}(p) = \delta(p^0)\delta(p^1)\delta(p^2)\delta(p^3)$$

is Lorentz invariant, i.e.,

$$\delta^{(4)}(p) = \delta^{(4)}(\tilde{p})$$

where $\tilde{p}^\mu$ is a Lorentz transformation of $p$.

**Your Work:**



---

### (b)
Show that

$$\omega_1 \delta^{(3)}(\vec{k}_1 - \vec{k}_2)$$

is Lorentz invariant, i.e.,

$$\omega_1 \delta^{(3)}(\vec{k}_1 - \vec{k}_2) = \omega_1' \delta^{(3)}(\vec{k}_1' - \vec{k}_2')$$

where $\vec{k}_1$ and $\vec{k}_2$ are respectively the spatial parts of four-vectors $k_1^\mu = (\omega_1, \vec{k}_1)$ and $k_2^\mu = (\omega_2, \vec{k}_2)$ which satisfy the on-shell condition:

$$k_1^2 = k_2^2 = -m^2$$

and $k_1'^\mu = (\omega_1', \vec{k}_1')$ and $k_2'^\mu = (\omega_2', \vec{k}_2')$ are related to $k_1^\mu$, $k_2^\mu$ by the same Lorentz transformation.

**Your Work:**



---

### (c)
For any function $f(k) = f(k^0, k^1, k^2, k^3)$, prove that

$$\int \frac{d^3\vec{k}}{(2\pi)^3} \frac{1}{2\omega_{\vec{k}}} f(k), \quad \omega_{\vec{k}} = \sqrt{\vec{k}^2 + m^2}$$

is Lorentz invariant in the sense that

$$\int \frac{d^3\vec{k}}{(2\pi)^3} \frac{1}{2\omega_{\vec{k}}} f(k) = \int \frac{d^3\vec{k}}{(2\pi)^3} \frac{1}{2\omega_{\vec{k}}} f(\tilde{k})$$

where $\tilde{k}^\mu = \Lambda^\mu_{\ \nu} k^\nu$ is a Lorentz transformation of $k^\mu$.

**Your Work:**



---

## Problem 3: A Complex Scalar Field (20 points)

Consider the field theory of a complex-valued scalar field $\phi(x)$ with action:

$$S = \int d^4x \left[ -\partial_\mu \phi^* \partial^\mu \phi - V(|\phi|^2) \right], \quad |\phi|^2 = \phi \phi^*$$

One could either consider the real and imaginary parts of $\phi$, or $\phi$ and $\phi^*$ as independent dynamical variables. The latter is more convenient in most situations.

### (a)
Check that the action is Lorentz invariant and find the equations of motion.

**Your Work:**



---

### (b)
Find the canonical conjugate momenta for $\phi$ and $\phi^*$, and the Hamiltonian $H$.

**Your Work:**



---

### (c)
The action is invariant under the transformation

$$\phi \to e^{i\alpha}\phi, \quad \phi^* \to e^{-i\alpha}\phi^*$$

for arbitrary constant $\alpha$. When $\alpha$ is small, i.e., for an infinitesimal transformation:

$$\delta\phi = i\alpha\phi, \quad \delta\phi^* = -i\alpha\phi^*$$

Use Noether's theorem to find the corresponding conserved current $j^\mu$ and conserved charge $Q$.

**Your Work:**



---

### (d)
Use the equations of motion from part (a) to verify directly that $j^\mu$ is indeed conserved.

**Your Work:**



---

## Problem 4: The Energy-Momentum Tensor for the Complex Scalar Field (20 points)

In this problem we work out the energy-momentum tensor of the complex scalar theory from Problem 3.

### (a)
Under a spacetime translation

$$x^\mu \to x'^\mu = x^\mu + a^\mu$$

a scalar field transforms as

$$\phi'(x') = \phi(x)$$

Show that the action is invariant under the transformation $\phi(x) \to \phi'(x)$.

**Your Work:**



---

### (b)
Write down the transformation of the scalar fields $\phi$ and $\phi^*$ for an infinitesimal translation, and use Noether's theorem to find the corresponding conserved currents $T^{\mu\nu}$.

**Your Work:**



---

### (c)
The conserved charge for a time translation

$$H = \int d^3x \, T^{00}$$

should be identified with the total energy of the system, while that for a spatial translation

$$P^i = \int d^3x \, T^{0i}$$

should be identified with the total momentum. Thus $T^{\mu\nu}$ is referred to as the energy-momentum tensor.

Write down the explicit expressions for $H$ and $P^i$. Compare $H$ obtained here with the Hamiltonian of Problem 3(b).

**Your Work:**



---

### (d)
Use the equations of motion from Problem 3(a) to verify directly that $T^{\mu\nu}$ is indeed conserved.

**Your Work:**



---

## Self-Assessment

Before checking solutions, rate your confidence:

| Problem | Confidence (1-5) | Time Spent | Notes |
|---------|-----------------|------------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

---

## Stuck Points

List any places where you got stuck. These are learning opportunities:

1. 
2. 
3. 

---

**Next**: Compare with [mit8_323_s23_pset_01sol.pdf](../../8.323-spring-2023/static_resources/mit8_323_s23_pset_01sol.pdf), then write up in [ps01_solutions.md](./ps01_solutions.md)
