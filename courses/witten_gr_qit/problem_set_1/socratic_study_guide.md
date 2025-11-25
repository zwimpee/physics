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

# Quick Self-Test

Before returning to Problem 1.3, verify you can answer:

1. What is the Minkowski metric in 2D?
2. What does ds² = 0 represent physically?
3. Why are the curves γₙ = sin(πnt) non-causal?
4. What is the limit of γₙ when parametrized by Euclidean arclength?
5. What is a Cauchy surface?
6. What does global hyperbolicity guarantee?
7. Why does any causal curve from past-of-S to future-of-S cross S exactly once?

If you can answer these confidently, you're ready for Problem 1.3!

