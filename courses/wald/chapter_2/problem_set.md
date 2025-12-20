
## Wald — General Relativity — Chapter 2

This document is a **Socratic workbook** for the Chapter 2 problems. It’s designed so **you** do the work and use me as a guided assistant (prompts, checks, and incremental hints), rather than reading a finished solution.

### How to use this (Socratic mode)

- **You try first**: write an outline or partial derivation under “Your work”.
- **When stuck**: tell me where you are stuck and what you’ve tried; I’ll respond with a **question** or a **small hint**, not the final argument.
- **Hint ladder**: each problem has Hint 1/2/3. Ask for the next hint only when you’ve exhausted the previous one.
- **Checkpoints**: use these to confirm you’re on track without me giving away the conclusion.

### Conventions (edit as needed)

- **Signature**: $(- + + +)$ unless noted
- **Units**: $c = 1$ unless noted
- **Index conventions**:
  - Greek indices $\mu,\nu,\dots$: spacetime components
  - Latin indices $a,b,\dots$: abstract indices (when used)

---

## Problem template (copy/paste per problem)

### Problem X.Y — <short title>

#### Statement (paraphrased)

#### Given / assumptions

#### Tools to recall (definitions / lemmas)

#### Socratic prompts

#### Hint ladder

#### Checkpoints

---

## Problems

### Problem 1 — Manifold structure of $S^2$: hemispherical charts and stereographic charts

#### Statement (paraphrased)

- **(a)** Using the **six hemispherical local coordinate charts** for $S^2$ described in the text, show that their **overlap/transition maps** are $C^\infty$, thereby completing the proof that $S^2$ is a smooth manifold.
- **(b)** Show by explicit construction that **two** coordinate charts suffice to cover $S^2$. *(This is where we introduce stereographic projection from the poles.)*

#### Tools to recall (definitions / lemmas)

- Definition of **smooth atlas** and **transition map**.
- The “six hemispherical charts” construction from the text (typically: open sets defined by the sign of one Cartesian coordinate, with the other two used as local coordinates).
- Stereographic projection (north/south pole) as a two-chart cover.

#### Socratic prompts

- **(a)** What are the six domains $U_{\pm x}$, $U_{\pm y}$, $U_{\pm z}\subset S^2$ (or whatever notation Wald uses)? Are they open in the subspace topology on $S^2$?
- **(a)** For one representative overlap (e.g. $U_{+z}\cap U_{+x}$), what are the two coordinate maps $\varphi_{+z}$ and $\varphi_{+x}$? What is $\varphi_{+x}\circ \varphi_{+z}^{-1}$ as an explicit function between open subsets of $\mathbb{R}^2$?
- **(a)** Which part of the transition map is “nontrivial” (usually a square root)? On what domain is it smooth?
- **(b)** What are the two stereographic charts (north-pole and south-pole projection)? What is their overlap, and what is the transition map between the two $\mathbb{R}^2$ coordinate descriptions?

#### Hint ladder

- **Hint 1 (a)**: Don’t do all $15$ overlaps separately. Do one carefully, then note the others are the same up to permuting $(x,y,z)$ and choosing signs.
- **Hint 2 (a)**: If a chart uses “solve for the missing coordinate” via $x=\pm\sqrt{1-y^2-z^2}$ (etc.), remember $\sqrt{\cdot}$ is smooth on $(0,\infty)$. Make sure the overlap corresponds to an open set where the radicand is $>0$.
- **Hint 3 (b)**: Use stereographic projection from the north/south pole onto the equatorial plane; on the overlap, the transition map is a smooth (indeed rational) map on $\mathbb{R}^2\setminus\{0\}$.

#### Checkpoints

- **(a)** You can state the six chart domains and write at least one nontrivial transition map explicitly, with a clear argument that it is $C^\infty$ on its domain.
- **(b)** You can state clearly: “the two stereographic charts cover $S^2$” and “their transition map is smooth on the overlap.”

#### Your work

---

### Problem 2 — A smooth-function factorization lemma (Eq. 2.2.2)

#### Statement (paraphrased)

Prove that an arbitrary **smooth** function $F:\mathbb{R}^n\to\mathbb{R}$ can be written in the form

$$
F(x)=F(a)+\sum_{\mu=1}^n \big(x^\mu-a^\mu\big)\,H_\mu(x),
$$

where

$$
H_\mu(x)=\int_0^1 \frac{\partial F}{\partial x^\mu}\!\big(t(x-a)+a\big)\,dt.
$$

The hint suggests proving the $n=1$ case using the identity

$$
F(x)-F(a)=(x-a)\int_0^1 F'\!\big(a+t(x-a)\big)\,dt
$$

