# Problem 3: Detailed Derivation of R_tt

## Metric and Setup

Given metric:
$$ds^2 = -dt^2 + \sum_{i,j=1}^d g_{ij}(t, \vec{x}) dx^i dx^j$$

Convention: 
- Greek indices $\mu, \nu, \rho, \sigma \in \{0, 1, 2, \ldots, d\}$ (spacetime)
- Latin indices $i, j, k, l \in \{1, 2, \ldots, d\}$ (spatial)
- $x^0 = t$

## Step 1: Metric Components

$$g_{\mu\nu} = \begin{pmatrix} 
-1 & 0 & \cdots & 0 \\
0 & g_{11} & \cdots & g_{1d} \\
\vdots & \vdots & \ddots & \vdots \\
0 & g_{d1} & \cdots & g_{dd}
\end{pmatrix}$$

$$g^{\mu\nu} = \begin{pmatrix} 
-1 & 0 & \cdots & 0 \\
0 & g^{11} & \cdots & g^{1d} \\
\vdots & \vdots & \ddots & \vdots \\
0 & g^{d1} & \cdots & g^{dd}
\end{pmatrix}$$

## Step 2: Christoffel Symbols

General formula:
$$\Gamma^\rho_{\mu\nu} = \frac{1}{2} g^{\rho\sigma}(\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu})$$

### Computing $\Gamma^t_{tt}$:

$$\Gamma^t_{tt} = \frac{1}{2} g^{t\sigma}(\partial_t g_{t\sigma} + \partial_t g_{t\sigma} - \partial_\sigma g_{tt})$$
$$= \frac{1}{2} g^{tt}(2\partial_t g_{tt} - \partial_t g_{tt}) = \frac{1}{2}(-1)(2 \cdot 0 - 0) = 0$$

### Computing $\Gamma^i_{tt}$:

$$\Gamma^i_{tt} = \frac{1}{2} g^{i\sigma}(\partial_t g_{t\sigma} + \partial_t g_{t\sigma} - \partial_\sigma g_{tt})$$

Since $g_{tj} = 0$ for all $j$, and $\partial_\sigma g_{tt} = 0$:
$$\Gamma^i_{tt} = 0$$

### Computing $\Gamma^t_{ti} = \Gamma^t_{it}$:

$$\Gamma^t_{ti} = \frac{1}{2} g^{t\sigma}(\partial_t g_{i\sigma} + \partial_i g_{t\sigma} - \partial_\sigma g_{ti})$$
$$= \frac{1}{2} g^{tt}(\partial_t g_{it} + \partial_i g_{tt} - \partial_t g_{ti})$$
$$= \frac{1}{2}(-1)(0 + 0 - 0) = 0$$

### Computing $\Gamma^i_{ti} = \Gamma^i_{it}$:

$$\Gamma^i_{tj} = \frac{1}{2} g^{i\sigma}(\partial_t g_{j\sigma} + \partial_j g_{t\sigma} - \partial_\sigma g_{tj})$$
$$= \frac{1}{2} g^{ik}(\partial_t g_{jk} + \partial_j g_{tk} - \partial_k g_{tj})$$
$$= \frac{1}{2} g^{ik}\partial_t g_{jk} = \frac{1}{2} g^{ik}\dot{g}_{jk}$$

In matrix notation: $\Gamma^i_{tj} = \frac{1}{2}(g^{-1}\dot{g})^i_j$

### Computing $\Gamma^t_{ij}$:

$$\Gamma^t_{ij} = \frac{1}{2} g^{t\sigma}(\partial_i g_{j\sigma} + \partial_j g_{i\sigma} - \partial_\sigma g_{ij})$$
$$= \frac{1}{2} g^{tt}(\partial_i g_{jt} + \partial_j g_{it} - \partial_t g_{ij})$$
$$= \frac{1}{2}(-1)(0 + 0 - \dot{g}_{ij}) = \frac{1}{2}\dot{g}_{ij}$$

### Computing $\Gamma^k_{ij}$:

$$\Gamma^k_{ij} = \frac{1}{2} g^{k\sigma}(\partial_i g_{j\sigma} + \partial_j g_{i\sigma} - \partial_\sigma g_{ij})$$
$$= \frac{1}{2} g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$$

This is the standard 3D Christoffel symbol for the spatial metric $g_{ij}$.

## Step 3: Summary of Non-zero Christoffel Symbols

