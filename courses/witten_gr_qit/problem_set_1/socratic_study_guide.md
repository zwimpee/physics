# Problem Set 1: Socratic Study Guide

## How to Use This Document

This guide presents the material we covered in a self-testing format. For each section:

1. **Read the problem statement**
2. **Attempt the "Check Your Understanding" questions** before looking at the answers
3. **Work through the derivations** step by step
4. **Try the coding exercises** to verify your understanding

---

# Problem 1.1: Convergence of Curves in Minkowski Space

## Problem Statement

In 2D Minkowski space with coordinates (t, x) and metric:
```
ds² = -dt² + dx²
```

Consider the sequence of curves γₙ defined by:
```
x = sin(πnt),  for n = 1, 2, 3, ...
```

**Part (a):** Viewing the γₙ as inextendible curves with t ∈ [0, ∞), parametrized by Euclidean arclength, find a convergent subsequence and describe what it converges to.

**Part (b):** Is your answer in (a) a curve from q = (0,0) to p = (1,0)?

---

## Foundational Concepts

### Concept 1: Minkowski Space

**Check Your Understanding:**
> Q: What distinguishes the Minkowski metric from the Euclidean metric?
> 
> (Try to answer before reading below)

<details>
<summary>Answer</summary>

The Minkowski metric has a **negative sign** on the time component:
```
Minkowski:  ds² = -dt² + dx²
Euclidean:  ds² = dt² + dx²
```

This negative sign encodes the distinction between time and space in special relativity.
</details>

---

### Concept 2: Light Cones and Causal Structure

**Check Your Understanding:**
> Q: For a light ray traveling at speed c = 1, we have dx/dt = ±1. What is ds² along this trajectory?

<details>
<summary>Answer</summary>

```
ds² = -dt² + dx² = -dt² + (±dt)² = -dt² + dt² = 0
```

Light rays satisfy ds² = 0 — they are **null**.
</details>

---

**Check Your Understanding:**
> Q: What are the three types of curves/intervals in Minkowski space?

<details>
<summary>Answer</summary>

| Type | Condition | Physical Meaning |
|------|-----------|------------------|
| Timelike | ds² < 0 | Massive particles (slower than light) |
| Null | ds² = 0 | Light rays (at light speed) |
| Spacelike | ds² > 0 | "Faster than light" (not physical for particles) |
</details>

---

### Concept 3: The Light Cone Geometry

```
        t (future)
        |
   Q2   |   Q1
    \   |   /
     \  |  /   ← Future light cone (t > 0)
      \ | /
       \|/
--------q--------→ x
       /|\
      / | \
     /  |  \   ← Past light cone (t < 0)
    /   |   \
   Q3   |   Q4
        |
     (past)
```

**Key facts:**
- Future light cone extends into quadrants 1 and 2 (t > 0)
- Past light cone extends into quadrants 3 and 4 (t < 0)
- The light cone forms an "X" centered at the point q

---

## Derivation: Classifying the Curves γₙ

### Step 1: Compute the tangent vector

For γₙ: x = sin(πnt)

**Check Your Understanding:**
> Q: What is dx/dt? (Remember the chain rule!)

<details>
<summary>Answer</summary>

```
dx/dt = d/dt[sin(πnt)] = πn·cos(πnt)
```

The factor of πn comes from the chain rule.
</details>

---

### Step 2: Compute ds² along the curve

**Check Your Understanding:**
> Q: Express ds²/dt² in terms of n and t.

<details>
<summary>Answer</summary>

```
ds² = -dt² + dx²
    = -dt² + (πn·cos(πnt))² dt²
    = [-1 + π²n² cos²(πnt)] dt²
```

So:
```
ds²/dt² = π²n² cos²(πnt) - 1
```
</details>

---

### Step 3: Determine causal character

**Check Your Understanding:**
> Q: For n = 1, what is the maximum value of |dx/dt|? Is γ₁ always timelike, always spacelike, or mixed?

