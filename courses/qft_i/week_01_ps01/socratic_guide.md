# Week 1 Socratic Guide

*Self-test questions to check your understanding*

---

## How to Use This Guide

1. **Close all notes and books**
2. Try to answer each question from memory
3. Write your answer, then check
4. Note which topics need review

The goal is **active recall** — this strengthens memory far more than passive re-reading.

---

## Part 1: The Big Picture

### Q1: Why Fields?

Why do we need field theory instead of just multi-particle quantum mechanics?

*Think about this before revealing the answer.*

<details>
<summary>Answer</summary>

Several reasons:

1. **Relativistic QM allows particle creation/destruction**: $E = mc^2$ means energy can convert to mass. A fixed-particle-number theory can't handle this.

2. **Causality requires locality**: In relativity, nothing travels faster than light. Action-at-a-distance violates this. Fields mediate interactions locally.

3. **The cluster decomposition principle**: Experiments far apart should be independent. Field theories naturally satisfy this.

4. **Antiparticles are required**: The Klein-Gordon and Dirac equations predict negative energy solutions. Reinterpreting these as antiparticles requires a many-particle (field) framework.
</details>

### Q2: What is Locality?

What does it mean for a Lagrangian to be "local"?

<details>
<summary>Answer</summary>

A Lagrangian density $\mathcal{L}(x)$ is local if it depends only on fields and their derivatives **at the same spacetime point** $x$:

$$\mathcal{L} = \mathcal{L}(\phi(x), \partial_\mu\phi(x))$$

Not allowed: $\mathcal{L} \sim \phi(x)\phi(y)$ for $x \neq y$ (action at a distance).

Also restricted: Higher derivatives like $\partial_\mu\partial_\nu\partial_\rho\phi$ typically lead to problems (Ostrogradsky instability).
</details>

---

## Part 2: Lagrangian Mechanics for Fields

### Q3: The Action

Write the action for a scalar field theory in terms of the Lagrangian density.

<details>
<summary>Answer</summary>

$$S[\phi] = \int d^4x \, \mathcal{L}(\phi, \partial_\mu\phi)$$

where $d^4x = dt \, d^3\vec{x}$ and the integral is over all spacetime (or a bounded region).
</details>

### Q4: Euler-Lagrange Equation

State the field Euler-Lagrange equation.

<details>
<summary>Answer</summary>

$$\partial_\mu \left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\right) - \frac{\partial \mathcal{L}}{\partial \phi} = 0$$

This is the condition for the action to be stationary: $\delta S = 0$.
</details>

### Q5: Klein-Gordon Derivation

From $\mathcal{L} = \frac{1}{2}(\partial_\mu\phi)(\partial^\mu\phi) - \frac{1}{2}m^2\phi^2$, derive the equation of motion.

<details>
<summary>Answer</summary>

Step 1: Compute $\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}$

Since $(\partial_\mu\phi)(\partial^\mu\phi) = \eta^{\mu\nu}(\partial_\mu\phi)(\partial_\nu\phi)$, we get:
$$\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)} = \partial^\mu\phi$$

Step 2: Compute $\frac{\partial \mathcal{L}}{\partial\phi}$
$$\frac{\partial \mathcal{L}}{\partial\phi} = -m^2\phi$$

Step 3: Apply Euler-Lagrange
$$\partial_\mu(\partial^\mu\phi) + m^2\phi = 0$$
$$(\Box + m^2)\phi = 0$$

where $\Box = \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2$.
</details>

### Q6: Conjugate Momentum

For the Klein-Gordon field, what is the conjugate momentum $\pi(x)$?

<details>
<summary>Answer</summary>

$$\pi = \frac{\partial \mathcal{L}}{\partial \dot{\phi}} = \dot{\phi}$$

The "velocity" $\dot{\phi}$ is the conjugate momentum — simple for this theory!
</details>

### Q7: Hamiltonian Density

Write the Hamiltonian density for the Klein-Gordon field in terms of $\phi$, $\pi$, and $\nabla\phi$.

<details>
<summary>Answer</summary>

$$\mathcal{H} = \pi\dot{\phi} - \mathcal{L}$$

Since $\pi = \dot{\phi}$:
$$\mathcal{H} = \dot{\phi}^2 - \frac{1}{2}\dot{\phi}^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2$$
$$= \frac{1}{2}\pi^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2$$

This is the energy density — note it's positive definite.
</details>

---

## Part 3: Noether's Theorem

### Q8: Statement of Noether's Theorem

State Noether's theorem in one sentence.

<details>
<summary>Answer</summary>

**Every continuous symmetry of the action corresponds to a conserved current (and therefore a conserved charge).**

Mathematically: If $\delta S = 0$ under $\phi \to \phi + \epsilon\,\delta\phi$, then there exists $j^\mu$ with $\partial_\mu j^\mu = 0$.
</details>

### Q9: Conserved Charge

If $\partial_\mu j^\mu = 0$, what is the conserved charge and why is it conserved?

<details>
<summary>Answer</summary>

The conserved charge is:
$$Q = \int d^3x \, j^0$$

To see conservation, integrate $\partial_\mu j^\mu = 0$ over all space:
$$\frac{\partial}{\partial t}\int d^3x \, j^0 + \int d^3x \, \nabla \cdot \vec{j} = 0$$

Assuming $\vec{j} \to 0$ at spatial infinity (fields fall off), the second term vanishes by Gauss's theorem:
$$\frac{dQ}{dt} = 0$$
</details>

### Q10: Translation Invariance

What conserved quantity arises from time translation invariance?

<details>
<summary>Answer</summary>