and then proving the general case by induction on $n$.

#### Tools to recall (definitions / lemmas)

- Differentiation under the integral sign (basic smoothness check).
- Induction strategy on $n$: treat $\mathbb{R}^n \cong \mathbb{R}^{n-1}\times \mathbb{R}$.

#### Socratic prompts

- In the $n=1$ identity, what function would you naturally **define** as $G(x)$ so that $F(x)=F(a)+(x-a)G(x)$?
- How would you argue $G$ is $C^\infty$?
- For the induction step $n-1\to n$, what variable do you “peel off”, and how do you reduce to the 1D identity?

#### Hint ladder

- **Hint 1**: For $n=1$, define $G(x):=\int_0^1 F'(a+t(x-a))dt$.
- **Hint 2**: To show $G$ is smooth, try differentiating $G$ with respect to $x$ and justify exchanging $\frac{d}{dx}$ and $\int$.
- **Hint 3**: For $n>1$, fix $(x^1,\dots,x^{n-1})$ and apply the $n=1$ argument in the last variable.

#### Checkpoints

- You can produce explicit candidates $G_i(x)$ (or whatever Eq. (2.2.2) uses) and explain why each is smooth.

#### Your work

---

### Problem 3 — Commutators of vector fields and structure functions

#### Statement (paraphrased)

- **(a)** Show that the commutator $[X,Y]$ of smooth vector fields satisfies the axioms of a vector field (linearity and Leibniz rule when acting on smooth functions).
- **(b)** Verify the **Jacobi identity** for commutators:
  $$
  [[X,Y],Z] + [[Y,Z],X] + [[Z,X],Y] = 0.
  $$
- **(c)** If $\{Y_1,\dots,Y_n\}$ is a smooth local frame (a basis of $T_pM$ at each point), define functions $C^k{}_{ij}$ by
  $$
  [Y_i,Y_j] = \sum_k C^k{}_{ij}\,Y_k,\quad C^k{}_{ij}=-C^k{}_{ji},
  $$
  and derive the identity that the $C^k{}_{ij}$ must satisfy (from Jacobi).

#### Tools to recall (definitions / lemmas)

- Vector field as a derivation $X:C^\infty(M)\to C^\infty(M)$.
- Definition $[X,Y](f)=X(Y(f))-Y(X(f))$.

#### Socratic prompts

- For (a): If you compute $[X,Y](fg)$, where do you use the Leibniz rule for $X$ and $Y$?
- For (b): What happens if you expand $[[X,Y],Z](f)$ in terms of $X,Y,Z$ acting on $f$? Do terms cancel in groups?
- For (c): Substitute the expansion $[Y_i,Y_j]=C^k{}_{ij}Y_k$ into the Jacobi identity and compare coefficients of the basis vectors $Y_k$.

#### Hint ladder

- **Hint 1**: For (a), just treat everything as operators on functions and check derivation properties directly.
- **Hint 2**: For (b), expand the Jacobi combination acting on an arbitrary $f$ and use associativity of composition to cancel terms.
- **Hint 3**: For (c), you’ll get terms involving $Y_i(C^m{}_{jk})$ plus quadratic terms in $C$; group them by basis vector.

#### Checkpoints

- Your final identity in (c) should be antisymmetric in $i,j,k$ and should reduce to the usual Lie-algebra Jacobi identity when the $C^k{}_{ij}$ are constants.

#### Your work

---

### Problem 4 — Coordinate expression for commutators; dual coframe identity

#### Statement (paraphrased)

- **(a)** In a coordinate basis $\{\partial/\partial x^\mu\}$, show the components of the commutator satisfy the standard coordinate formula (the one involving partial derivatives of the components).
- **(b)** With $\{Y_i\}$ and structure functions $C^k{}_{ij}$ as in Problem 3(c), let $\{\theta^1,\dots,\theta^n\}$ be the dual coframe. Show the components of $\theta^i$ in a coordinate basis satisfy an identity involving the $C^i{}_{jk}$. (The book’s hint: contract with the coordinate components of $Y_i$.)

#### Tools to recall (definitions / lemmas)

- In coordinates: $v=v^\mu \partial_\mu$, $w=w^\mu \partial_\mu$.
- Duality: $\theta^i(Y_j)=\delta^i{}_j$.

#### Socratic prompts

- For (a): compute $[v,w](x^\nu)$ in two ways — directly from the definition and using $[v,w]=([v,w]^\mu)\partial_\mu$.
- For (b): start from $\theta^i(Y_j)=\delta^i{}_j$ and differentiate; where do commutators enter?

#### Hint ladder