<details>
<summary>Answer</summary>

Maximum of |dx/dt| = |π·cos(πt)| is **π ≈ 3.14** (when cos = ±1).

Since π > 1, the curve exceeds light speed at some points!

- When |cos(πt)| is small: |dx/dt| < 1 → **timelike**
- When |cos(πt)| is large: |dx/dt| > 1 → **spacelike**

The curve is **mixed** — it oscillates between timelike and spacelike.
</details>

---

### Step 4: Count light cone crossings

**Result:** For general n, the curve γₙ crosses the light cone **2n times** in the interval t ∈ [0, 1].

**Check Your Understanding:**
> Q: Why 2n crossings?

<details>
<summary>Answer</summary>

The curve crosses the light cone when |πn·cos(πnt)| = 1.

In t ∈ [0, 1], the argument πnt goes through n half-periods of cosine.

Each half-period contributes 2 crossings (once for cos = +1/(πn), once for cos = -1/(πn)).

Total: 2n crossings.
</details>

---

## Derivation: The Arclength Argument

### Step 1: Euclidean arclength element

**Check Your Understanding:**
> Q: What is the Euclidean arclength element ds_E/dt for γₙ?

<details>
<summary>Answer</summary>

```
ds_E = √(dt² + dx²) = √(1 + (dx/dt)²) dt

ds_E/dt = √(1 + π²n² cos²(πnt))
```
</details>

---

### Step 2: Behavior for large n

**Check Your Understanding:**
> Q: For large n, approximately how much Euclidean arclength is needed to traverse from t = 0 to t = 1?

<details>
<summary>Answer</summary>

When cos(πnt) ≠ 0, the integrand ≈ πn|cos(πnt)|.

The total arclength grows like **O(n)** — proportional to n.

More oscillations → more "zigzag" → more total path length.
</details>

---

### Step 3: The key insight

**Check Your Understanding:**
> Q: If arclength to reach t = 1 grows like n, what happens to t(s) for fixed arclength s as n → ∞?

<details>
<summary>Answer</summary>

For fixed s, as n → ∞:
```
t(s) → 0
```

The curve "uses up" all its arclength budget wiggling near t = 0, so it never makes progress in time.
</details>

---

### Step 4: The limit curve

**Check Your Understanding:**
> Q: What is the limit curve γ_∞(s) as n → ∞?

<details>
<summary>Answer</summary>

```
γ_∞(s) = (0, 0) = q   for all s ≥ 0
```

The limit is the **constant curve** that stays at the starting point q forever.
</details>

---

## Resolution of the Paradox

| Viewpoint | Domain | Limit exists? | What is the limit? |
|-----------|--------|---------------|-------------------|
| Curves from q to p | t ∈ [0, 1] | **No** | — |
| Inextendible curves (arclength) | s ∈ [0, ∞) | **Yes** | Constant curve at q |

**The resolution:** The limit exists in the arclength parametrization, but it's **degenerate** — it never reaches p. There's no contradiction because different notions of "limit" give different answers.

---

## Coding Exercises

### Exercise 1: Verify the derivative

```python
import sympy as sp

t = sp.Symbol('t', real=True)
n = sp.Symbol('n', positive=True, integer=True)

x = sp.sin(sp.pi * n * t)
dx_dt = sp.diff(x, t)
print("dx/dt =", dx_dt)
```

**Expected output:** `pi*n*cos(pi*n*t)`

---

### Exercise 2: Find light cone crossings numerically

```python
import numpy as np

def count_crossings(n, num_points=10000):
    """Find all light-cone crossings for γₙ in [0, 1]"""
    t = np.linspace(0, 1, num_points)
    f = np.abs(np.pi * n * np.cos(np.pi * n * t)) - 1
    
    crossings = []
    for i in range(len(f) - 1):
        if f[i] * f[i+1] < 0:
            t_cross = t[i] - f[i] * (t[i+1] - t[i]) / (f[i+1] - f[i])
            crossings.append(t_cross)
    
    return crossings

# Verify 2n crossings
for n in range(1, 6):
    print(f"n = {n}: {len(count_crossings(n))} crossings")
```

