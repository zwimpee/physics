"""
Wald GR — Chapter 2 — Visualization Suite (Problems 1–8)

Generates static figures that support intuition for the Chapter 2 problem set.
Outputs images into ../figures/.

Run:
  python3 scripts/generate_ch2_visualizations.py
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------


def save(fig: plt.Figure, name: str) -> None:
    out = FIG_DIR / name
    fig.tight_layout()
    fig.savefig(out, dpi=220)
    plt.close(fig)


def disk_boundary(n: int = 500) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(0, 2 * math.pi, n)
    return np.cos(t), np.sin(t)


# -----------------------------------------------------------------------------
# Problem 2 — Factorization lemma (Eq. 2.2.2)
# -----------------------------------------------------------------------------


def fig_p2_1d_factorization() -> None:
    """
    Illustrate: F(x) = F(a) + (x-a) G(x), where G(x)=∫_0^1 F'(a+t(x-a)) dt.
    Use a concrete smooth function and show residual ~ 0 numerically.
    """
    F = lambda x: np.sin(2.2 * x) + 0.2 * x**3
    Fp = lambda x: 2.2 * np.cos(2.2 * x) + 0.6 * x**2

    a = -0.6
    xs = np.linspace(-2.0, 2.0, 500)
    # numerical integral for G(x)
    ts = np.linspace(0.0, 1.0, 400)
    G = []
    for x in xs:
        integrand = Fp(a + ts * (x - a))
        G.append(np.trapezoid(integrand, ts))
    G = np.array(G)
    approx = F(a) + (xs - a) * G
    resid = approx - F(xs)

    fig = plt.figure(figsize=(12, 4.5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title("Problem 2: 1D factorization intuition")
    ax1.plot(xs, F(xs), label="$F(x)$", linewidth=2.5)
    ax1.plot(xs, approx, "--", label="$F(a)+(x-a)G(x)$ (numeric)", linewidth=2.0)
    ax1.axvline(a, color="black", alpha=0.25)
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("value")
    ax1.grid(True, alpha=0.25)
    ax1.legend()

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title("Residual (should be ~0)")
    ax2.plot(xs, resid, color="#E45756", linewidth=2.0)
    ax2.axhline(0, color="black", alpha=0.3)
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("approx − exact")
    ax2.grid(True, alpha=0.25)

    save(fig, "p2_1d_factorization.png")


def fig_p2_2d_line_segment_gradient() -> None:
    """
    2D intuition: parameterize line from a to x, show gradient samples along it.
    This supports g(t)=F(a+t(x-a)) and g'(t)=∇F · (x-a).
    """
    # Example smooth function on R^2
    def F(x, y):
        return np.sin(1.7 * x) * np.cos(1.3 * y) + 0.15 * (x**2 + y**2)

    def gradF(x, y):
        dFx = 1.7 * np.cos(1.7 * x) * np.cos(1.3 * y) + 0.3 * x
        dFy = -1.3 * np.sin(1.7 * x) * np.sin(1.3 * y) + 0.3 * y
        return dFx, dFy

    a = np.array([-0.8, -0.2])
    x = np.array([0.9, 0.75])

    # background scalar field
    grid = np.linspace(-1.5, 1.5, 160)
    X, Y = np.meshgrid(grid, grid)
    Z = F(X, Y)

    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Problem 2: line-segment fundamental theorem of calculus in $\\mathbb{R}^2$")
    im = ax.imshow(Z, extent=[grid.min(), grid.max(), grid.min(), grid.max()], origin="lower", cmap="viridis", alpha=0.92)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="$F(x,y)$")

    # line segment from a to x
    ts = np.linspace(0, 1, 26)
    seg = a[None, :] + ts[:, None] * (x - a)[None, :]
    ax.plot(seg[:, 0], seg[:, 1], color="white", linewidth=2.5, label="segment $a+t(x-a)$")
    ax.scatter([a[0], x[0]], [a[1], x[1]], color=["#F58518", "#E45756"], s=70, zorder=5)
    ax.text(a[0] + 0.03, a[1] + 0.03, "$a$", color="white", fontsize=12, weight="bold")
    ax.text(x[0] + 0.03, x[1] + 0.03, "$x$", color="white", fontsize=12, weight="bold")

    # gradient samples along segment
    gx, gy = gradF(seg[:, 0], seg[:, 1])
    # scale arrows for readability
    ax.quiver(seg[:, 0], seg[:, 1], gx, gy, color="white", alpha=0.55, scale=35, width=0.003, label="$\\nabla F$ samples")

    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_aspect("equal")
    ax.legend(loc="upper right", fontsize=9)

    save(fig, "p2_2d_line_segment_gradient.png")


# -----------------------------------------------------------------------------
# Problem 3/4 — Commutator as “failure to commute” of flows
# -----------------------------------------------------------------------------


def fig_p3_commutator_flow_rectangle() -> None:
    """
    Visualize commutator [X,Y] at a point by comparing XY vs YX small-step flows.
    """
    # Choose two vector fields on R^2 that do not commute.
    # X = (1, 0) (constant right)
    # Y = (0, x) (vertical speed depends on x)
    def X_field(p):
        x, y = p
        return np.array([1.0, 0.0])

    def Y_field(p):
        x, y = p
        return np.array([0.0, x])

    p0 = np.array([0.6, -0.2])
    eps = 0.55

    # One Euler step along X then Y
    p1 = p0 + eps * X_field(p0)
    p2 = p1 + eps * Y_field(p1)

    # One Euler step along Y then X
    q1 = p0 + eps * Y_field(p0)
    q2 = q1 + eps * X_field(q1)

    # “commutator displacement” approx is (p2 - q2) / eps^2
    comm_approx = (p2 - q2) / (eps**2)

    # background vector field arrows
    grid = np.linspace(-1.2, 1.2, 17)
    Xg, Yg = np.meshgrid(grid, grid)
    U = np.ones_like(Xg)
    V = Xg

    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Problem 3: commutator as failure of flows to commute (toy example)")
    ax.quiver(Xg, Yg, U, V, alpha=0.35, color="gray", scale=18)

    ax.scatter([p0[0]], [p0[1]], color="#F58518", s=80, zorder=5)
    ax.text(p0[0] + 0.03, p0[1] + 0.03, "$p$", fontsize=12)

    # paths
    ax.plot([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], "-o", color="#4C78A8", linewidth=2.5, label="$X$ then $Y$")
    ax.plot([p0[0], q1[0], q2[0]], [p0[1], q1[1], q2[1]], "-o", color="#E45756", linewidth=2.5, label="$Y$ then $X$")

    # commutator arrow
    ax.arrow(
        q2[0],
        q2[1],
        (p2[0] - q2[0]),
        (p2[1] - q2[1]),
        head_width=0.04,
        head_length=0.06,
        length_includes_head=True,
        color="#54A24B",
        linewidth=2.0,
    )
    ax.text(
        q2[0] + 0.03,
        q2[1] + 0.03,
        f"$\\Delta\\approx\\varepsilon^2[X,Y](p)$\\n$[X,Y](p)\\approx({comm_approx[0]:.2f},{comm_approx[1]:.2f})$",
        fontsize=10,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85),
    )

    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_aspect("equal")
    ax.set_xlim(-1.2, 1.8)
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True, alpha=0.2)
    ax.legend(loc="upper left")

    save(fig, "p3_commutator_flow_rectangle.png")


# -----------------------------------------------------------------------------
# Problem 6/7 — Dual basis & signature intuition
# -----------------------------------------------------------------------------


def fig_p6_dual_basis_geometry() -> None:
    """
    Show a 2D basis and its dual basis as families of parallel lines (level sets of covectors).
    """
    v1 = np.array([1.0, 0.2])
    v2 = np.array([0.4, 1.0])
    A = np.column_stack([v1, v2])  # columns are basis vectors
    # Dual covectors (row vectors) satisfy v^{i*}(v_j)=δ^i_j, so rows are A^{-1}
    Ainv = np.linalg.inv(A)
    alpha = Ainv[0, :]  # covector components
    beta = Ainv[1, :]

    grid = np.linspace(-2, 2, 300)
    X, Y = np.meshgrid(grid, grid)
    # level sets alpha·x = const and beta·x = const
    F1 = alpha[0] * X + alpha[1] * Y
    F2 = beta[0] * X + beta[1] * Y

    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Problem 6: dual basis as coordinate readouts (level sets of covectors)")

    # contours
    ax.contour(X, Y, F1, levels=np.arange(-2.5, 2.6, 0.5), colors="#4C78A8", alpha=0.55, linewidths=1.2)
    ax.contour(X, Y, F2, levels=np.arange(-2.5, 2.6, 0.5), colors="#E45756", alpha=0.55, linewidths=1.2)

    # basis vectors
    ax.arrow(0, 0, v1[0], v1[1], head_width=0.06, head_length=0.08, color="#4C78A8", linewidth=3)
    ax.arrow(0, 0, v2[0], v2[1], head_width=0.06, head_length=0.08, color="#E45756", linewidth=3)
    ax.text(v1[0] + 0.05, v1[1] + 0.05, "$v_1$", color="#4C78A8", fontsize=13, weight="bold")
    ax.text(v2[0] + 0.05, v2[1] + 0.05, "$v_2$", color="#E45756", fontsize=13, weight="bold")

    ax.text(
        -1.9,
        1.7,
        "Blue lines: $v^{1*}(w)=\\text{const}$\nRed lines: $v^{2*}(w)=\\text{const}$\n\nDual basis satisfies:\n$v^{i*}(v_j)=\\delta^i{}_j$",
        fontsize=10,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.9),
    )

    ax.set_aspect("equal")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.grid(True, alpha=0.2)

    save(fig, "p6_dual_basis_geometry.png")


def fig_p7_signature_level_sets() -> None:
    """
    Show quadratic form level sets for Euclidean (+,+) vs Minkowski (-,+) in 2D.
    """
    grid = np.linspace(-2.2, 2.2, 600)
    X, Y = np.meshgrid(grid, grid)

    Q_euclid = X**2 + Y**2
    Q_mink = -X**2 + Y**2

    fig = plt.figure(figsize=(12, 5))

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title("Signature $(+,+)$: circles (positive definite)")
    levels = [0.5, 1.0, 2.0, 3.0]
    ax1.contour(X, Y, Q_euclid, levels=levels, colors="#4C78A8", linewidths=2.0)
    ax1.set_aspect("equal")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$y$")
    ax1.grid(True, alpha=0.25)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title("Signature $(-,+)$: hyperbolas (indefinite)")
    levels2 = [-3.0, -2.0, -1.0, -0.5, 0.5, 1.0, 2.0, 3.0]
    ax2.contour(X, Y, Q_mink, levels=levels2, colors="#E45756", linewidths=2.0)
    ax2.axline((0, 0), slope=1, color="black", alpha=0.25, linestyle="--")
    ax2.axline((0, 0), slope=-1, color="black", alpha=0.25, linestyle="--")
    ax2.text(0.2, 0.2, "null lines", alpha=0.65)
    ax2.set_aspect("equal")
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("$y$")
    ax2.grid(True, alpha=0.25)

    save(fig, "p7_signature_level_sets.png")


# -----------------------------------------------------------------------------
# Problem 8 — Rotating coordinates “light cylinder”
# -----------------------------------------------------------------------------


def fig_p8_rotating_light_cylinder() -> None:
    """
    Plot g_tt(rho) = -(1 - omega^2 rho^2) in rotating coordinates.
    Shows sign change at rho = 1/omega.
    """
    omega = 1.0
    rho = np.linspace(0, 2.0, 500)
    g_tt = -(1 - (omega**2) * rho**2)

    fig = plt.figure(figsize=(10.5, 4.5))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Problem 8(b): rotating coordinates — $g_{tt}=-(1-\\omega^2\\rho^2)$ and the light cylinder")
    ax.plot(rho, g_tt, linewidth=2.5, color="#4C78A8", label="$g_{tt}(\\rho)$")
    ax.axhline(0, color="black", alpha=0.35)
    rho_c = 1.0 / omega
    ax.axvline(rho_c, color="#E45756", linewidth=2.5, linestyle="--", label="$\\rho=1/\\omega$ (light cylinder)")
    ax.fill_between(rho, g_tt, 0, where=rho > rho_c, alpha=0.15, color="#E45756", label="region where $g_{tt}>0$")
    ax.set_xlabel("$\\rho$")
    ax.set_ylabel("$g_{tt}$")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left")

    save(fig, "p8_rotating_light_cylinder.png")


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main() -> None:
    # Problem 2
    fig_p2_1d_factorization()
    fig_p2_2d_line_segment_gradient()

    # Problem 3
    fig_p3_commutator_flow_rectangle()

    # Problem 6/7
    fig_p6_dual_basis_geometry()
    fig_p7_signature_level_sets()

    # Problem 8
    fig_p8_rotating_light_cylinder()

    print(f"[OK] Wrote Chapter 2 figures to: {FIG_DIR}")


if __name__ == "__main__":
    main()