- **Hint 1**: For (a), use $\partial_\mu(x^\nu)=\delta^\nu_\mu$ and the product rule.
- **Hint 2**: For (b), write $Y_j = (Y_j)^\mu \partial_\mu$ and $\theta^i = (\theta^i)_\mu dx^\mu$. Then $(\theta^i)_\mu (Y_j)^\mu=\delta^i{}_j$.
- **Hint 3**: Contract your target identity with $(Y_p)^\mu (Y_q)^\nu$ to isolate structure functions $C^i{}_{pq}$.

#### Checkpoints

- (a) should yield the familiar “$v^\mu\partial_\mu w^\nu - w^\mu\partial_\mu v^\nu$” pattern.
- (b) should look like a coordinate version of “$d\theta^i$” expressed via the structure functions (up to conventional signs).

#### Your work

---

### Problem 5 — Commuting frame implies local coordinates

#### Statement (paraphrased)

Given a local frame $\{Y_1,\dots,Y_n\}$ with $[Y_i,Y_j]=0$ for all $i,j$, prove that near each point there exist coordinates $(y^1,\dots,y^n)$ such that
$$
Y_i=\frac{\partial}{\partial y^i}.
$$

#### Tools to recall (definitions / lemmas)

- Integrability intuition (commuting flows).
- The PDE fact mentioned in the hint: a system $\partial f/\partial x^i = F_i$ has a local solution iff mixed partial derivatives match.
- Relation between commuting vector fields and exactness/closedness of the dual coframe (connects to Problem 4(b)).

#### Socratic prompts

- If $Y_i=\partial/\partial y^i$, what is the dual coframe $\{dy^i\}$ supposed to satisfy?
- Can you construct functions $y^i$ by solving differential equations of the form $Y_j(y^i)=\delta^i{}_j$?
- Where exactly do you use $[Y_i,Y_j]=0$ to ensure consistency of that PDE system?

#### Hint ladder

- **Hint 1**: Try to build $y^i$ as solutions to $Y_j(y^i)=\delta^i{}_j$.
- **Hint 2**: Rewrite those equations in a coordinate basis and apply the “mixed partials commute” condition from the hint.
- **Hint 3**: Use Problem 4(b) with $C^k{}_{ij}=0$ to show the relevant 1-forms are closed, then invoke local exactness.

#### Checkpoints

- You can explicitly state the compatibility condition for the PDE system and show it follows from $[Y_i,Y_j]=0$.

#### Your work

---

### Problem 6 — Dual basis and basis-independence of contraction (and one more operation)

#### Statement (paraphrased)

- **(a)** Verify that the dual vectors (defined in Eq. (2.3.1)) form a basis of $V^*$.
- **(b)** Let $v_1,\dots,v_n$ be a basis of the vector space $V$, and let $v^{1*},\dots,v^{n*}$ be its dual basis. Let $w\in V$ and let $\omega\in V^*$. Show that
  $$
  w=\sum_{\alpha} v^{\alpha *}(w)\,v_\alpha,
  \qquad
  \omega=\sum_{\alpha}\omega(v_\alpha)\,v^{\alpha *}.
  $$
- **(c)** Prove that the operation of **contraction** (Eq. (2.3.2)) is **independent of the choice of basis**.

#### Tools to recall (definitions / lemmas)

- Dual basis characterization: $\theta^i(e_j)=\delta^i{}_j$.
- Change-of-basis matrices and how components transform.

#### Socratic prompts

- For (a): if $\{\theta^i\}$ is defined by $\theta^i(e_j)=\delta^i{}_j$, how do you show $\{\theta^i\}$ spans $V^*$ and is linearly independent?
- For (b): what do the scalars $v^{\alpha *}(w)$ “mean” in terms of components of $w$ relative to the basis $\{v_\alpha\}$?
- For (b): how could you prove a vector identity like $w=\sum_\alpha c_\alpha v_\alpha$ without guessing $c_\alpha$? (What should you apply to both sides?)
- For (c): how do the components of a tensor change under a basis change, and why should a fully contracted quantity not change?

#### Hint ladder

- **Hint 1 (b)**: To show two vectors are equal, it’s enough to show they give the same value when paired with every element of a basis of $V^*$.
- **Hint 2 (b)**: Use the defining property of the dual basis: $v^{\alpha *}(v_\beta)=\delta^\alpha{}_\beta$.
- **Hint 3 (c)**: Write down the basis-change matrix $A$ and track how covariant and contravariant indices transform (one uses $A$, the other $A^{-1}$); in a contraction, an $A$ and an $A^{-1}$ appear and cancel.

#### Checkpoints