**Expected output:** 2, 4, 6, 8, 10

---

### Exercise 3: SymPy with proper domains

```python
import sympy as sp

t = sp.Symbol('t', real=True)
n_val = 3
c = 1 / (sp.pi * n_val)
domain = sp.Interval(0, 1)

sols_pos = sp.solveset(sp.cos(sp.pi * n_val * t) - c, t, domain=domain)
sols_neg = sp.solveset(sp.cos(sp.pi * n_val * t) + c, t, domain=domain)

print(f"Total crossings: {len(sols_pos) + len(sols_neg)}")
```

**Key lesson:** Use `solveset` with explicit domains for trigonometric equations!

---

# Problem 1.2: Compactness of Causal Curves

## Problem Statement

Let M be a globally hyperbolic spacetime with Cauchy hypersurface S. Let C_q^p denote the space of causal curves from q to p.

**Known:** C_q^p is compact when both q and p are on the same side of S.

**Prove:** C_q^p is also compact when q is to the past of S and p is to the future of S.

---

## Foundational Concepts

### Concept 1: Causal Structure Notation

**Check Your Understanding:**
> Q: What do J⁺(q), J⁻(q), I⁺(q), I⁻(q) denote?

<details>
<summary>Answer</summary>

| Symbol | Name | Definition |
|--------|------|------------|
| J⁺(q) | Causal future | Points reachable by causal (timelike or null) curves |
| J⁻(q) | Causal past | Points from which q is reachable causally |
| I⁺(q) | Chronological future | Points reachable by timelike curves only |
| I⁻(q) | Chronological past | Points from which q is reachable by timelike curves |

J⁺(q) includes the light cone boundary; I⁺(q) is the interior only.
</details>

---

### Concept 2: Cauchy Surfaces

**Check Your Understanding:**
> Q: What is the defining property of a Cauchy surface?

<details>
<summary>Answer</summary>

A **Cauchy surface** S is a spacelike hypersurface such that:

> **Every inextendible causal curve intersects S exactly once.**

It's a "complete snapshot" of the universe — knowing the state on S determines the entire past and future.
</details>

---

**Check Your Understanding:**
> Q: Why can't a causal curve cross a Cauchy surface twice?

<details>
<summary>Answer</summary>

1. A causal curve always moves "forward in time" (or stays on the light cone)
2. A Cauchy surface is spacelike — like a "surface of constant time"
3. Once you cross from past to future, you can't go back — that would require time travel!
</details>

---

### Concept 3: Global Hyperbolicity

**Check Your Understanding:**
> Q: What does global hyperbolicity guarantee about causal diamonds?

<details>
<summary>Answer</summary>

A spacetime is **globally hyperbolic** if:

```
J⁺(q) ∩ J⁻(p) is compact for all points q, p
```

The "causal diamond" between any two points is a bounded, closed region.
</details>

---

### The Causal Diamond

```
           p
          /|\
         / | \
        /  |  \
       / J⁻(p) \      ← past light cone of p
      /    |    \
     /     |     \
    +------+------+   ← causal diamond = intersection
     \     |     /
      \    |    /
       \ J⁺(q) /      ← future light cone of q
        \  |  /
         \ | /
          \|/
           q
```

---

## The Proof

### Step 1: Decomposition

**Check Your Understanding:**
> Q: If q is in the past of S and p is in the future of S, what can we say about any causal curve from q to p?

<details>
<summary>Answer</summary>

Any causal curve from q to p must **cross S exactly once** at some point r.

