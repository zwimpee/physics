# Problem 2: Extended Notes on Causal Curves and Compactness

## Background: Globally Hyperbolic Spacetimes

A spacetime $(M, g)$ is **globally hyperbolic** if:
1. It contains no closed causal curves
2. For any two points $p, q \in M$, the set $J^+(p) \cap J^-(q)$ is compact

Equivalently (by a theorem of Geroch), $M$ is globally hyperbolic if and only if it admits a Cauchy surface $S$.

### Cauchy Surface

A spacelike hypersurface $S \subset M$ is a **Cauchy surface** if every inextendible causal curve in $M$ intersects $S$ exactly once.

## The Space of Causal Curves

### Topology on Curve Spaces

The space $C_q^p$ of causal curves from $q$ to $p$ is given a topology as follows:

1. **Parametrization**: We parametrize curves by a complete Riemannian metric on $M$ (which exists by paracompactness)

2. **Compact-Open Topology**: A sequence of curves $\gamma_n$ converges to $\gamma$ if:
   - For each parametrized curve $\gamma_n: [0, L_n] \to M$ and $\gamma: [0, L] \to M$
   - We have $L_n \to L$
   - For each $s \in [0, L]$, $\gamma_n(s) \to \gamma(s)$ in $M$

3. **Causality Preservation**: The limit of causal curves is causal (this requires global hyperbolicity)

## Proof Strategy for Problem 2

We need to show: If $q$ is to the past of $S$ and $p$ is to the future of $S$, then $C_q^p$ is compact.

### Key Ingredients

1. **Intersection with Cauchy Surface**: Every curve in $C_q^p$ must intersect $S$ at some point $r \in S$

2. **Compactness of Intersection Set**: The set 
   $$K = J^+(q) \cap J^-(p) \cap S$$
   is compact. This follows from:
   - $J^+(q) \cap J^-(p)$ is compact (by global hyperbolicity)
   - $S$ is a closed subset (being a Cauchy surface)
   - The intersection of a compact set with a closed set is compact

3. **Decomposition of Curves**: Each $\gamma \in C_q^p$ decomposes as:
   $$\gamma = \gamma_1 * \gamma_2$$
   where $\gamma_1 \in C_q^r$ and $\gamma_2 \in C_r^p$ for some $r \in K$

4. **Compactness of Pieces**: 
   - $C_q^r$ is compact for each $r$ (both $q$ and $r$ are to the past of or on $S$)
   - $C_r^p$ is compact for each $r$ (both $r$ and $p$ are on or to the future of $S$)

### The Fiber Bundle Perspective

We can view $C_q^p$ as sitting inside a fiber bundle:

$$\pi: \bigcup_{r \in K} C_q^r \times C_r^p \to K$$

where $\pi(\gamma_1, \gamma_2) = \gamma_1(L_1) = \gamma_2(0) = r$ is the meeting point.

The space $C_q^p$ is the image of the concatenation map:
$$\Phi: \bigcup_{r \in K} C_q^r \times C_r^p \to C_q^p$$

### Why is the Image Compact?

This requires a detailed argument using:

1. **Sequential Compactness**: Take a sequence $\{\gamma_n\} \subset C_q^p$

2. **Extract Meeting Points**: For each $\gamma_n$, let $r_n = \gamma_n \cap S$

3. **Compactness of K**: Since $\{r_n\} \subset K$ and $K$ is compact, there exists a convergent subsequence $r_{n_k} \to r_\infty \in K$

4. **Decompose**: Write $\gamma_{n_k} = \gamma_{n_k}^{(1)} * \gamma_{n_k}^{(2)}$ where:
   - $\gamma_{n_k}^{(1)} \in C_q^{r_{n_k}}$
   - $\gamma_{n_k}^{(2)} \in C_{r_{n_k}}^p$

5. **Compactness of Pieces**: 
   - By compactness theorems, extract convergent subsequences:
     - $\gamma_{n_{k_j}}^{(1)} \to \gamma_\infty^{(1)} \in C_q^{r_\infty}$
     - $\gamma_{n_{k_j}}^{(2)} \to \gamma_\infty^{(2)} \in C_{r_\infty}^p$

6. **Concatenation is Continuous**: 
   $$\gamma_{n_{k_j}} = \gamma_{n_{k_j}}^{(1)} * \gamma_{n_{k_j}}^{(2)} \to \gamma_\infty^{(1)} * \gamma_\infty^{(2)} = \gamma_\infty \in C_q^p$$

Therefore, $C_q^p$ is sequentially compact, hence compact.

## Why Global Hyperbolicity is Essential

Without global hyperbolicity, this argument fails:

### Example: Minkowski Space with a Point Removed

Consider $M = \mathbb{R}^{1,1} \setminus \{(0,0)\}$ (2D Minkowski space with origin removed).

- This is NOT globally hyperbolic (no Cauchy surface exists)
- Take $q = (-2, 0)$ and $p = (2, 0)$
- The space of causal curves from $q$ to $p$ includes:
  1. The straight line through the origin (but this doesn't exist in $M$!)
  2. Sequences of curves going around the removed point converging to this non-existent curve

The space $C_q^p$ is **not** compact in this case.

## Intuition: Why Compactness Matters

Compactness of $C_q^p$ is crucial for:

1. **Existence of Geodesics**: Compactness ensures that the length functional (for timelike curves) or action functional attains its extremum

2. **Stability**: Small perturbations of the spacetime lead to small changes in causal structure

3. **Singularity Theorems**: Compactness arguments are used extensively in proving that singularities are generic under certain conditions

4. **Causality Conditions**: Strong causality and stable causality can be characterized using properties of curve spaces

## Further Reading

- **Beem, Ehrlich, Easley**: "Global Lorentzian Geometry" (comprehensive reference)
- **Hawking & Ellis**: "Large Scale Structure of Space-Time" (classic reference)
- **Wald**: "General Relativity" (Chapter 8 on causal structure)
- **Minguzzi & Sánchez**: "The Causal Hierarchy of Spacetimes" (detailed survey)

## Connection to Other Results

This compactness result is used in proving:

1. **Penrose-Hawking Singularity Theorems**: Trapped surfaces and energy conditions lead to geodesic incompleteness

2. **Cosmic Censorship**: Attempts to prove that singularities are hidden behind event horizons

3. **Maximum Principles**: For wave equations on globally hyperbolic spacetimes

4. **Quantum Field Theory on Curved Spacetime**: Global hyperbolicity ensures well-posed initial value problem for field equations