**Energy.**

Time translation: $x^0 \to x^0 + \epsilon$, $\phi(x) \to \phi(x) - \epsilon\partial_0\phi$.

The conserved current is $j^\mu = T^{\mu 0}$, the first column of the stress-energy tensor.

The conserved charge is:
$$H = \int d^3x \, T^{00} = \int d^3x \, \mathcal{H}$$

This is the total energy (Hamiltonian).
</details>

### Q11: The Stress-Energy Tensor

Write the formula for the (canonical) stress-energy tensor $T^{\mu\nu}$.

<details>
<summary>Answer</summary>

$$T^{\mu\nu} = \frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\partial^\nu\phi - \eta^{\mu\nu}\mathcal{L}$$

For multiple fields $\phi_a$:
$$T^{\mu\nu} = \sum_a \frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi_a)}\partial^\nu\phi_a - \eta^{\mu\nu}\mathcal{L}$$
</details>

### Q12: Internal Symmetry Example

For a complex scalar field $\phi$, what is the Noether current for the U(1) symmetry $\phi \to e^{i\alpha}\phi$?

<details>
<summary>Answer</summary>

The infinitesimal transformation is $\delta\phi = i\epsilon\phi$, $\delta\phi^* = -i\epsilon\phi^*$.

The Noether current is:
$$j^\mu = i\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\phi - \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^*)}\phi^*\right)$$

For $\mathcal{L} = (\partial_\mu\phi^*)(\partial^\mu\phi) - m^2|\phi|^2$:
$$j^\mu = i(\phi^*\partial^\mu\phi - \phi\partial^\mu\phi^*)$$

The conserved charge $Q = \int d^3x \, j^0$ is interpreted as **electric charge** (or particle number).
</details>

---

## Part 4: Calculations

### Q13: Compute $T^{00}$ for Klein-Gordon

Calculate the energy density $T^{00}$ for the Klein-Gordon field.

<details>
<summary>Answer</summary>

Using $T^{\mu\nu} = (\partial^\mu\phi)(\partial^\nu\phi) - \eta^{\mu\nu}\mathcal{L}$:

$$T^{00} = (\partial^0\phi)(\partial^0\phi) - \eta^{00}\mathcal{L}$$
$$= \dot{\phi}^2 - \mathcal{L}$$
$$= \dot{\phi}^2 - \frac{1}{2}\dot{\phi}^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2$$
$$= \frac{1}{2}\dot{\phi}^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2$$

This is exactly the Hamiltonian density $\mathcal{H}$.
</details>

### Q14: Index Gymnastics

Simplify: $\eta^{\mu\nu}\partial_\mu\partial_\nu$

<details>
<summary>Answer</summary>

$$\eta^{\mu\nu}\partial_\mu\partial_\nu = \eta^{00}\partial_0\partial_0 + \eta^{11}\partial_1\partial_1 + \eta^{22}\partial_2\partial_2 + \eta^{33}\partial_3\partial_3$$

With $\eta = \text{diag}(1, -1, -1, -1)$:
$$= \partial_t^2 - \partial_x^2 - \partial_y^2 - \partial_z^2 = \partial_t^2 - \nabla^2 = \Box$$

This is the d'Alembertian (wave operator).
</details>

### Q15: Verify Conservation

Show that $\partial_\mu T^{\mu\nu} = 0$ for the Klein-Gordon field (using the equation of motion).

<details>
<summary>Answer</summary>

$T^{\mu\nu} = (\partial^\mu\phi)(\partial^\nu\phi) - \eta^{\mu\nu}\mathcal{L}$

Taking $\partial_\mu$:
$$\partial_\mu T^{\mu\nu} = (\partial_\mu\partial^\mu\phi)(\partial^\nu\phi) + (\partial^\mu\phi)(\partial_\mu\partial^\nu\phi) - \partial^\nu\mathcal{L}$$

The first term: $\partial_\mu\partial^\mu\phi = \Box\phi = -m^2\phi$ (by equation of motion).

The second term: $(\partial^\mu\phi)(\partial_\mu\partial^\nu\phi) = \frac{1}{2}\partial^\nu[(\partial_\mu\phi)(\partial^\mu\phi)]$

Computing $\partial^\nu\mathcal{L}$:
$$\partial^\nu\mathcal{L} = \frac{\partial\mathcal{L}}{\partial\phi}\partial^\nu\phi + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\partial^\nu\partial_\mu\phi$$
$$= -m^2\phi\partial^\nu\phi + (\partial^\mu\phi)(\partial^\nu\partial_\mu\phi)$$
$$= -m^2\phi\partial^\nu\phi + \frac{1}{2}\partial^\nu[(\partial_\mu\phi)(\partial^\mu\phi)]$$

Putting it together:
$$\partial_\mu T^{\mu\nu} = -m^2\phi\partial^\nu\phi + \frac{1}{2}\partial^\nu[(\partial\phi)^2] + m^2\phi\partial^\nu\phi - \frac{1}{2}\partial^\nu[(\partial\phi)^2] = 0$$

</details>

---

## Summary: How Did You Do?

| Section | Questions | Confident? |
|---------|-----------|------------|
| Big Picture | Q1-2 | [ ] |
| Lagrangian Mechanics | Q3-7 | [ ] |
| Noether's Theorem | Q8-12 | [ ] |
| Calculations | Q13-15 | [ ] |

**If all confident**: Move on to the problem set!

**If some gaps**: Re-read the relevant sections of P&S or Tong.

---

**Next**: Attempt the problem set in [ps01_attempt.md](./ps01_attempt.md) (don't look at solutions yet!)