We can decompose:
```
γ = γ₁ * γ₂
```
where:
- γ₁ ∈ C_q^r (curve from q to r)
- γ₂ ∈ C_r^p (curve from r to p)
</details>

---

### Step 2: The crossing points form a compact set

**Check Your Understanding:**
> Q: The possible crossing points r form the set K = J⁺(q) ∩ J⁻(p) ∩ S. Why is K compact?

<details>
<summary>Answer</summary>

1. J⁺(q) ∩ J⁻(p) is compact (by global hyperbolicity)
2. S is a closed surface
3. Intersection of compact with closed = **compact**

Therefore K is compact.
</details>

---

### Step 3: Products of compact sets

**Check Your Understanding:**
> Q: For a fixed crossing point r, why is C_q^r × C_r^p compact?

<details>
<summary>Answer</summary>

- C_q^r is compact (q and r are both on the past side of S — known result)
- C_r^p is compact (r and p are both on the future side of S — known result)
- **Product of compact sets is compact** (topology fact)
</details>

---

### Step 4: Continuous images preserve compactness

**Check Your Understanding:**
> Q: How does the concatenation map Φ(γ₁, γ₂) = γ₁ * γ₂ help us conclude?

<details>
<summary>Answer</summary>

1. Φ: C_q^r × C_r^p → C_q^p is continuous
2. Continuous image of compact set is compact
3. Therefore the image (curves from q to p through r) is compact
4. Taking the union over all r ∈ K (a compact set) preserves compactness

**Conclusion:** C_q^p is compact. ∎
</details>

---

## Summary Table

| Step | What | Why compact? |
|------|------|--------------|
| 1 | K = crossing points on S | Causal diamond ∩ S |
| 2 | For each r: C_q^r × C_r^p | Product of compact |
| 3 | Union over r ∈ K | Continuous family over compact base |
| 4 | Apply concatenation Φ | Continuous image of compact |
| 5 | **Result: C_q^p** | **Compact!** ✓ |

---

## Physical Interpretation

In a globally hyperbolic spacetime:
- No closed timelike curves (no time travel)
- Causal diamonds are bounded
- The space of "ways to travel causally from q to p" is well-behaved

This is foundational for proving singularity theorems — it ensures that focusing of geodesics leads to predictable consequences.

---

# Next: Problem 1.3

Problem 1.3 involves computing the Ricci tensor component R_tt for the metric:
```
ds² = -dt² + g_ij(t, x) dx^i dx^j
```

This calculation leads directly to **Raychaudhuri's equation**, which describes how geodesic congruences focus or defocus due to gravity.

**Key skills needed:**
- Christoffel symbol calculation
- Ricci tensor from Christoffel symbols
- Matrix trace operations

We'll use SymPy to verify the tensor calculations!

---

# Quick Self-Test (Problems 1.1 & 1.2)

Before proceeding to Problem 1.3, verify you can answer:

1. What is the Minkowski metric in 2D?
2. What does ds² = 0 represent physically?
3. Why are the curves γₙ = sin(πnt) non-causal?
4. What is the limit of γₙ when parametrized by Euclidean arclength?
5. What is a Cauchy surface?
6. What does global hyperbolicity guarantee?
7. Why does any causal curve from past-of-S to future-of-S cross S exactly once?

---

# Problem 1.3: Computing R_tt for Raychaudhuri's Equation

## Problem Statement

Consider the metric:
```
ds² = -dt² + g_ij(t, x⃗) dx^i dx^j
```

where:
- g_ij is a d×d matrix (d = D-1, where D is spacetime dimension)
- g⁻¹ is the inverse matrix
- ġ denotes ∂g/∂t

**Goal:** Verify that:
```
R_tt = -½ ∂_t Tr(g⁻¹ġ) - ¼ [Tr(g⁻¹ġ)]²
```

This formula is the key step in deriving **Raychaudhuri's equation**.

---

## Foundational Concepts

### Concept 1: Why the Metric Tensor?