- $\Gamma^t_{ij} = \frac{1}{2}\dot{g}_{ij}$
- $\Gamma^i_{tj} = \Gamma^i_{jt} = \frac{1}{2}g^{ik}\dot{g}_{jk} = \frac{1}{2}(g^{-1}\dot{g})^i_j$
- $\Gamma^k_{ij}$ = spatial Christoffel symbols

## Step 4: Computing the Contracted Christoffel Symbol

$$\Gamma^\rho_{t\rho} = \Gamma^t_{tt} + \Gamma^i_{ti} = 0 + \frac{1}{2}g^{ik}\dot{g}_{ik}$$

In index notation:
$$\Gamma^i_{ti} = \frac{1}{2}g^{ik}\dot{g}_{ik} = \frac{1}{2}\text{Tr}(g^{-1}\dot{g})$$

## Step 5: Ricci Tensor Formula

$$R_{\mu\nu} = \partial_\rho \Gamma^\rho_{\mu\nu} - \partial_\nu \Gamma^\rho_{\mu\rho} + \Gamma^\rho_{\rho\sigma}\Gamma^\sigma_{\mu\nu} - \Gamma^\rho_{\mu\sigma}\Gamma^\sigma_{\nu\rho}$$

For $R_{tt}$:
$$R_{tt} = \partial_\rho \Gamma^\rho_{tt} - \partial_t \Gamma^\rho_{t\rho} + \Gamma^\rho_{\rho\sigma}\Gamma^\sigma_{tt} - \Gamma^\rho_{t\sigma}\Gamma^\sigma_{t\rho}$$

## Step 6: Evaluating $R_{tt}$ Term by Term

### Term 1: $\partial_\rho \Gamma^\rho_{tt}$

$$\partial_\rho \Gamma^\rho_{tt} = \partial_t \Gamma^t_{tt} + \partial_i \Gamma^i_{tt} = 0 + 0 = 0$$

### Term 2: $-\partial_t \Gamma^\rho_{t\rho}$

$$-\partial_t \Gamma^\rho_{t\rho} = -\partial_t\left(\frac{1}{2}\text{Tr}(g^{-1}\dot{g})\right) = -\frac{1}{2}\partial_t\text{Tr}(g^{-1}\dot{g})$$

### Term 3: $\Gamma^\rho_{\rho\sigma}\Gamma^\sigma_{tt}$

Since $\Gamma^\sigma_{tt} = 0$ for all $\sigma$:
$$\Gamma^\rho_{\rho\sigma}\Gamma^\sigma_{tt} = 0$$

### Term 4: $-\Gamma^\rho_{t\sigma}\Gamma^\sigma_{t\rho}$

This expands as:
$$-\Gamma^\rho_{t\sigma}\Gamma^\sigma_{t\rho} = -\sum_{\rho,\sigma} \Gamma^\rho_{t\sigma}\Gamma^\sigma_{t\rho}$$

Breaking into cases:

**Case $\rho = t, \sigma = t$:**
$$-\Gamma^t_{tt}\Gamma^t_{tt} = 0$$

**Case $\rho = t, \sigma = i$:**
$$-\Gamma^t_{ti}\Gamma^i_{tt} = 0$$ (since $\Gamma^i_{tt} = 0$)

**Case $\rho = i, \sigma = t$:**
$$-\Gamma^i_{tt}\Gamma^t_{ti} = 0$$ (since $\Gamma^i_{tt} = 0$)

**Case $\rho = i, \sigma = j$:**
$$-\Gamma^i_{tj}\Gamma^j_{ti}$$

Let's compute this carefully:
$$\Gamma^i_{tj} = \frac{1}{2}g^{ik}\dot{g}_{kj}, \quad \Gamma^j_{ti} = \frac{1}{2}g^{jl}\dot{g}_{li}$$

Therefore:
$$-\Gamma^i_{tj}\Gamma^j_{ti} = -\left(\frac{1}{2}g^{ik}\dot{g}_{kj}\right)\left(\frac{1}{2}g^{jl}\dot{g}_{li}\right)$$
$$= -\frac{1}{4}g^{ik}\dot{g}_{kj}g^{jl}\dot{g}_{li}$$

In matrix notation, $(g^{-1}\dot{g})^i_j = g^{ik}\dot{g}_{kj}$, so:
$$= -\frac{1}{4}(g^{-1}\dot{g})^i_j(g^{-1}\dot{g})^j_i$$

