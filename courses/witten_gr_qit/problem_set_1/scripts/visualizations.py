"""
Visualization of Problem 1: Convergence of curves x = sin(πnt) in Minkowski space

This script visualizes the curves γ_n and their behavior as n increases,
helping to illustrate why they converge to the constant curve at q when
parametrized by Euclidean arclength.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import cumulative_trapezoid

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 16

# Define a nice color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Set up the figure with better spacing
fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle('Curves γ_n: x = sin(πnt) in Minkowski Space', fontsize=18, fontweight='bold', y=0.995)

# Parameters
t_max = 1.0
t = np.linspace(0, t_max, 5000)
n_values = [1, 3, 10, 30]

# Plot 1: Curves in (t, x) coordinates
ax1 = axes[0, 0]
ax1.set_title('(a) Curves in (t, x) coordinates', fontweight='bold', pad=10)
ax1.set_xlabel('Time t', fontsize=12)
ax1.set_ylabel('Position x', fontsize=12)
ax1.grid(True, alpha=0.25, linestyle='--', linewidth=0.7)
ax1.plot(0, 0, 'o', color='green', markersize=12, label='q = (0, 0)', zorder=5, 
         markeredgecolor='darkgreen', markeredgewidth=2)
ax1.plot(1, 0, 'o', color='red', markersize=12, label='p = (1, 0)', zorder=5,
         markeredgecolor='darkred', markeredgewidth=2)

for i, n in enumerate(n_values):
    x = np.sin(np.pi * n * t)
    ax1.plot(t, x, label=f'n = {n}', alpha=0.8, linewidth=2.5, color=colors[i])

ax1.legend(loc='upper right', framealpha=0.95, edgecolor='black')
ax1.set_xlim(-0.05, 1.05)
ax1.set_ylim(-1.2, 1.2)
ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.3)

# Plot 2: Euclidean arclength as function of t
ax2 = axes[0, 1]
ax2.set_title('(b) Euclidean arclength s(t) for different n', fontweight='bold', pad=10)
ax2.set_xlabel('Time t', fontsize=12)
ax2.set_ylabel('Euclidean arclength s', fontsize=12)
ax2.grid(True, alpha=0.25, linestyle='--', linewidth=0.7)

for i, n in enumerate(n_values):
    dx_dt = np.pi * n * np.cos(np.pi * n * t)
    ds_dt = np.sqrt(1 + dx_dt**2)
    # Compute cumulative arclength
    s = np.zeros_like(t)
    s[1:] = cumulative_trapezoid(ds_dt, t)
    ax2.plot(t, s, label=f'n = {n}', alpha=0.8, linewidth=2.5, color=colors[i])

ax2.legend(loc='upper left', framealpha=0.95, edgecolor='black')
ax2.set_xlim(0, 1)
# Add annotation
ax2.text(0.65, ax2.get_ylim()[1] * 0.4, 'Larger n →\nmore arclength\nfor same t', 
         bbox=dict(boxstyle='round,pad=0.7', facecolor='wheat', alpha=0.8, edgecolor='black'),
         fontsize=10, verticalalignment='center')

# Plot 3: Curves parametrized by Euclidean arclength (first part)
ax3 = axes[1, 0]
ax3.set_title('(c) Curves parametrized by arclength s ∈ [0, 5]', fontweight='bold', pad=10)
ax3.set_xlabel('Time t(s)', fontsize=12)
ax3.set_ylabel('Position x(s)', fontsize=12)
ax3.grid(True, alpha=0.25, linestyle='--', linewidth=0.7)
ax3.plot(0, 0, 'o', color='green', markersize=12, label='q = (0, 0)', zorder=5,
         markeredgecolor='darkgreen', markeredgewidth=2)

s_max_plot = 5.0  # Maximum arclength to plot

n_extended = [1, 3, 10, 30, 100]
for i, n in enumerate(n_extended):
    dx_dt = np.pi * n * np.cos(np.pi * n * t)
    ds_dt = np.sqrt(1 + dx_dt**2)
    
    # Compute arclength
    s = np.zeros_like(t)
    s[1:] = cumulative_trapezoid(ds_dt, t)
    
    # Interpolate to get t as function of s
    s_uniform = np.linspace(0, min(s[-1], s_max_plot), 1000)
    if s[-1] > s_uniform[-1]:
        t_of_s = np.interp(s_uniform, s, t)
        x_of_s = np.sin(np.pi * n * t_of_s)
        color_idx = i if i < len(colors) else i % len(colors)
        ax3.plot(t_of_s, x_of_s, label=f'n = {n}', alpha=0.8, linewidth=2.2, color=colors[color_idx])

ax3.legend(loc='upper left', framealpha=0.95, edgecolor='black', ncol=1)
ax3.set_xlim(-0.005, 0.15)
ax3.set_ylim(-0.25, 0.25)
# Add annotation showing convergence
ax3.annotate('As n → ∞,\ncurves stay\nnear q', 
            xy=(0.01, 0.05), xytext=(0.08, 0.18),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, color='darkred',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.8, edgecolor='black'))

# Plot 4: Position at fixed arclength vs n
ax4 = axes[1, 1]
ax4.set_title('(d) Time coordinate t(s) for fixed arclength s', fontweight='bold', pad=10)
ax4.set_xlabel('Curve index n', fontsize=12)
ax4.set_ylabel('Time t(s) for fixed s', fontsize=12)
ax4.grid(True, alpha=0.25, linestyle='--', linewidth=0.7)

n_range = np.arange(1, 101)
s_fixed_values = [1.0, 2.0, 5.0]

for i, s_fixed in enumerate(s_fixed_values):
    t_at_s = []
    
    for n in n_range:
        t_fine = np.linspace(0, min(1.0, s_fixed / (np.pi * n - 1)), 10000)
        dx_dt = np.pi * n * np.cos(np.pi * n * t_fine)
        ds_dt = np.sqrt(1 + dx_dt**2)
        
        s = np.zeros_like(t_fine)
        s[1:] = cumulative_trapezoid(ds_dt, t_fine)
        
        if s[-1] >= s_fixed:
            t_val = np.interp(s_fixed, s, t_fine)
            t_at_s.append(t_val)
        else:
            t_at_s.append(np.nan)
    
    ax4.plot(n_range, t_at_s, 'o-', label=f's = {s_fixed}', alpha=0.8, 
             markersize=4, linewidth=2, color=colors[i])

ax4.set_xlim(0, 100)
ax4.set_ylim(0, 0.2)
ax4.legend(loc='upper right', framealpha=0.95, edgecolor='black')
ax4.text(50, 0.15, 'As n → ∞, t(s) → 0\nfor any fixed s > 0\n\n→ Curves converge to γ∞(s) = q', 
         bbox=dict(boxstyle='round,pad=0.7', facecolor='lightyellow', alpha=0.9, edgecolor='black'),
         fontsize=10, ha='center')

plt.tight_layout(rect=[0, 0.02, 1, 0.98])
plt.savefig('../figures/curves.png', dpi=200, bbox_inches='tight')
print("[OK] Saved visualization to ../figures/curves.png")

# Create a second figure showing the key insight
fig2, ax = plt.subplots(figsize=(12, 9))
fig2.suptitle('Key Insight: Curves spend more arclength near t = 0 as n increases', 
              fontsize=16, fontweight='bold', y=0.98)

ax.set_xlabel('Euclidean arclength s', fontsize=13)
ax.set_ylabel('Time coordinate t', fontsize=13)
ax.grid(True, alpha=0.25, linestyle='--', linewidth=0.7)

n_insight = [1, 3, 10, 30, 100]
for i, n in enumerate(n_insight):
    t_fine = np.linspace(0, min(1.0, 5.0 / (np.pi * n)), 10000)
    dx_dt = np.pi * n * np.cos(np.pi * n * t_fine)
    ds_dt = np.sqrt(1 + dx_dt**2)
    
    s = np.zeros_like(t_fine)
    s[1:] = cumulative_trapezoid(ds_dt, t_fine)
    
    color_idx = i if i < len(colors) else i % len(colors)
    ax.plot(s, t_fine, label=f'n = {n}', linewidth=3, alpha=0.85, color=colors[color_idx])

ax.axvline(x=2.0, color='darkred', linestyle='--', linewidth=2.5, alpha=0.6, label='Fixed s = 2')
ax.legend(fontsize=11, loc='upper left', framealpha=0.95, edgecolor='black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 0.3)

# Add annotation
ax.annotate('For fixed s, as n → ∞,\nthe time t(s) → 0\n\nLIMIT: γ∞(s) = (0, 0) = q ∀s', 
            xy=(2, 0.05), xytext=(5.5, 0.20),
            arrowprops=dict(arrowstyle='->', color='darkred', lw=3, connectionstyle='arc3,rad=0.3'),
            fontsize=12, color='darkred', weight='bold',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow', alpha=0.95, edgecolor='darkred', linewidth=2))

# Add secondary annotation
ax.text(7, 0.05, 'Each curve "slows down"\nin time as it accumulates\nEuclidean arclength', 
        bbox=dict(boxstyle='round,pad=0.7', facecolor='lightblue', alpha=0.85, edgecolor='black'),
        fontsize=11, ha='center')

plt.tight_layout()
plt.savefig('../figures/insight.png', dpi=200, bbox_inches='tight')
print("[OK] Saved insight visualization to ../figures/insight.png")

plt.show()  # Commented out to avoid blocking on Windows

print("\n" + "="*80)
print(" " * 20 + "INTERPRETATION OF RESULTS")
print("="*80)
print("""
As n increases, the curves gamma_n oscillate more rapidly. When parametrized
by Euclidean arclength:

1. The curves spend increasingly more arclength near t = 0
   (see second figure: t(s) decreases for fixed s as n grows)

2. For any fixed arclength parameter s > 0, the corresponding time t(s) -> 0 
   as n -> infinity

3. Therefore, the sequence converges to the CONSTANT CURVE gamma_infinity(s) = (0, 0)
   that never leaves the initial point q

4. This is consistent with having NO LIMIT as curves from q to p, because
   the limit curve doesn't reach p!

KEY INSIGHT: The resolution of the apparent contradiction is that convergence
depends on parametrization. With Euclidean arclength parametrization, the
limiting object exists but is degenerate—it stays at q forever.
""")

