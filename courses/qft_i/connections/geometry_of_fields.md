# Connections: The Geometry of Fields

*How QFT connects to your GR/QIT background*

---

## Overview

You've spent time with Witten's course on GR and quantum information. That background gives you a unique perspective on QFT — you already think geometrically. This document maps the connections.

---

## 1. Field Configurations as Geometry

### In GR

The dynamical variable is the metric $g_{\mu\nu}(x)$ — a tensor field on spacetime. The action is:

$$S[g] = \int d^4x \sqrt{-g} \, R$$

where $R$ is the Ricci scalar (curvature).

### In QFT

The dynamical variable is a field $\phi(x)$ — also defined at every spacetime point. The action is:

$$S[\phi] = \int d^4x \, \mathcal{L}(\phi, \partial\phi)$$

**The parallel**: Both are functionals on a space of field configurations. The path integral sums over all configurations:

- GR: $\int \mathcal{D}g \, e^{iS[g]}$
- QFT: $\int \mathcal{D}\phi \, e^{iS[\phi]}$

### The Configuration Space

The space of all field configurations is infinite-dimensional. This is where geometry enters:

- **DeWitt metric**: Defines distances between field configurations
- **Field space curvature**: Affects the measure in the path integral
- **Geodesics**: Extremize the action (classical solutions)

---

## 2. Propagators and Geodesics

### In GR

Particles follow geodesics — paths that extremize proper time:

$$\delta \int ds = 0$$

The geodesic equation:

$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\nu\rho} \frac{dx^\nu}{d\tau}\frac{dx^\rho}{d\tau} = 0$$

### In QFT

The **propagator** $G(x, y)$ gives the amplitude for a particle to travel from $y$ to $x$:

$$G(x, y) = \langle 0 | T\phi(x)\phi(y) | 0 \rangle$$

For a free field, this is a Green's function:

$$(\Box + m^2)G(x, y) = -i\delta^4(x - y)$$

**The connection**: In the classical limit, the propagator is dominated by the classical path — the geodesic in field space.

### The Heat Kernel

There's a deep connection via the heat kernel:

$$K(x, y; s) = \langle x | e^{-s\hat{H}} | y \rangle$$

This "diffuses" from $y$ to $x$. For small $s$, it's concentrated on geodesics. The QFT propagator is an analytic continuation of this.

---

## 3. Stress-Energy and Geometry

### In GR

The stress-energy tensor $T_{\mu\nu}$ sources curvature via Einstein's equations:

$$G_{\mu\nu} = 8\pi G \, T_{\mu\nu}$$

### In QFT

The stress-energy tensor $T^{\mu\nu}$ comes from Noether's theorem applied to spacetime translations:

$$T^{\mu\nu} = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)}\partial^\nu \phi - \eta^{\mu\nu}\mathcal{L}$$

**The connection**: When you put QFT on curved spacetime, this $T_{\mu\nu}$ becomes the source for gravity. This is the **semiclassical approximation**:

$$G_{\mu\nu} = 8\pi G \, \langle T_{\mu\nu} \rangle_\text{QFT}$$

---

## 4. Gauge Theory = Geometry

### Electromagnetism as Geometry

The electromagnetic potential $A_\mu$ is a **connection** on a U(1) fiber bundle. The field strength:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

is the **curvature** of this connection.

**Gauge transformations**: $A_\mu \to A_\mu + \partial_\mu \alpha$ are like coordinate changes on the fiber.

### Comparison with GR

| GR | Electromagnetism |
|----|-----------------|
| Metric $g_{\mu\nu}$ | Potential $A_\mu$ |
| Christoffel $\Gamma^\mu_{\nu\rho}$ | $A_\mu$ (connection) |
| Riemann $R^\mu{}_{\nu\rho\sigma}$ | $F_{\mu\nu}$ (curvature) |
| Diffeomorphisms | Gauge transformations |

### Yang-Mills Theory

Non-abelian gauge theories (like QCD) make this even more explicit. The connection takes values in a Lie algebra:

$$A_\mu = A_\mu^a T^a$$

and the curvature is:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]$$

The non-abelian structure parallels non-abelian holonomy in GR.

---

## 5. Entanglement and QFT

### From Witten's Course

You learned that entanglement entropy in a QFT is related to bulk geometry via **Ryu-Takayanagi**:

$$S_A = \frac{\text{Area}(\gamma_A)}{4G_N}$$

where $\gamma_A$ is the minimal surface in the bulk anchored on the boundary of region $A$.

### What This Course Teaches

To actually *compute* entanglement entropy in a QFT, you need the tools from this course:

1. **Reduced density matrix**: $\rho_A = \text{Tr}_{\bar{A}} |0\rangle\langle 0|$
2. **Replica trick**: Compute $\text{Tr}(\rho_A^n)$ and analytically continue
3. **Correlation functions**: These determine entanglement structure

### The Vacuum Entanglement

The QFT vacuum is **highly entangled** across regions. For a free scalar field:

$$S_A \sim \frac{\text{Area}(\partial A)}{\epsilon^2}$$

This "area law" is exactly what Ryu-Takayanagi predicts! The boundary QFT entanglement matches the bulk geometry.

---

## 6. Information Geometry

### The Fisher Metric

Given a family of probability distributions $p(x|\theta)$, the **Fisher information metric** is:

$$g_{ij}(\theta) = \int p(x|\theta) \frac{\partial \log p}{\partial \theta^i} \frac{\partial \log p}{\partial \theta^j} dx$$

This makes the space of distributions into a Riemannian manifold.

### In QFT

For quantum states, there's an analogous **quantum Fisher metric** (Fubini-Study metric). The space of states has geometry.

The correlation functions you compute in QFT determine this geometry:

- Two-point function → Metric on field space
- Higher correlations → Curvature, connections

### Clinical Trajectories Connection

If you model patient state evolution as a path through some state space:

- The state at time $t$ is like a field configuration
- Evolution is like field dynamics
- Correlation functions encode how states at different times relate

---

## 7. Synthesis

### What You Already Know

From Witten's course:
- Geometry encodes physics (metrics, curvature)
- Variational principles (action extremization)
- Tensors and index notation
- The holographic principle (boundary/bulk duality)

### What This Course Adds

- How to **quantize** fields (not just write classical equations)
- **Particles** as excitations of quantum fields
- **Interactions** via Feynman diagrams
- The boundary theory in AdS/CFT is a **quantum field theory**

### The Complete Picture

```
Classical Mechanics → Quantum Mechanics
       ↓                    ↓
Classical Field Theory → Quantum Field Theory
       ↓                    ↓
  General Relativity → Quantum Gravity (?)
                           ↓
                    AdS/CFT (bulk GR ↔ boundary CFT)
```

You're filling in "Quantum Field Theory" — the language of the boundary in AdS/CFT.

---

## Reading Suggestions

If you want to explore these connections more:

1. **Wald, "Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics"** — QFT on curved backgrounds

2. **Birrell & Davies, "Quantum Fields in Curved Space"** — Technical treatment

3. **Carroll, "Spacetime and Geometry"** — GR with an eye toward QFT

4. **Nakahara, "Geometry, Topology and Physics"** — Gauge theory as fiber bundles

5. **Rangamani & Takayanagi, "Holographic Entanglement Entropy"** — The Ryu-Takayanagi formula in depth

---

**Next**: Back to the course material — [../week_01_ps01/README.md](../week_01_ps01/README.md)