**Check Your Understanding:**
> Q: Why do we need a position-dependent metric g_μν(x) instead of the fixed Minkowski metric?

<details>
<summary>Answer</summary>

**Historical progression:**

1. **Special Relativity (1905):** Fixed interval ds² = -dt² + dx² + dy² + dz²
2. **Problem:** SR doesn't include gravity
3. **Equivalence Principle (1907):** Gravity ≈ acceleration (locally indistinguishable)
4. **Key insight:** If gravity = acceleration = curved motion, then gravity IS curvature of spacetime
5. **Solution:** Make the "distance formula" vary with position: ds² = g_μν(x) dx^μ dx^ν

The metric tensor g_μν(x) encodes how spacetime is curved at each point.
</details>

---

### Concept 2: Index Conventions

**Check Your Understanding:**
> Q: What's the difference between Greek indices (μ, ν) and Latin indices (i, j)?

<details>
<summary>Answer</summary>

| Index type | Letters | Range | What it covers |
|------------|---------|-------|----------------|
| Greek | μ, ν, ρ, σ | 0, 1, ..., D-1 | **All** coordinates (time + space) |
| Latin | i, j, k | 1, 2, ..., D-1 | **Spatial** coordinates only |

For D = 2: Greek indices ∈ {t, x}, Latin indices ∈ {x} only.
</details>

---

### Concept 3: The Line Element as a Quadratic Form

The line element ds² = g_μν dx^μ dx^ν is a **quadratic form**:
```
ds² = (dx)ᵀ · G · (dx)
```

where G is the metric matrix and (dx) is the vector of coordinate differentials.

---

## Derivation for D = 2 (Simplified Case)

We work with D = 2 (one time, one space) first, then generalize.

### Step 1: Write the metric in matrix form

**Given:**
```
ds² = -dt² + g(t,x) dx²
```

**Check Your Understanding:**
> Q: Expand the matrix multiplication ds² = [dt dx] G [dt; dx] and match coefficients.

<details>
<summary>Answer</summary>

Expanding:
```
ds² = [dt  dx] · [ g_tt   g_tx ] · [dt]
                 [ g_tx   g_xx ]   [dx]

    = [g_tt·dt + g_tx·dx,  g_tx·dt + g_xx·dx] · [dt]
                                                [dx]

    = g_tt·dt² + g_tx·dx·dt + g_tx·dt·dx + g_xx·dx²
    = g_tt·dt² + 2g_tx·dt·dx + g_xx·dx²
```

Matching with ds² = -dt² + g(t,x)·dx²:

| Coefficient of | Value | Therefore |
|----------------|-------|-----------|
| dt² | -1 | g_tt = -1 |
| dt dx | 0 | g_tx = 0 |
| dx² | g(t,x) | g_xx = g(t,x) |

**The metric matrix:**
```
G = g_μν = [ -1       0     ]
           [  0    g(t,x)   ]
```
</details>

---

### Step 2: Compute the inverse metric

**Check Your Understanding:**
> Q: For a diagonal matrix, how do you find the inverse?

<details>
<summary>Answer</summary>

For a diagonal matrix, take the reciprocal of each diagonal entry:
```
[ a   0 ]⁻¹   =   [ 1/a    0   ]
[ 0   b ]         [  0    1/b  ]
```

For our metric:
```
g^μν = [ -1        0       ]
       [  0    1/g(t,x)    ]
```
</details>

---

### Step 3: Compute Christoffel symbols

The Christoffel symbols are:
```
Γ^ρ_μν = ½ g^ρσ (∂_μ g_νσ + ∂_ν g_μσ - ∂_σ g_μν)
```

**Check Your Understanding:**
> Q: Why do most Christoffel symbols vanish for our diagonal metric?

<details>
<summary>Answer</summary>

