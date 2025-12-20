"""
Wald GR (Ch. 2) — Problem 1(a)
Visual intuition for the "hemispherical charts" on S^2 and their projection to the unit disk.

This script generates a few static figures under ../figures/.
It intentionally emphasizes geometry (projection + hemisphere as a graph), not proofs.
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def _sphere_mesh(n_theta: int = 80, n_phi: int = 160) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    theta = np.linspace(0, math.pi, n_theta)  # polar angle
    phi = np.linspace(0, 2 * math.pi, n_phi)  # azimuth
    TH, PH = np.meshgrid(theta, phi, indexing="ij")
    X = np.sin(TH) * np.cos(PH)
    Y = np.sin(TH) * np.sin(PH)
    Z = np.cos(TH)
    return X, Y, Z


def _disk_boundary(n: int = 400) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(0, 2 * math.pi, n)
    return np.cos(t), np.sin(t)


def _sample_upper_hemisphere(n: int = 1200, seed: int = 0) -> np.ndarray:
    """Uniform-ish sampling on z>0 hemisphere via rejection in (x,y) disk."""
    rng = np.random.default_rng(seed)
    pts = []
    while len(pts) < n:
        xy = rng.uniform(-1, 1, size=(n, 2))
        r2 = (xy[:, 0] ** 2 + xy[:, 1] ** 2)
        ok = r2 < 1
        xy = xy[ok]
        r2 = r2[ok]
        z = np.sqrt(1 - r2)
        pts.append(np.column_stack([xy[:, 0], xy[:, 1], z]))
    return np.vstack(pts)[:n]


def fig1_upper_hemisphere_projection() -> None:
    """
    3D: upper hemisphere (z>0) as a surface; plus its projection onto the xy-plane.
    2D: the projected image in the xy-plane, emphasizing the open disk (boundary = equator z=0).
    """
    X, Y, Z = _sphere_mesh()
    upper = Z > 0

    fig = plt.figure(figsize=(13, 5))

    ax3d = fig.add_subplot(1, 2, 1, projection="3d")
    ax3d.set_title("Upper hemisphere $O_{+z}$ and projection $(x,y,z)\\mapsto(x,y)$")
    ax3d.plot_wireframe(X[::4, ::6], Y[::4, ::6], Z[::4, ::6], linewidth=0.4, alpha=0.25, color="gray")
    # Plot upper hemisphere by masking out z<=0 values.
    Z_upper = np.ma.masked_where(~upper, Z)
    ax3d.plot_surface(X, Y, Z_upper, alpha=0.55, color="#4C78A8", linewidth=0)

    # Unit disk boundary in xy-plane (z=0 plane)
    bx, by = _disk_boundary()
    ax3d.plot(bx, by, 0 * bx, color="#F58518", linewidth=2.0, label="boundary $x^2+y^2=1$ (equator)")

    # A few projection lines from hemisphere points down to z=0 plane
    pts = _sample_upper_hemisphere(n=80, seed=1)
    for x, y, z in pts[::5]:
        ax3d.plot([x, x], [y, y], [z, 0], color="black", alpha=0.12, linewidth=0.8)

    ax3d.set_xlabel("$x$")
    ax3d.set_ylabel("$y$")
    ax3d.set_zlabel("$z$")
    ax3d.set_box_aspect((1, 1, 1))
    ax3d.set_xlim(-1.1, 1.1)
    ax3d.set_ylim(-1.1, 1.1)
    ax3d.set_zlim(-0.1, 1.1)
    ax3d.legend(loc="upper left")

    ax2d = fig.add_subplot(1, 2, 2)
    ax2d.set_title("Image of $O_{+z}$ under $(x,y,z)\\mapsto(x,y)$ is the open unit disk")
    ax2d.scatter(pts[:, 0], pts[:, 1], s=6, alpha=0.35, color="#4C78A8", label="projected points")
    ax2d.plot(bx, by, color="#F58518", linewidth=2.0, label="boundary $x^2+y^2=1$")
    ax2d.set_aspect("equal")
    ax2d.set_xlabel("$x$")
    ax2d.set_ylabel("$y$")
    ax2d.set_xlim(-1.1, 1.1)
    ax2d.set_ylim(-1.1, 1.1)
    ax2d.grid(True, alpha=0.25)
    ax2d.legend(loc="upper right")

    out = FIG_DIR / "p1a_upper_hemisphere_projection.png"
    fig.tight_layout()
    fig.savefig(out, dpi=220)
    plt.close(fig)


def fig2_overlap_region_and_two_coordinate_descriptions() -> None:
    """
    Visualize an overlap, e.g. O_{+z} ∩ O_{+x}.

    - In 3D: highlight points with z>0 and x>0.
    - In 2D: show the corresponding subset in the (x,y) disk coordinates.
    - In another 2D: show the corresponding subset in the (y,z) disk coordinates
      (the chart that 'drops x').

    This makes the idea of transition maps feel like "same geometric points, different coordinate readouts".
    """
    pts = _sample_upper_hemisphere(n=2500, seed=2)
    overlap = pts[:, 0] > 0  # x>0 within z>0 hemisphere
    P = pts[overlap]

    fig = plt.figure(figsize=(14, 4.5))

    ax3d = fig.add_subplot(1, 3, 1, projection="3d")
    ax3d.set_title("Overlap region: $O_{+z}\\cap O_{+x}$")
    ax3d.scatter(pts[:, 0], pts[:, 1], pts[:, 2], s=2, alpha=0.06, color="gray")
    ax3d.scatter(P[:, 0], P[:, 1], P[:, 2], s=4, alpha=0.35, color="#54A24B")
    bx, by = _disk_boundary()
    ax3d.plot(bx, by, 0 * bx, color="#F58518", linewidth=1.8)
    ax3d.set_xlabel("$x$")
    ax3d.set_ylabel("$y$")
    ax3d.set_zlabel("$z$")
    ax3d.set_box_aspect((1, 1, 1))
    ax3d.set_xlim(-1.1, 1.1)
    ax3d.set_ylim(-1.1, 1.1)
    ax3d.set_zlim(-0.1, 1.1)

    # Coordinates in chart dropping z: (x,y)
    ax_xy = fig.add_subplot(1, 3, 2)
    ax_xy.set_title("Same overlap points in chart $(x,y)$ (drop $z$)")
    ax_xy.scatter(P[:, 0], P[:, 1], s=6, alpha=0.35, color="#4C78A8")
    ax_xy.plot(bx, by, color="#F58518", linewidth=2.0)
    ax_xy.axvline(0, color="black", alpha=0.25, linewidth=1.0, linestyle="--", label="$x=0$ (boundary of overlap)")
    ax_xy.set_aspect("equal")
    ax_xy.set_xlabel("$x$")
    ax_xy.set_ylabel("$y$")
    ax_xy.set_xlim(-1.1, 1.1)
    ax_xy.set_ylim(-1.1, 1.1)
    ax_xy.grid(True, alpha=0.25)
    ax_xy.legend(loc="lower left", fontsize=8)

    # Coordinates in chart dropping x: (y,z)
    ax_yz = fig.add_subplot(1, 3, 3)
    ax_yz.set_title("Same overlap points in chart $(y,z)$ (drop $x$)")
    ax_yz.scatter(P[:, 1], P[:, 2], s=6, alpha=0.35, color="#E45756")
    ax_yz.plot(bx, by, color="#F58518", linewidth=2.0)
    ax_yz.set_aspect("equal")
    ax_yz.set_xlabel("$y$")
    ax_yz.set_ylabel("$z$")
    ax_yz.set_xlim(-1.1, 1.1)
    ax_yz.set_ylim(-0.1, 1.1)
    ax_yz.grid(True, alpha=0.25)

    out = FIG_DIR / "p1a_overlap_two_coordinate_descriptions.png"
    fig.tight_layout()
    fig.savefig(out, dpi=220)
    plt.close(fig)


def main() -> None:
    fig1_upper_hemisphere_projection()
    fig2_overlap_region_and_two_coordinate_descriptions()
    print(f"[OK] Wrote figures to: {FIG_DIR}")


if __name__ == "__main__":
    main()


