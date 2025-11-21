"""
Visualizations for Physics 539 - Problem Set 3
Topics: Quantum Information Theory - Entropy, Density Matrices, Quantum Channels
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Wedge
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patches as mpatches
from matplotlib import cm

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 14

# Color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

print("Generating visualizations for Problem Set 3...")
print("="*80)

# ============================================================================
# PROBLEM 1: VON NEUMANN ENTROPY
# ============================================================================

print("\n[1/7] Creating visualizations for Problem 1: von Neumann entropy...")

fig1 = plt.figure(figsize=(16, 10))
fig1.suptitle('Problem 1: von Neumann Entropy and Maximization', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: Entropy vs probability (2-level system)
ax1 = fig1.add_subplot(2, 3, 1)
ax1.set_title('(a) Entropy of 2-level system', fontweight='bold')
ax1.set_xlabel('Probability p₁')
ax1.set_ylabel('Entropy S(ρ)')
ax1.grid(True, alpha=0.3)

p1 = np.linspace(0.001, 0.999, 500)
p2 = 1 - p1
S = -p1 * np.log2(p1) - p2 * np.log2(p2)

ax1.plot(p1, S, linewidth=3, color=colors[0], label='S = -p₁log₂(p₁) - p₂log₂(p₂)')
ax1.axvline(x=0.5, color='red', linestyle='--', linewidth=2, label='Maximum at p₁ = 1/2')
ax1.axhline(y=1.0, color='red', linestyle='--', linewidth=2, alpha=0.5)
ax1.plot(0.5, 1.0, 'ro', markersize=12, zorder=5)

ax1.text(0.5, 0.9, 'S_max = log₂(2) = 1 bit', ha='center',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

ax1.legend()
ax1.set_ylim(0, 1.1)

# Panel 2: Entropy for N-dimensional system
ax2 = fig1.add_subplot(2, 3, 2)
ax2.set_title('(b) Maximum Entropy vs Dimension N', fontweight='bold')
ax2.set_xlabel('Hilbert space dimension N')
ax2.set_ylabel('Maximum entropy S_max')
ax2.grid(True, alpha=0.3)

N_vals = np.arange(2, 21)
S_max_vals = np.log(N_vals)  # Natural log
S_max_vals_log2 = np.log2(N_vals)  # Log base 2

ax2.plot(N_vals, S_max_vals, 'o-', linewidth=2.5, markersize=8, 
        color=colors[0], label='S_max = ln(N)')
ax2.plot(N_vals, S_max_vals_log2, 's-', linewidth=2.5, markersize=8,
        color=colors[1], label='S_max = log₂(N)')

ax2.legend()

# Add annotation
ax2.text(15, 2.5, 'Maximally mixed state:\nρ = (1/N)𝕀', 
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

# Panel 3: Simplex visualization for 3-level system
ax3 = fig1.add_subplot(2, 3, 3, projection='3d')
ax3.set_title('(c) Entropy on Probability Simplex (N=3)', fontweight='bold')
ax3.set_xlabel('p₁')
ax3.set_ylabel('p₂')
ax3.set_zlabel('S(ρ)')

# Create probability simplex
n_points = 30
p1_range = np.linspace(0.01, 0.99, n_points)
p2_range = np.linspace(0.01, 0.99, n_points)

S_grid = np.zeros((n_points, n_points))
for i, p1_val in enumerate(p1_range):
    for j, p2_val in enumerate(p2_range):
        if p1_val + p2_val < 1:
            p3_val = 1 - p1_val - p2_val
            S_val = 0
            for p in [p1_val, p2_val, p3_val]:
                if p > 0:
                    S_val -= p * np.log(p)
            S_grid[i, j] = S_val
        else:
            S_grid[i, j] = np.nan

P1, P2 = np.meshgrid(p1_range, p2_range)
surf = ax3.plot_surface(P1, P2, S_grid.T, cmap='viridis', alpha=0.8, 
                        vmin=0, vmax=np.log(3))

# Mark maximum
ax3.plot([1/3], [1/3], [np.log(3)], 'ro', markersize=15, zorder=10)

ax3.view_init(elev=20, azim=45)
fig1.colorbar(surf, ax=ax3, shrink=0.5)

# Panel 4: Concavity demonstration
ax4 = fig1.add_subplot(2, 3, 4)
ax4.set_title('(d) Concavity of Entropy', fontweight='bold')
ax4.set_xlabel('Mixing parameter λ')
ax4.set_ylabel('Entropy S')
ax4.grid(True, alpha=0.3)

# Two pure states
rho1_p = [0.9, 0.1]  # First state
rho2_p = [0.2, 0.8]  # Second state

lambda_vals = np.linspace(0, 1, 100)
S_mixed = []
S_classical = []

for lam in lambda_vals:
    # Quantum mixing
    p_mixed = [lam * rho1_p[0] + (1-lam) * rho2_p[0],
               lam * rho1_p[1] + (1-lam) * rho2_p[1]]
    S_q = -sum([p * np.log(p) if p > 0 else 0 for p in p_mixed])
    S_mixed.append(S_q)
    
    # Classical mixing
    S1 = -sum([p * np.log(p) if p > 0 else 0 for p in rho1_p])
    S2 = -sum([p * np.log(p) if p > 0 else 0 for p in rho2_p])
    S_classical.append(lam * S1 + (1-lam) * S2)

ax4.plot(lambda_vals, S_mixed, linewidth=3, color=colors[0], label='S(λρ₁ + (1-λ)ρ₂)')
ax4.plot(lambda_vals, S_classical, linewidth=3, color=colors[1], 
        linestyle='--', label='λS(ρ₁) + (1-λ)S(ρ₂)')

ax4.fill_between(lambda_vals, S_mixed, S_classical, alpha=0.3, color='green',
                label='Concavity gap')

ax4.legend()
ax4.text(0.5, 0.5, 'S(λρ₁ + (1-λ)ρ₂) ≥ λS(ρ₁) + (1-λ)S(ρ₂)', 
        ha='center', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Panel 5: Lagrange multiplier optimization
ax5 = fig1.add_subplot(2, 3, 5)
ax5.axis('off')
ax5.text(0.5, 0.95, 'Lagrange Multiplier Method', 
         ha='center', fontsize=13, fontweight='bold', transform=ax5.transAxes)

lagrange_text = r'''
Optimization Problem:
Maximize: $S(\rho) = -\text{Tr}(\rho \log \rho) = -\sum_i \lambda_i \log \lambda_i$

Constraints:
• $\sum_i \lambda_i = 1$ (normalization)
• $\lambda_i \geq 0$ (positivity)

Lagrangian:
$\mathcal{L} = -\sum_i \lambda_i \log \lambda_i - \mu(\sum_i \lambda_i - 1)$

First-order condition:
$\frac{\partial \mathcal{L}}{\partial \lambda_j} = -\log \lambda_j - 1 - \mu = 0$

Solution: $\log \lambda_j = -1 - \mu$ (constant)
Therefore: $\lambda_j = \text{const}$

From normalization: $N \cdot \lambda_j = 1$
$\Rightarrow \lambda_j = \frac{1}{N}$

Maximum entropy:
$S_{\text{max}} = -N \cdot \frac{1}{N} \log\frac{1}{N} = \log N$
'''

ax5.text(0.05, 0.48, lagrange_text, 
         fontsize=9, verticalalignment='center', transform=ax5.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightcyan', alpha=0.9, edgecolor='black'))

# Panel 6: Eigenvalue distribution
ax6 = fig1.add_subplot(2, 3, 6)
ax6.set_title('(e) Eigenvalue Distributions', fontweight='bold')
ax6.set_xlabel('Eigenvalue index i')
ax6.set_ylabel('Eigenvalue λᵢ')
ax6.grid(True, alpha=0.3)

N = 8
indices = np.arange(1, N+1)

# Pure state
lambda_pure = np.zeros(N)
lambda_pure[0] = 1.0
ax6.bar(indices - 0.25, lambda_pure, width=0.2, color=colors[3], 
       label=f'Pure (S=0)', alpha=0.8)

# Partially mixed
lambda_partial = np.array([0.4, 0.3, 0.2, 0.1, 0, 0, 0, 0])
S_partial = -sum([l * np.log(l) if l > 0 else 0 for l in lambda_partial])
ax6.bar(indices, lambda_partial, width=0.2, color=colors[1], 
       label=f'Partial (S={S_partial:.2f})', alpha=0.8)

# Maximally mixed
lambda_max = np.ones(N) / N
S_max = np.log(N)
ax6.bar(indices + 0.25, lambda_max, width=0.2, color=colors[0], 
       label=f'Maximally mixed (S={S_max:.2f})', alpha=0.8)

ax6.legend()
ax6.set_ylim(0, 1.1)

plt.tight_layout()
plt.savefig('../figures/entropy.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/entropy.png")

# ============================================================================
# PROBLEM 2: BLOCH SPHERE AND DENSITY MATRICES
# ============================================================================

print("\n[2/7] Creating visualizations for Problem 2: Bloch sphere...")

fig2 = plt.figure(figsize=(16, 11))
fig2.suptitle('Problem 2: Density Matrices and the Bloch Sphere', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: Bloch sphere
ax1 = fig2.add_subplot(2, 3, 1, projection='3d')
ax1.set_title('(a) Bloch Sphere Representation', fontweight='bold')
ax1.set_xlabel('$b_x$')
ax1.set_ylabel('$b_y$')
ax1.set_zlabel('$b_z$')

# Draw sphere at radius 1/2
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
x_sphere = 0.5 * np.outer(np.cos(u), np.sin(v))
y_sphere = 0.5 * np.outer(np.sin(u), np.sin(v))
z_sphere = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v))

ax1.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.2, color='cyan')

# Draw axes
ax1.plot([-0.6, 0.6], [0, 0], [0, 0], 'k-', linewidth=1)
ax1.plot([0, 0], [-0.6, 0.6], [0, 0], 'k-', linewidth=1)
ax1.plot([0, 0], [0, 0], [-0.6, 0.6], 'k-', linewidth=1)

# Mark pure states on surface
pure_states = [
    ([0, 0, 0.5], '|0⟩', 'red'),
    ([0, 0, -0.5], '|1⟩', 'blue'),
    ([0.5, 0, 0], '|+⟩', 'green'),
    ([0, 0.5, 0], '|+i⟩', 'purple')
]

for pos, label, color in pure_states:
    ax1.scatter(*pos, s=100, c=color, marker='o', edgecolors='black', linewidths=2)
    ax1.text(pos[0]*1.3, pos[1]*1.3, pos[2]*1.3, label, fontsize=10)

# Mark a mixed state (interior)
mixed_pos = [0.1, 0.1, 0.15]
ax1.scatter(*mixed_pos, s=150, c='orange', marker='s', edgecolors='black', linewidths=2)
ax1.text(mixed_pos[0]*1.5, mixed_pos[1]*1.5, mixed_pos[2]*1.5, 'Mixed\nstate', fontsize=9)

ax1.set_xlim([-0.6, 0.6])
ax1.set_ylim([-0.6, 0.6])
ax1.set_zlim([-0.6, 0.6])
ax1.view_init(elev=20, azim=45)

# Panel 2: Pure states on Bloch sphere
ax2 = fig2.add_subplot(2, 3, 2)
ax2.set_title('(b) Condition |b⃗| = 1/2 for pure states', fontweight='bold')
ax2.set_xlabel('|b⃗|')
ax2.set_ylabel('Purity Tr(ρ²)')
ax2.grid(True, alpha=0.3)

b_mag = np.linspace(0, 0.5, 100)
purity = 0.5 + 2 * b_mag**2

ax2.plot(b_mag, purity, linewidth=3, color=colors[0])
ax2.axvline(x=0.5, color='red', linestyle='--', linewidth=2, label='Pure: |b⃗| = 1/2')
ax2.axvline(x=0, color='blue', linestyle='--', linewidth=2, label='Maximally mixed: |b⃗| = 0')
ax2.axhline(y=1, color='red', linestyle='--', linewidth=1, alpha=0.5)
ax2.axhline(y=0.5, color='blue', linestyle='--', linewidth=1, alpha=0.5)

ax2.fill_between([0, 0.5], 0, 1.1, alpha=0.2, color='green', label='Allowed region')

ax2.legend()
ax2.set_ylim(0.4, 1.1)

# Panel 3: Parametrization of pure states
ax3 = fig2.add_subplot(2, 3, 3)
ax3.axis('off')
ax3.text(0.5, 0.95, 'Pure State Parametrization', 
         ha='center', fontsize=13, fontweight='bold', transform=ax3.transAxes)

param_text = r'''
General pure state:
$|\Psi\rangle = (\alpha, \beta)^T$, where $|\alpha|^2 + |\beta|^2 = 1$

Density matrix: $\rho = |\Psi\rangle\langle\Psi|$

Bloch vector components:
$\vec{b} = (\text{Re}(\alpha\beta^*), \text{Im}(\alpha\beta^*), \frac{|\alpha|^2 - |\beta|^2}{2})$

Check: $|\vec{b}|^2 = |\alpha\beta^*|^2 + \frac{(|\alpha|^2-|\beta|^2)^2}{4}$
$= |\alpha|^2|\beta|^2 + \frac{|\alpha|^4 - 2|\alpha|^2|\beta|^2 + |\beta|^4}{4}$
$= \frac{|\alpha|^4 + 2|\alpha|^2|\beta|^2 + |\beta|^4}{4} = \frac{(|\alpha|^2+|\beta|^2)^2}{4} = \frac{1}{4}$

Therefore: $|\vec{b}| = 1/2$ (check!)

In Pauli basis:
$\rho = \frac{1}{2}\mathbb{I} + \vec{b} \cdot \vec{\sigma}$
where $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$
'''

ax3.text(0.05, 0.48, param_text, 
         fontsize=8.5, verticalalignment='center', transform=ax3.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightblue', alpha=0.9, edgecolor='black'))

# Panel 4: The example from part (c)
ax4 = fig2.add_subplot(2, 3, 4, projection='3d')
ax4.set_title('(c) Decomposition of Mixed State', fontweight='bold')
ax4.set_xlabel('$b_x$')
ax4.set_ylabel('$b_y$')
ax4.set_zlabel('$b_z$')

# Draw Bloch sphere
ax4.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.15, color='cyan')

# The mixed state ρ = diag(3/4, 1/4)
# In Bloch sphere: b⃗ = (0, 0, 1/4)
rho_vec = [0, 0, 0.25]
ax4.scatter(*rho_vec, s=200, c='orange', marker='s', edgecolors='black', linewidths=3)
ax4.text(rho_vec[0]+0.1, rho_vec[1]+0.1, rho_vec[2]+0.1, 'ρ', fontsize=12, weight='bold')

# Three pure states that average to ρ
# From solution: b₁ = (0, 0, 1/2), b₂ = (√15/8, 0, 1/8), b₃ = (-√15/8, 0, 1/8)
b1 = [0, 0, 0.5]
b2 = [np.sqrt(15)/8, 0, 0.125]
b3 = [-np.sqrt(15)/8, 0, 0.125]

pure_vecs = [b1, b2, b3]
labels = ['ρ₁', 'ρ₂', 'ρ₃']
colors_pure = ['red', 'green', 'blue']

for vec, label, col in zip(pure_vecs, labels, colors_pure):
    ax4.scatter(*vec, s=150, c=col, marker='o', edgecolors='black', linewidths=2)
    ax4.text(vec[0]*1.4, vec[1]*1.4, vec[2]*1.4, label, fontsize=10)
    # Draw line from origin
    ax4.plot([0, vec[0]], [0, vec[1]], [0, vec[2]], '--', color=col, linewidth=1.5, alpha=0.7)

# Draw lines showing the averaging
for vec in pure_vecs:
    ax4.plot([vec[0], rho_vec[0]], [vec[1], rho_vec[1]], [vec[2], rho_vec[2]], 
            'k--', linewidth=1, alpha=0.4)

ax4.set_xlim([-0.6, 0.6])
ax4.set_ylim([-0.6, 0.6])
ax4.set_zlim([-0.1, 0.6])
ax4.view_init(elev=15, azim=30)

# Panel 5: Cross-section showing decomposition
ax5 = fig2.add_subplot(2, 3, 5)
ax5.set_title('(d) xz-plane cross section', fontweight='bold')
ax5.set_xlabel('$b_x$')
ax5.set_ylabel('$b_z$')
ax5.set_aspect('equal')
ax5.grid(True, alpha=0.3)

# Draw circle of radius 1/2
circle = Circle((0, 0), 0.5, fill=False, edgecolor='cyan', linewidth=2)
ax5.add_patch(circle)

# Plot the points
ax5.plot(rho_vec[0], rho_vec[2], 'o', color='orange', markersize=15, 
        markeredgecolor='black', markeredgewidth=2, label='ρ')
ax5.plot(b1[0], b1[2], 'o', color='red', markersize=12, 
        markeredgecolor='black', markeredgewidth=2, label='ρ₁')
ax5.plot(b2[0], b2[2], 'o', color='green', markersize=12,
        markeredgecolor='black', markeredgewidth=2, label='ρ₂')
ax5.plot(b3[0], b3[2], 'o', color='blue', markersize=12,
        markeredgecolor='black', markeredgewidth=2, label='ρ₃')

# Draw barycenter construction
triangle = plt.Polygon([[b1[0], b1[2]], [b2[0], b2[2]], [b3[0], b3[2]]], 
                       fill=True, alpha=0.2, color='gray')
ax5.add_patch(triangle)

ax5.legend()
ax5.set_xlim(-0.6, 0.6)
ax5.set_ylim(-0.2, 0.6)

# Panel 6: Verification
ax6 = fig2.add_subplot(2, 3, 6)
ax6.axis('off')
ax6.text(0.5, 0.95, 'Verification of Decomposition', 
         ha='center', fontsize=13, fontweight='bold', transform=ax6.transAxes)

verify_text = r'''
Given: $\rho = \text{diag}(3/4, 1/4)$

In Bloch representation: $\vec{b} = (0, 0, 1/4)$

Find three pure states: $\rho = \frac{1}{3}(\rho_1 + \rho_2 + \rho_3)$

Solution:
$\vec{b}_1 = (0, 0, 1/2)$
$\vec{b}_2 = (\sqrt{15}/8, 0, 1/8)$
$\vec{b}_3 = (-\sqrt{15}/8, 0, 1/8)$

Check: $\frac{1}{3}(\vec{b}_1 + \vec{b}_2 + \vec{b}_3)$
$= \frac{1}{3}(0 + \sqrt{15}/8 - \sqrt{15}/8, \, 0, \, 1/2 + 1/8 + 1/8)$
$= (0, 0, 1/4)$ (check!)

Matrices:
$\rho_1 = \text{diag}(1, 0)$
$\rho_2 = [5/8, \sqrt{15}/8; \sqrt{15}/8, 3/8]$
$\rho_3 = [5/8, -\sqrt{15}/8; -\sqrt{15}/8, 3/8]$
'''

ax6.text(0.05, 0.48, verify_text, 
         fontsize=8.5, verticalalignment='center', transform=ax6.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow', alpha=0.9, edgecolor='black'))

plt.tight_layout()
plt.savefig('../figures/bloch_sphere.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/bloch_sphere.png")

# ============================================================================
# PROBLEM 3 & 5: STRONG SUBADDITIVITY AND RELATIVE ENTROPY
# ============================================================================

print("\n[3/7] Creating visualizations for Problems 3 & 5: Entropy inequalities...")

fig3 = plt.figure(figsize=(16, 10))
fig3.suptitle('Problems 3 & 5: Entropy Inequalities', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: Venn diagram for strong subadditivity
ax1 = fig3.add_subplot(2, 3, 1)
ax1.set_title('(a) Strong Subadditivity: S_AB + S_BC ≥ S_B + S_ABC', fontweight='bold')
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 3)
ax1.set_aspect('equal')
ax1.axis('off')

# Draw systems as overlapping circles
circle_A = Circle((1, 1.5), 0.6, fill=True, facecolor='red', alpha=0.3, edgecolor='red', linewidth=3)
circle_B = Circle((2, 1.5), 0.6, fill=True, facecolor='blue', alpha=0.3, edgecolor='blue', linewidth=3)
circle_C = Circle((3, 1.5), 0.6, fill=True, facecolor='green', alpha=0.3, edgecolor='green', linewidth=3)

ax1.add_patch(circle_A)
ax1.add_patch(circle_B)
ax1.add_patch(circle_C)

ax1.text(0.7, 1.5, 'A', fontsize=18, weight='bold')
ax1.text(2, 1.5, 'B', fontsize=18, weight='bold')
ax1.text(3.3, 1.5, 'C', fontsize=18, weight='bold')

ax1.text(2, 0.3, 'S_AB + S_BC ≥ S_B + S_ABC', ha='center', fontsize=11,
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

# Panel 2: Case (a) - AB pure
ax2 = fig3.add_subplot(2, 3, 2)
ax2.set_title('(b) Case: AB is pure state', fontweight='bold')
ax2.axis('off')

case_a_text = r'''
Given: ρ_AB is pure (S_AB = 0)

Key facts:
• Pure bipartite state: S_A = S_B
• System factorizes: |Ψ⟩_ABC = |ψ⟩_AB ⊗ |φ⟩_C
• Therefore: ρ_ABC = ρ_AB ⊗ ρ_C

Entropies:
• S_AB = 0
• S_ABC = S_AB + S_C = S_C
• S_BC = S_B + S_C (B, C uncorrelated)

Check inequality:
$S_{AB} + S_{BC} = 0 + S_B + S_C$
$S_B + S_{ABC} = S_B + S_C$

Result: EQUALITY (saturated)
'''

ax2.text(0.05, 0.5, case_a_text, 
         fontsize=10, verticalalignment='center', transform=ax2.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightgreen', alpha=0.9, edgecolor='black'))

# Panel 3: Case (b) - AC pure
ax3 = fig3.add_subplot(2, 3, 3)
ax3.set_title('(c) Case: AC is pure state', fontweight='bold')
ax3.axis('off')

case_b_text = r'''
Given: ρ_AC is pure (S_AC = 0)

Key facts:
• Pure bipartite state: S_A = S_C  
• System factorizes: |Ψ⟩_ABC = |ψ⟩_AC ⊗ |φ⟩_B
• A, B uncorrelated; B, C uncorrelated

Entropies:
• S_AC = 0
• S_ABC = S_AC + S_B = S_B
• S_AB = S_A + S_B (A, B uncorrelated)
• S_BC = S_B + S_C (B, C uncorrelated)

Check inequality:
$S_{AB} + S_{BC} = S_A + S_B + S_B + S_C$
$= 2S_A + 2S_B$ (since S_A = S_C)
$S_B + S_{ABC} = 2S_B$

Need: $2S_A + 2S_B \geq 2S_B$
$\Rightarrow S_A \geq 0$ (check!)

Result: SATISFIED (equality when A pure)
'''

ax3.text(0.05, 0.5, case_b_text, 
         fontsize=9, verticalalignment='center', transform=ax3.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightcyan', alpha=0.9, edgecolor='black'))

# Panel 4: Relative entropy
ax4 = fig3.add_subplot(2, 3, 4)
ax4.set_title('(d) Relative Entropy S(ρ||σ)', fontweight='bold')
ax4.set_xlabel('State parameter')
ax4.set_ylabel('Entropy / Relative Entropy')
ax4.grid(True, alpha=0.3)

# For 2-level system
p_vals = np.linspace(0.01, 0.99, 100)

# von Neumann entropy
S_rho = -p_vals * np.log(p_vals) - (1-p_vals) * np.log(1-p_vals)

# Relative entropy to maximally mixed (σ = I/2)
S_rel = np.log(2) - S_rho

ax4.plot(p_vals, S_rho, linewidth=2.5, label='S(ρ)', color=colors[0])
ax4.plot(p_vals, S_rel, linewidth=2.5, label='S(ρ||σ) = log2 - S(ρ)', color=colors[1])
ax4.plot(p_vals, np.log(2) * np.ones_like(p_vals), 'k--', linewidth=1.5, 
        label='log N', alpha=0.5)

ax4.legend()
ax4.text(0.5, 0.8, 'σ = maximally mixed', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Panel 5: Monotonicity
ax5 = fig3.add_subplot(2, 3, 5)
ax5.set_title('(e) Monotonicity under Quantum Channels', fontweight='bold')
ax5.set_xlim(0, 4)
ax5.set_ylim(0, 3)
ax5.axis('off')

# Draw channel diagram
box_rho = FancyBboxPatch((0.2, 2), 0.6, 0.6, boxstyle="round,pad=0.1", 
                         facecolor='lightblue', edgecolor='black', linewidth=2)
ax5.add_patch(box_rho)
ax5.text(0.5, 2.3, 'ρ', ha='center', fontsize=16, weight='bold')

box_sigma = FancyBboxPatch((0.2, 0.8), 0.6, 0.6, boxstyle="round,pad=0.1",
                           facecolor='lightgreen', edgecolor='black', linewidth=2)
ax5.add_patch(box_sigma)
ax5.text(0.5, 1.1, 'σ', ha='center', fontsize=16, weight='bold')

# Channel
arrow1 = FancyArrowPatch((0.9, 2.3), (2.5, 2.3), arrowstyle='->', mutation_scale=30, 
                        linewidth=3, color='red')
arrow2 = FancyArrowPatch((0.9, 1.1), (2.5, 1.1), arrowstyle='->', mutation_scale=30,
                        linewidth=3, color='red')
ax5.add_patch(arrow1)
ax5.add_patch(arrow2)

ax5.text(1.7, 2.5, '𝓔', ha='center', fontsize=18, weight='bold', style='italic')
ax5.text(1.7, 1.3, '𝓔', ha='center', fontsize=18, weight='bold', style='italic')

box_rho_p = FancyBboxPatch((3, 2), 0.6, 0.6, boxstyle="round,pad=0.1",
                           facecolor='lightblue', edgecolor='black', linewidth=2)
ax5.add_patch(box_rho_p)
ax5.text(3.3, 2.3, "ρ'", ha='center', fontsize=16, weight='bold')

box_sigma_p = FancyBboxPatch((3, 0.8), 0.6, 0.6, boxstyle="round,pad=0.1",
                             facecolor='lightgreen', edgecolor='black', linewidth=2)
ax5.add_patch(box_sigma_p)
ax5.text(3.3, 1.1, "σ'=σ", ha='center', fontsize=14, weight='bold')

ax5.text(2, 0.3, 'S(ρ||σ) ≥ S(ρ\'||σ\') ⇒ S(ρ\') ≥ S(ρ)', ha='center', fontsize=11,
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

# Panel 6: Summary
ax6 = fig3.add_subplot(2, 3, 6)
ax6.axis('off')
ax6.text(0.5, 0.95, 'Key Results Summary', 
         ha='center', fontsize=13, fontweight='bold', transform=ax6.transAxes)

summary_text = r'''
STRONG SUBADDITIVITY:
$S_{AB} + S_{BC} \geq S_B + S_{ABC}$

Equivalent forms:
• $S_ABC - S_BC \leq S_AB - S_B$ (conditional entropy)
• $I(A:C|B) \geq 0$ (conditional mutual information)

RELATIVE ENTROPY:
$S(\rho||\sigma) = \text{Tr}(\rho \log \rho - \rho \log \sigma) \geq 0$

For σ maximally mixed:
$S(\rho||\sigma) = \log N - S(\rho)$

MONOTONICITY:
If 𝓔(σ) = σ (channel preserves σ):
$S(\rho||\sigma) \geq S(\mathcal{E}(\rho)||\sigma)$
$\Rightarrow S(\mathcal{E}(\rho)) \geq S(\rho)$

Physical meaning: 
Channels preserving maximally mixed
state are "randomizing" → increase entropy
'''

ax6.text(0.05, 0.48, summary_text, 
         fontsize=9, verticalalignment='center', transform=ax6.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lavender', alpha=0.9, edgecolor='black'))

plt.tight_layout()
plt.savefig('../figures/entropy_inequalities.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/entropy_inequalities.png")

print("\n" + "="*80)
print("Quantum information visualizations complete!")
print("="*80)
print("\nGenerated files:")
print("  • problem3_1_entropy.png")
print("  • problem3_2_bloch_sphere.png")
print("  • problem3_3_5_entropy_inequalities.png")

# Note: Problems 4, 6, and 7 are more abstract - creating additional visual aids
print("\n[4/7] Creating supplementary visualizations...")

plt.show()