- g_tt = -1 is constant → all derivatives of g_tt are zero
- g_tx = 0 is constant → all derivatives of g_tx are zero
- Only g_xx = g(t,x) has non-zero derivatives

Most terms in the Christoffel formula involve derivatives of constant components, so they vanish.
</details>

---

**The non-zero Christoffel symbols (D = 2):**

| Symbol | Computation | Result |
|--------|-------------|--------|
| Γ^t_xx | ½ g^tt (−∂_t g_xx) = ½(−1)(−ġ) | **ġ/2** |
| Γ^x_tx = Γ^x_xt | ½ g^xx (∂_t g_xx) = ½(1/g)(ġ) | **ġ/(2g)** |

where ġ = ∂g/∂t.

All other Christoffel symbols are zero.

---

### Step 4: Compute R_tt

The Ricci tensor formula is:
```
R_μν = ∂_ρ Γ^ρ_μν - ∂_ν Γ^ρ_μρ + Γ^ρ_ρσ Γ^σ_μν - Γ^ρ_μσ Γ^σ_νρ
```

For R_tt:
```
R_tt = ∂_ρ Γ^ρ_tt - ∂_t Γ^ρ_tρ + Γ^ρ_ρσ Γ^σ_tt - Γ^ρ_tσ Γ^σ_tρ
```

**Check Your Understanding:**
> Q: Since Γ^ρ_tt = 0 for all ρ, which terms vanish?

<details>
<summary>Answer</summary>

- Term 1: ∂_ρ Γ^ρ_tt = ∂_ρ(0) = 0 ✓
- Term 3: Γ^ρ_ρσ Γ^σ_tt = Γ^ρ_ρσ · 0 = 0 ✓

Only Terms 2 and 4 survive:
```
R_tt = - ∂_t Γ^ρ_tρ - Γ^ρ_tσ Γ^σ_tρ
```
</details>

---

### Step 5: Evaluate the surviving terms

**Term 2: -∂_t Γ^ρ_tρ**

First compute Γ^ρ_tρ (sum over ρ):
```
Γ^ρ_tρ = Γ^t_tt + Γ^x_tx = 0 + ġ/(2g)
```

Now take the time derivative:
```
∂_t [ġ/(2g)] = ½ ∂_t [ġ · g⁻¹]
             = ½ [g̈ · g⁻¹ + ġ · (-g⁻² ġ)]
             = ½ [g̈/g - ġ²/g²]
```

So:
```
-∂_t Γ^ρ_tρ = -½ g̈/g + ½ ġ²/g²
```

**Term 4: -Γ^ρ_tσ Γ^σ_tρ**

This is a double sum. The only non-zero contribution comes from ρ = x, σ = x:
```
-Γ^x_tx Γ^x_tx = -[ġ/(2g)]² = -ġ²/(4g²)
```

**Combining:**
```
R_tt = -½ g̈/g + ½ ġ²/g² - ġ²/(4g²)
     = -½ g̈/g + ¼ ġ²/g²
```

---

### Step 6: Rewrite using traces

For D = 2 with one spatial dimension:
```
Tr(g⁻¹ġ) = g⁻¹ġ = ġ/g
```

So:
```
∂_t Tr(g⁻¹ġ) = ∂_t(ġ/g) = g̈/g - ġ²/g²

[Tr(g⁻¹ġ)]² = (ġ/g)² = ġ²/g²
```

Substituting:
```
R_tt = -½ ∂_t Tr(g⁻¹ġ) - ¼ [Tr(g⁻¹ġ)]²

     = -½ [g̈/g - ġ²/g²] - ¼ [ġ²/g²]
     = -½ g̈/g + ½ ġ²/g² - ¼ ġ²/g²
     = -½ g̈/g + ¼ ġ²/g²  ✓
```

This matches what we computed directly!

---

## The General Case (D dimensions)

For the general metric with d = D-1 spatial dimensions:
```
ds² = -dt² + g_ij(t, x⃗) dx^i dx^j
```