Summing over $i, j$:
$$-\sum_{i,j}\Gamma^i_{tj}\Gamma^j_{ti} = -\frac{1}{4}\sum_i(g^{-1}\dot{g})^i_j(g^{-1}\dot{g})^j_i$$
$$= -\frac{1}{4}\sum_i[(g^{-1}\dot{g})^2]^i_i = -\frac{1}{4}\text{Tr}[(g^{-1}\dot{g})^2]$$

## Step 7: Final Result

Combining all terms:
$$R_{tt} = 0 - \frac{1}{2}\partial_t\text{Tr}(g^{-1}\dot{g}) + 0 - \frac{1}{4}\text{Tr}(g^{-1}\dot{g})^2$$

$$\boxed{R_{tt} = -\frac{1}{2}\partial_t\text{Tr}(g^{-1}\dot{g}) - \frac{1}{4}\text{Tr}(g^{-1}\dot{g})^2}$$

## Expansion of the Time Derivative Term

To better understand the first term, let's expand it using the product rule.

Let $K = g^{-1}\dot{g}$. Then:
$$\frac{d}{dt}\text{Tr}(K) = \text{Tr}\left(\frac{dK}{dt}\right) = \text{Tr}\left(\frac{d}{dt}(g^{-1}\dot{g})\right)$$

Using the product rule:
$$\frac{d}{dt}(g^{-1}\dot{g}) = \frac{d g^{-1}}{dt}\dot{g} + g^{-1}\ddot{g}$$

For the derivative of $g^{-1}$, we use $g \cdot g^{-1} = I$, so:
$$\dot{g} \cdot g^{-1} + g \cdot \frac{dg^{-1}}{dt} = 0$$
$$\frac{dg^{-1}}{dt} = -g^{-1}\dot{g}g^{-1}$$

Therefore:
$$\frac{d}{dt}(g^{-1}\dot{g}) = -g^{-1}\dot{g}g^{-1}\dot{g} + g^{-1}\ddot{g}$$
$$= -(g^{-1}\dot{g})^2 + g^{-1}\ddot{g}$$

Taking the trace:
$$\partial_t\text{Tr}(g^{-1}\dot{g}) = -\text{Tr}(g^{-1}\dot{g})^2 + \text{Tr}(g^{-1}\ddot{g})$$

Substituting back:
$$R_{tt} = -\frac{1}{2}\left[-\text{Tr}(g^{-1}\dot{g})^2 + \text{Tr}(g^{-1}\ddot{g})\right] - \frac{1}{4}\text{Tr}(g^{-1}\dot{g})^2$$
$$= \frac{1}{2}\text{Tr}(g^{-1}\dot{g})^2 - \frac{1}{2}\text{Tr}(g^{-1}\ddot{g}) - \frac{1}{4}\text{Tr}(g^{-1}\dot{g})^2$$
$$= \frac{1}{4}\text{Tr}(g^{-1}\dot{g})^2 - \frac{1}{2}\text{Tr}(g^{-1}\ddot{g})$$

This is an alternative form that makes the second derivative explicit:
$$\boxed{R_{tt} = \frac{1}{4}\text{Tr}(g^{-1}\dot{g})^2 - \frac{1}{2}\text{Tr}(g^{-1}\ddot{g})}$$

## Connection to Raychaudhuri's Equation

The expansion scalar $\theta$ of a congruence of timelike geodesics with tangent $u^\mu = \delta^\mu_t$ is:
$$\theta = \nabla_\mu u^\mu = \Gamma^\mu_{\mu t} = \Gamma^t_{tt} + \Gamma^i_{it} = 0 + \frac{1}{2}\text{Tr}(g^{-1}\dot{g})$$

So $\theta = \frac{1}{2}\text{Tr}(g^{-1}\dot{g})$.

From our result:
$$R_{tt} = -\frac{1}{2}\dot{\theta} - \theta^2$$

Rearranging:
$$\dot{\theta} = -2R_{tt} - 2\theta^2$$

This is a key component of Raychaudhuri's equation! The full equation includes shear and vorticity terms:
$$\frac{d\theta}{dt} = -R_{\mu\nu}u^\mu u^\nu - \frac{1}{3}\theta^2 - \sigma^2 + \omega^2$$

In our case with $u^\mu = \delta^\mu_t$ and assuming zero shear and vorticity, we recover the simplified form.

