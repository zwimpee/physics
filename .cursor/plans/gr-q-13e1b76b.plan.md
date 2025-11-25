<!-- 13e1b76b-ab9c-41da-b70a-ac78aaa141cd cedfac06-8979-421d-a0d7-1149f98d60ba -->
# Recursive Socratic Learning: GR & Quantum Information Theory

## Overview

Work through all three problem sets from Witten's Physics 539 course using a recursive Socratic method. Each problem will be approached through guided questioning that descends to your level of comfort, then builds back up. We'll pair analytic work with SymPy-based symbolic computation to verify and deepen understanding.

## Approach: Recursive Socratic Structure

For each problem:

1. **Initial probe questions** - Test understanding of core concepts
2. **Recursive descent** - If stuck, decompose into simpler prerequisite questions
3. **Grounded questions** - Reach questions you can answer from your physics/math background
4. **Guided ascent** - Build back up to the original problem
5. **Symbolic verification** - Implement the solution in SymPy to check and consolidate

---

## Problem Set 1: Causal Structure & Raychaudhuri

### Problem 1.1: Curve Convergence in Minkowski Space

- **Core concepts**: Arclength parametrization, pointwise limits, topology on curve spaces
- **Python**: Numerical integration of arclength, visualizing convergence
- **SymPy**: Symbolic arclength integral, limit analysis

### Problem 1.2: Compactness of Causal Curves

- **Core concepts**: Global hyperbolicity, Cauchy surfaces, causal structure
- **Python**: Visualizing causal diamonds, curve decomposition
- **Brush-up needed**: May need to revisit compactness arguments

### Problem 1.3: Computing R_tt (Raychaudhuri)

- **Core concepts**: Christoffel symbols, Ricci tensor, index gymnastics
- **Python**: SymPy tensor computations - this is where symbolic math shines
- **Key file**: `extended_notes_problem3.md` has detailed Christoffel calculations

---

## Problem Set 2: Null Hypersurfaces & Trapped Surfaces

### Problem 2.1: R_uu along Null Hypersurfaces

- **Core concepts**: Null geodesics, adapted coordinates, expansion/shear
- **Python**: SymPy metric inversion, Christoffel computation

### Problem 2.2: Trapped Surfaces

- **Core concepts**: Conformal transformations, null expansions, focusing
- **Python**: Numerical exploration of parameter space (t_0, R)

### Problem 2.3: Boundaries of Causal Futures

- **Core concepts**: Causal theory, achronal boundaries, null generators
- **Python**: Visualization of causal structure

---

## Problem Set 3: Quantum Information Theory

### Problems 3.1-3.2: Entropy & Density Matrices

- **Build-up needed**: Density matrix formalism from undergraduate QM
- **Core concepts**: von Neumann entropy, Bloch sphere, mixed vs pure states
- **Python**: SymPy matrix operations, eigenvalue computation

### Problem 3.3: Strong Subadditivity

- **Core concepts**: Bipartite/tripartite systems, partial trace, Schmidt decomposition
- **Python**: Tensor product spaces in NumPy/SymPy

### Problem 3.4: First Law of Thermodynamics

- **Core concepts**: Thermal states, variational calculus
- **Python**: Symbolic variation of entropy

### Problems 3.5-3.7: Relative Entropy & Quantum Channels

- **Core concepts**: CPTP maps, Kraus representation, monotonicity
- **Python**: Implementing quantum channels, verifying Kraus completeness

---

## Python/SymPy Learning Track

Alongside the physics, we'll build skills in:

1. **SymPy basics**: Symbols, expressions, simplification
2. **Calculus**: Differentiation, integration, limits
3. **Linear algebra**: Matrix operations, eigenvalues, traces
4. **Tensor calculus**: Index notation, metric operations (using sympy.tensor or custom)
5. **Quantum computing**: Density matrices, partial traces, channels

---

## Starting Point

We begin with **Problem 1.1** (curve convergence), which requires:

- Understanding arclength in a metric
- Limits and convergence of function sequences
- Parametrization-dependence of limits

This is an ideal entry point: conceptually rich but computationally tractable, and sets up the physical intuition for Raychaudhuri's equation.

### To-dos

- [ ] Problem 1.1: Curve convergence - Socratic walkthrough + SymPy arclength
- [ ] Problem 1.2: Compactness of causal curves - causal structure concepts
- [ ] Problem 1.3: R_tt calculation - SymPy tensor/Christoffel computation
- [ ] Problem 2.1: R_uu on null hypersurfaces - Raychaudhuri for null
- [ ] Problem 2.2: Trapped surfaces - conformal geometry + parameter space
- [ ] Problem 2.3: Causal future boundaries - black hole horizon theory
- [ ] Problem 3.1: Maximum entropy - Lagrange multipliers + SymPy optimization
- [ ] Problem 3.2: Bloch sphere - density matrix parametrization
- [ ] Problem 3.3: Strong subadditivity - tripartite quantum systems
- [ ] Problem 3.4: First law of thermodynamics - quantum derivation
- [ ] Problems 3.5-3.7: Relative entropy & Kraus operators