The same calculation gives:
```
R_tt = -½ ∂_t Tr(g⁻¹ġ) - ¼ Tr[(g⁻¹ġ)²]
```

**Note:** In the general case, we get Tr[(g⁻¹ġ)²] not [Tr(g⁻¹ġ)]². 

For D = 2 (1×1 matrix), these are equal. For higher dimensions, they differ — the trace of a square is not the square of a trace!

---

## Connection to Raychaudhuri's Equation

Define the **expansion**:
```
θ = Tr(g⁻¹ġ)/2
```

This measures how rapidly geodesics are spreading apart (or converging).

Then R_tt becomes:
```
R_tt = -dθ/dt - θ² - (shear terms)
```

The **Raychaudhuri equation** states:
```
dθ/dt = -θ²/d - σ² + ω² - R_μν u^μ u^ν
```

where σ is shear, ω is vorticity, and u is the tangent to geodesics.

This equation is fundamental to singularity theorems: positive energy (R_μν u^μ u^ν > 0) causes focusing (dθ/dt < 0), which leads to caustics and singularities.

---

## Coding Exercise: Verify with SymPy

```python
import sympy as sp

# Define symbols
t, x = sp.symbols('t x', real=True)
g = sp.Function('g')(t, x)  # g(t, x)

# Metric components (D = 2)
g_tt = -1
g_tx = 0
g_xx = g

# Inverse metric
g_inv_tt = -1
g_inv_xx = 1/g

# Time derivatives
g_dot = sp.diff(g, t)
g_ddot = sp.diff(g, t, 2)

# Christoffel symbols
Gamma_t_xx = g_dot / 2
Gamma_x_tx = g_dot / (2*g)

# Trace terms
Tr_ginv_gdot = g_dot / g
Tr_ginv_gdot_sq = (g_dot / g)**2

# R_tt via our formula
R_tt_formula = -sp.Rational(1,2) * sp.diff(Tr_ginv_gdot, t) - sp.Rational(1,4) * Tr_ginv_gdot_sq

# Simplify
R_tt_simplified = sp.simplify(R_tt_formula)
print("R_tt =", R_tt_simplified)

# Should give: -g̈/(2g) + ġ²/(4g²)
```

---

## Summary: Key Formulas

| Object | Formula |
|--------|---------|
| Metric | g_μν = diag(-1, g_ij) |
| Inverse metric | g^μν = diag(-1, g^ij) |
| Key Christoffel | Γ^t_ij = ½ ġ_ij,  Γ^k_ti = ½ g^kl ġ_il |
| Expansion | θ = ½ Tr(g⁻¹ġ) = ½ g^ij ġ_ij |
| R_tt | -½ ∂_t Tr(g⁻¹ġ) - ¼ Tr[(g⁻¹ġ)²] |

---

## Quick Self-Test (Problem 1.3)

Before moving to Problem Set 2, verify you can answer:

1. What is the relationship between the line element ds² and the metric tensor g_μν?
2. For a diagonal metric, how do you find the inverse?
3. What is the Christoffel symbol formula?
4. Why do most Christoffel symbols vanish for ds² = -dt² + g(t,x) dx²?
5. What is the expansion θ and what does it measure physically?
6. How does R_tt relate to Raychaudhuri's equation?

---

# Problem Set 1: Complete!

You have now worked through all three problems:

| Problem | Topic | Key Result |
|---------|-------|------------|
| 1.1 | Curve convergence | Limit depends on parametrization; can be degenerate |
| 1.2 | Compactness of causal curves | C_q^p compact via decomposition at Cauchy surface |
| 1.3 | R_tt calculation | R_tt = -½ ∂_t Tr(g⁻¹ġ) - ¼ Tr(g⁻¹ġ)² |

**Next up: Problem Set 2** — Null hypersurfaces, trapped surfaces, and causal boundaries!