- **(b)** If you apply $v^{\beta *}$ to your proposed expansion for $w$, you should recover $v^{\beta *}(w)$.
- **(b)** If you evaluate your proposed expansion for $\omega$ on an arbitrary basis vector $v_\beta$, you should recover $\omega(v_\beta)$.
- **(c)** You can state clearly which indices transform with $A$ vs $A^{-1}$, and exhibit the cancellation in a contracted expression.

#### Your work

---

### Problem 7 — Metrics on a vector space; existence of orthonormal bases; signature

#### Statement (paraphrased)

Let $V$ be an $n$-dimensional vector space and let $g$ be a metric on $V$.

- **(a)** Show that one always can find an **orthonormal basis** $v_1,\dots,v_n$ of $V$, i.e., a basis such that
  $$
  g(v_\alpha, v_\beta)=\pm\,\delta_{\alpha\beta}
  $$
  (with an appropriate pattern of $+$ and $-$ signs). *(Hint: use induction.)*
- **(b)** Show the **signature** of $g$ (number of $+$ and $-$ signs) is independent of the choice of such orthonormal basis.

#### Tools to recall (definitions / lemmas)

- Gram–Schmidt style process adapted to indefinite metrics (or Sylvester’s law of inertia).
- Definition of signature.

#### Socratic prompts

- What does “orthonormal” mean when the metric is indefinite?
- What inductive step would you use on $\dim V$? (Pick a vector with $g(v,v)\neq 0$, split into orthogonal complement, repeat.)
- Why should the counts of $+$ and $-$ be invariant under change of orthonormal basis?

#### Hint ladder

- **Hint 1**: Start by finding a vector $v$ with $g(v,v)\neq 0$ and normalize it to $\pm 1$.
- **Hint 2**: Decompose $V=\mathrm{span}\{v\}\oplus v^\perp$ and apply induction to $v^\perp$.
- **Hint 3**: For signature invariance, think “two orthonormal bases are related by a matrix $A$ satisfying $A^T \eta A = \eta$”; what does that constrain?

#### Checkpoints

- You can produce a basis where the matrix of $g$ is diagonal with only $\pm 1$ entries.
- You can argue the numbers of $+$ and $-$ entries cannot change between orthonormal bases.

#### Your work

---

### Problem 8 — Coordinate expressions for familiar metrics

#### Statement (paraphrased)

- **(a)** Start from Euclidean space with $ds^2=dx^2+dy^2+dz^2$. Using spherical polar coordinates $(r,\theta,\phi)$, compute the metric in these coordinates (i.e., show $ds^2=dr^2+r^2 d\theta^2 + r^2\sin^2\theta\, d\phi^2$).
- **(b)** Start from Minkowski space $ds^2=-dt^2+dx^2+dy^2+dz^2$. Transform to a **rotating coordinate system** and compute the metric components $g_{\mu\nu}$ and the inverse $g^{\mu\nu}$ in those coordinates.

The coordinate transformation (as you provided) is:

$$
t'=t,\quad z'=z,
$$
$$
x'=\sqrt{x^2+y^2}\,\cos(\phi-\omega t),\quad y'=\sqrt{x^2+y^2}\,\sin(\phi-\omega t),
$$
where $\tan(\phi)=y/x$.

#### Tools to recall (definitions / lemmas)

- Coordinate transformation rule: $g'_{\alpha\beta} = \frac{\partial x^\mu}{\partial x'^\alpha}\frac{\partial x^\nu}{\partial x'^\beta} g_{\mu\nu}$.
- Computing $g^{\mu\nu}$ as the matrix inverse of $g_{\mu\nu}$.

#### Socratic prompts

- For (a): can you compute $dx,dy,dz$ in terms of $dr,d\theta,d\phi$ and then expand $dx^2+dy^2+dz^2$?
- For (b): write $dx,dy$ in terms of the rotating-coordinate differentials. Which cross-terms $dt\,d\phi$ appear, and why?
- Once you have $g_{\mu\nu}$, what’s the cleanest way to get $g^{\mu\nu}$: symbolic inversion, or exploiting block structure?

#### Hint ladder

- **Hint 1**: In (b), treat the rotating transform as a time-dependent rotation in the $x$-$y$ plane; compute differentials carefully.
- **Hint 2**: Expect $g_{t\phi}\neq 0$ (a mixed term), and $g_{tt}$ to pick up an $\omega^2\rho^2$ correction.
- **Hint 3**: For the inverse metric, isolate the $(t,\phi)$ block and invert that $2\times 2$ block explicitly.

#### Checkpoints

- (a) has no cross terms; (b) generally does.
- Your $g^{\mu\nu}$ should satisfy $g^{\mu\alpha}g_{\alpha\nu}=\delta^\mu{}_\nu$.

#### Your work



