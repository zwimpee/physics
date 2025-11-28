"""
Visualizations for Physics 539 - Problem Set 2
Topics: General Relativity - Null hypersurfaces, Trapped surfaces, Causal structure
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Wedge
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 14

# Color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

print("Generating visualizations for Problem Set 2...")
print("="*80)

# ============================================================================
# PROBLEM 1: NULL HYPERSURFACES AND RAYCHAUDHURI'S EQUATION
# ============================================================================

print("\n[1/3] Creating visualizations for Problem 1: Null hypersurfaces...")

fig1 = plt.figure(figsize=(16, 10))
fig1.suptitle('Problem 1: Null Hypersurfaces and Raychaudhuri Equation', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: Null geodesic congruence
ax1 = fig1.add_subplot(2, 3, 1)
ax1.set_title('(a) Null Geodesic Congruence', fontweight='bold')
ax1.set_xlabel('Spatial coordinate x')
ax1.set_ylabel('Time coordinate t')
ax1.set_xlim(-2, 2)
ax1.set_ylim(0, 4)
ax1.grid(True, alpha=0.3)

# Draw null geodesics
x_init = np.linspace(-1.5, 1.5, 12)
for x0 in x_init:
    t = np.linspace(0, 4, 100)
    x = x0 + t * 0.3  # Slight spreading
    ax1.plot(x, t, 'b-', alpha=0.6, linewidth=1.5)

# Draw initial surface W
ax1.axhline(y=0, color='green', linewidth=3, label='W (u=v=0)')
ax1.fill_between([-2, 2], 0, -0.2, color='green', alpha=0.2)

# Draw null hypersurface Y
ax1.axhline(y=0, color='red', linewidth=3, linestyle='--', label='Y (v=0)')

ax1.legend(loc='upper left')
ax1.text(0, 3.5, 'Null geodesics\ngenerating Y', 
         ha='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Panel 2: Expansion, shear, and convergence
ax2 = fig1.add_subplot(2, 3, 2)
ax2.set_title('(b) Expansion θ vs proper time', fontweight='bold')
ax2.set_xlabel('Affine parameter u')
ax2.set_ylabel('Expansion θ(u)')
ax2.grid(True, alpha=0.3)

u = np.linspace(0, 5, 200)

# Different scenarios
# Focusing (θ < 0 initially, becomes more negative)
theta1 = -0.5 - 0.3 * u - 0.1 * u**2
ax2.plot(u, theta1, label='Strong focusing (R_uu > 0)', linewidth=2.5, color=colors[0])

# Weak focusing
theta2 = 0.3 - 0.2 * u - 0.05 * u**2
ax2.plot(u, theta2, label='Weak focusing', linewidth=2.5, color=colors[1])

# Expansion
theta3 = 1.0 - 0.1 * u
ax2.plot(u, theta3, label='Expansion (defocusing)', linewidth=2.5, color=colors[2])

ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax2.legend()
ax2.set_ylim(-10, 2)

# Add annotation
ax2.annotate('Caustic formation\n(θ → -∞)', 
            xy=(4, -8), xytext=(2, -6),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=9, color='red', weight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

# Panel 3: Raychaudhuri equation
ax3 = fig1.add_subplot(2, 3, 3)
ax3.axis('off')
ax3.text(0.5, 0.9, 'Raychaudhuri Equation', 
         ha='center', fontsize=13, fontweight='bold', transform=ax3.transAxes)

equation_text = '''
For null geodesic congruence:

dθ/du = -θ² - σ_ab·σ^ab + ω_ab·ω^ab - R_ab·k^a·k^b

where:
• θ = expansion scalar
• σₐᵦ = shear tensor
• ωₐᵦ = vorticity tensor  
• kᵃ = null tangent vector

For geodesic, twist-free congruence (ωₐᵦ = 0):

dθ/du = -θ² - σ_ab·σ^ab - R_uu

Key insight: If Rᵤᵤ > 0 (focusing condition),
then θ becomes negative and decreases,
leading to caustic formation.
'''

ax3.text(0.05, 0.5, equation_text, 
         fontsize=10, verticalalignment='center', transform=ax3.transAxes,
         bbox=dict(boxstyle='round,pad=1', facecolor='lightblue', alpha=0.8, edgecolor='black'))

# Panel 4: Phase space trajectory
ax4 = fig1.add_subplot(2, 3, 4)
ax4.set_title('(c) Phase Space: (θ, dθ/du)', fontweight='bold')
ax4.set_xlabel('Expansion θ')
ax4.set_ylabel('Rate of change dθ/du')
ax4.grid(True, alpha=0.3)

theta_vals = np.linspace(-3, 1, 30)
dtheta_vals = np.linspace(-5, 2, 30)
Theta, DTheta = np.meshgrid(theta_vals, dtheta_vals)

# Raychaudhuri equation with simplified form
# dθ/du = -θ² - σ² - R_uu
# For visualization, assume σ² = 0.1, R_uu = 0.2
sigma_sq = 0.1
R_uu = 0.2
DTheta_rhs = -Theta**2 - sigma_sq - R_uu

# Plot vector field
skip = 2
ax4.quiver(Theta[::skip, ::skip], DTheta[::skip, ::skip], 
          np.ones_like(Theta[::skip, ::skip]), 
          DTheta_rhs[::skip, ::skip] - DTheta[::skip, ::skip],
          alpha=0.4, scale=50)

# Plot nullcline
theta_null = np.linspace(-3, 1, 100)
dtheta_null = -theta_null**2 - sigma_sq - R_uu
ax4.plot(theta_null, dtheta_null, 'r-', linewidth=3, label='Nullcline (dθ/du = -θ² - σ² - R_uu)')

# Plot trajectories
for theta0 in [0.5, 0.0, -0.5]:
    u_traj = np.linspace(0, 2, 100)
    theta_traj = []
    theta_current = theta0
    dt = u_traj[1] - u_traj[0]
    
    for i in range(len(u_traj)):
        theta_traj.append(theta_current)
        dtheta = -theta_current**2 - sigma_sq - R_uu
        theta_current += dtheta * dt
        if theta_current < -3:
            break
    
    if len(theta_traj) > 1:
        dtheta_traj = [-t**2 - sigma_sq - R_uu for t in theta_traj]
        ax4.plot(theta_traj, dtheta_traj, 'b-', linewidth=2, alpha=0.7)
        ax4.plot(theta_traj[0], dtheta_traj[0], 'go', markersize=8)

ax4.legend(fontsize=8)
ax4.set_xlim(-3, 1)
ax4.set_ylim(-5, 2)

# Panel 5: 3D visualization of null hypersurface
ax5 = fig1.add_subplot(2, 3, 5, projection='3d')
ax5.set_title('(d) Null Hypersurface Y in 3D', fontweight='bold')
ax5.set_xlabel('x¹')
ax5.set_ylabel('x²')
ax5.set_zlabel('t (time)')

# Create null cone structure
theta = np.linspace(0, 2*np.pi, 50)
t_vals = np.linspace(0, 2, 30)
Theta_3d, T_3d = np.meshgrid(theta, t_vals)

# Expanding null cone
R_3d = T_3d * 0.8
X_3d = R_3d * np.cos(Theta_3d)
Y_3d = R_3d * np.sin(Theta_3d)

ax5.plot_surface(X_3d, Y_3d, T_3d, alpha=0.5, cmap='viridis')

# Initial surface W
theta_w = np.linspace(0, 2*np.pi, 50)
x_w = 0.2 * np.cos(theta_w)
y_w = 0.2 * np.sin(theta_w)
z_w = np.zeros_like(theta_w)
ax5.plot(x_w, y_w, z_w, 'g-', linewidth=3, label='W')

ax5.legend()

# Panel 6: Metric components
ax6 = fig1.add_subplot(2, 3, 6)
ax6.axis('off')
ax6.text(0.5, 0.95, 'Given Metric Structure', 
         ha='center', fontsize=13, fontweight='bold', transform=ax6.transAxes)

metric_text = r'''
$ds^2 = -2e^q dv\,du + g_{AB}(dx^A + c^A dv)(dx^B + c^B dv)$

Coordinates: $(u, v, x^A)$ where $A = 1, \ldots, D-2$

Structure:
• u, v: null coordinates
• $x^A$: transverse coordinates
• v = 0: null hypersurface Y
• u = v = 0: spacelike surface W

Key property at v = 0:
• q independent of u
• Metric adapted to null geodesic congruence

Result from calculation:

$R_{uu} = -\frac{\partial\theta}{\partial u} - \theta^2 - \sigma_{AB}\sigma^{AB}$

This is Raychaudhuri's equation!
'''

ax6.text(0.05, 0.5, metric_text, 
         fontsize=9, verticalalignment='center', transform=ax6.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lavender', alpha=0.9, edgecolor='black'))

plt.tight_layout()
plt.savefig('../figures/null_hypersurfaces.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/null_hypersurfaces.png")

# ============================================================================
# PROBLEM 2: TRAPPED SURFACES
# ============================================================================

print("\n[2/3] Creating visualizations for Problem 2: Trapped surfaces...")

fig2 = plt.figure(figsize=(16, 11))
fig2.suptitle('Problem 2: Trapped Surfaces in Conformally Flat Spacetime', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: The conformal factor
ax1 = fig2.add_subplot(2, 3, 1)
ax1.set_title('(a) Conformal Factor Ω²(t) = t² - 1', fontweight='bold')
ax1.set_xlabel('Time t')
ax1.set_ylabel('Ω²(t)')
ax1.grid(True, alpha=0.3)

t_plot = np.linspace(-3, 3, 500)
omega_sq = t_plot**2 - 1

ax1.plot(t_plot, omega_sq, linewidth=3, color=colors[0])
ax1.axhline(y=0, color='red', linestyle='--', linewidth=2, label='Ω² = 0')
ax1.axvline(x=-1, color='green', linestyle='--', linewidth=2, alpha=0.7)
ax1.axvline(x=1, color='green', linestyle='--', linewidth=2, alpha=0.7, label='t = ±1')
ax1.fill_between(t_plot, omega_sq, 0, where=(omega_sq > 0), alpha=0.3, color='blue', label='Lorentzian (Ω² > 0)')
ax1.fill_between(t_plot, omega_sq, 0, where=(omega_sq < 0), alpha=0.3, color='red', label='Unphysical (Ω² < 0)')

ax1.legend()
ax1.set_ylim(-2, 8)
ax1.set_xlim(-3, 3)

# Panel 2: Expansion of null normals
ax2 = fig2.add_subplot(2, 3, 2)
ax2.set_title('(b) Null Expansions θ₊ and θ₋', fontweight='bold')
ax2.set_xlabel('Time t₀')
ax2.set_ylabel('Expansion θ')
ax2.grid(True, alpha=0.3)

t0_vals = np.linspace(1.05, 3, 200)
R_test = 0.5

# D = 4 (3+1 dimensional spacetime)
D = 4

# Outgoing expansion
theta_plus = (D - 2) * (1/R_test + t0_vals/(t0_vals**2 - 1))

# Ingoing expansion
theta_minus = (D - 2) * (-1/R_test + t0_vals/(t0_vals**2 - 1))

ax2.plot(t0_vals, theta_plus, linewidth=2.5, label='θ₊ (outgoing)', color=colors[0])
ax2.plot(t0_vals, theta_minus, linewidth=2.5, label='θ₋ (ingoing)', color=colors[1])
ax2.axhline(y=0, color='black', linestyle='--', linewidth=1.5, alpha=0.5)

# Mark trapped region
t_crit = np.sqrt(1 + R_test**2)
ax2.axvline(x=t_crit, color='red', linestyle='--', linewidth=2, alpha=0.7)
ax2.fill_between([1, t_crit], -10, 10, alpha=0.2, color='red', label='Trapped region')

ax2.legend()
ax2.set_ylim(-3, 5)
ax2.text(1.3, 3, f'R = {R_test}', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Panel 3: Trapped surface diagram
ax3 = fig2.add_subplot(2, 3, 3)
ax3.set_title('(c) Trapped vs Non-trapped Regions', fontweight='bold')
ax3.set_xlabel('Radius R')
ax3.set_ylabel('Time |t₀|')
ax3.grid(True, alpha=0.3)

R_range = np.linspace(0.01, 2, 200)
t_range = np.linspace(1.01, 3, 200)
R_grid, T_grid = np.meshgrid(R_range, t_range)

# Condition: R > |t0| - 1/|t0| for trapped
T_boundary = R_grid + 1/R_grid  # Solving R = t - 1/t

# Create regions
trapped = T_grid > (R_grid + 1/R_grid)

ax3.contourf(R_grid, T_grid, trapped.astype(float), levels=[0, 0.5, 1], 
            colors=['lightblue', 'lightcoral'], alpha=0.6)
ax3.contour(R_grid, T_grid, trapped.astype(float), levels=[0.5], 
           colors=['red'], linewidths=3)

# Plot boundary curve
R_boundary = np.linspace(0.01, 2, 200)
t_boundary_vals = R_boundary + 1/R_boundary
ax3.plot(R_boundary, t_boundary_vals, 'r-', linewidth=3, label='Boundary: R = |t₀| - 1/|t₀|')

ax3.text(1.5, 2.7, 'TRAPPED\n(both θ₊, θ₋ < 0)', ha='center', fontsize=10, 
        bbox=dict(boxstyle='round', facecolor='red', alpha=0.6))
ax3.text(0.4, 1.3, 'NOT TRAPPED', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

ax3.legend()
ax3.set_xlim(0, 2)
ax3.set_ylim(1, 3)

# Panel 4: Penrose diagram representation
ax4 = fig2.add_subplot(2, 3, 4)
ax4.set_title('(d) Causal Structure (Schematic)', fontweight='bold')
ax4.set_xlabel('Spatial coordinate')
ax4.set_ylabel('Time')
ax4.set_xlim(-2, 2)
ax4.set_ylim(-0.5, 3.5)
ax4.grid(True, alpha=0.3)

# Draw light cones at different positions
times = [0.5, 1.5, 2.5]
positions = [0, 0, 0]

for t, x in zip(times, positions):
    # Light cone opening
    if t < 1:
        opening = 0.3  # Unphysical region
    else:
        omega_sq_val = t**2 - 1
        opening = 0.5 * np.sqrt(omega_sq_val)
    
    # Draw light cone
    cone_t = np.linspace(t, t + 0.5, 20)
    cone_x_plus = x + opening * (cone_t - t) / 0.5
    cone_x_minus = x - opening * (cone_t - t) / 0.5
    
    ax4.plot(cone_x_plus, cone_t, 'b-', linewidth=1.5, alpha=0.7)
    ax4.plot(cone_x_minus, cone_t, 'b-', linewidth=1.5, alpha=0.7)
    ax4.plot([x], [t], 'ko', markersize=5)

# Mark special times
ax4.axhline(y=1, color='red', linestyle='--', linewidth=2, alpha=0.7, label='t = 1 (Ω² = 0)')

# Draw trapped surface
theta_trap = np.linspace(0, 2*np.pi, 50)
R_trap = 0.8
t_trap = 2.0
x_trap = R_trap * np.cos(theta_trap)
y_trap = t_trap + 0.1 * np.sin(theta_trap)
ax4.fill_between(x_trap, t_trap - 0.1, t_trap + 0.1, alpha=0.5, color='red')
ax4.text(0, t_trap + 0.3, 'Trapped surface', ha='center', 
        bbox=dict(boxstyle='round', facecolor='red', alpha=0.6))

ax4.legend()

# Panel 5: 3D spacetime diagram
ax5 = fig2.add_subplot(2, 3, 5, projection='3d')
ax5.set_title('(e) Trapped Surface in 3D', fontweight='bold')
ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.set_zlabel('t')

# Draw sphere at t = t0
t0_3d = 2.0
R_3d = 1.0
theta_3d = np.linspace(0, 2*np.pi, 40)
phi_3d = np.linspace(0, np.pi, 40)
Theta_3d, Phi_3d = np.meshgrid(theta_3d, phi_3d)

X_sphere = R_3d * np.sin(Phi_3d) * np.cos(Theta_3d)
Y_sphere = R_3d * np.sin(Phi_3d) * np.sin(Theta_3d)
Z_sphere = t0_3d + 0 * X_sphere

# Check if trapped
if R_3d > t0_3d - 1/t0_3d:
    color_surface = 'red'
    label_surface = 'Trapped Surface'
else:
    color_surface = 'blue'
    label_surface = 'Non-trapped Surface'

ax5.plot_surface(X_sphere, Y_sphere, Z_sphere, alpha=0.6, color=color_surface)

# Draw null rays
for angle in np.linspace(0, 2*np.pi, 12):
    t_ray = np.linspace(t0_3d, t0_3d + 0.8, 20)
    x_ray = R_3d * np.cos(angle) + (t_ray - t0_3d) * np.cos(angle) * 0.3
    y_ray = R_3d * np.sin(angle) + (t_ray - t0_3d) * np.sin(angle) * 0.3
    ax5.plot(x_ray, y_ray, t_ray, 'g-', linewidth=1, alpha=0.5)

ax5.text2D(0.5, 0.95, label_surface, transform=ax5.transAxes, 
          ha='center', bbox=dict(boxstyle='round', facecolor=color_surface, alpha=0.6))

# Panel 6: Metric and results
ax6 = fig2.add_subplot(2, 3, 6)
ax6.axis('off')
ax6.text(0.5, 0.95, 'Problem Setup & Results', 
         ha='center', fontsize=13, fontweight='bold', transform=ax6.transAxes)

results_text = r'''
Metric: $ds^2 = (t^2 - 1)(-dt^2 + d\vec{x}^2)$

Conformal to Minkowski: $g_{\mu\nu} = \Omega^2(t) \eta_{\mu\nu}$
where $\Omega^2(t) = t^2 - 1$

Surface W: $t = t_0$, $|\vec{x}| = R$

Null expansions:
$\theta_+ = (D-2)\left(\frac{1}{R} + \frac{t_0}{t_0^2-1}\right)$
$\theta_- = (D-2)\left(-\frac{1}{R} + \frac{t_0}{t_0^2-1}\right)$

TRAPPED SURFACE CONDITION:
Both $\theta_+ < 0$ and $\theta_- < 0$

This requires:
$|t_0| > 1$ and $R > |t_0| - \frac{1}{|t_0|}$

Physical interpretation:
The conformal factor creates effective
"gravitational focusing" when $t_0$ is large
and surface radius R is sufficiently large.
'''

ax6.text(0.05, 0.48, results_text, 
         fontsize=9, verticalalignment='center', transform=ax6.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow', alpha=0.9, edgecolor='black'))

plt.tight_layout()
plt.savefig('../figures/trapped_surfaces.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/trapped_surfaces.png")

# ============================================================================
# PROBLEM 3: CAUSAL FUTURES AND BOUNDARIES
# ============================================================================

print("\n[3/3] Creating visualizations for Problem 3: Causal futures...")

fig3 = plt.figure(figsize=(16, 10))
fig3.suptitle('Problem 3: Boundaries of Causal Futures', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: Simple example in 2D Minkowski
ax1 = fig3.add_subplot(2, 3, 1)
ax1.set_title('(a) Causal Future of Region Q', fontweight='bold')
ax1.set_xlabel('Space x')
ax1.set_ylabel('Time t')
ax1.set_xlim(-3, 3)
ax1.set_ylim(-0.5, 4)
ax1.grid(True, alpha=0.3)
ax1.set_aspect('equal')

# Draw region Q on spacelike surface
Q_x = np.linspace(-1.5, 1.5, 100)
Q_t = np.zeros_like(Q_x)
ax1.fill_between(Q_x, -0.1, 0.1, color='green', alpha=0.4, label='Q')
ax1.plot(Q_x, Q_t, 'g-', linewidth=3)

# Draw boundary ∂Q
ax1.plot([-1.5, -1.5], [-0.1, 0.1], 'r-', linewidth=4, label='∂Q')
ax1.plot([1.5, 1.5], [-0.1, 0.1], 'r-', linewidth=4)

# Draw light cones from boundary points
for x0 in [-1.5, 1.5]:
    t_cone = np.linspace(0, 3.5, 100)
    x_plus = x0 + t_cone
    x_minus = x0 - t_cone
    ax1.plot(x_plus, t_cone, 'r--', linewidth=1.5, alpha=0.6)
    ax1.plot(x_minus, t_cone, 'r--', linewidth=1.5, alpha=0.6)

# Fill J+(Q)
t_fill = np.linspace(0, 3.5, 100)
x_left = -1.5 - t_fill
x_right = 1.5 + t_fill
ax1.fill_betweenx(t_fill, x_left, x_right, alpha=0.2, color='blue', label='J⁺(Q)')

# Mark a point on boundary
p_x, p_t = 3, 1.5
ax1.plot(p_x, p_t, 'ko', markersize=10, label='p ∈ ∂J⁺(Q)')

ax1.legend(loc='upper left')

# Panel 2: Zoomed view near boundary
ax2 = fig3.add_subplot(2, 3, 2)
ax2.set_title('(b) Boundary ∂J⁺(Q) is generated by ∂Q', fontweight='bold')
ax2.set_xlabel('Space x')
ax2.set_ylabel('Time t')
ax2.set_xlim(0.5, 3.5)
ax2.set_ylim(0.5, 2.5)
ax2.grid(True, alpha=0.3)
ax2.set_aspect('equal')

# Draw boundary ∂Q point
ax2.plot([1.5], [0], 'ro', markersize=12, label='Point on ∂Q', zorder=5)

# Draw null geodesic from ∂Q to p
t_null = np.linspace(0, 1.5, 50)
x_null = 1.5 + t_null
ax2.plot(x_null, t_null, 'r-', linewidth=3, label='Null geodesic from ∂Q')

# Point p
ax2.plot(p_x, p_t, 'ko', markersize=10, label='p ∈ ∂J⁺(∂Q)', zorder=5)

# Draw small neighborhood around p
circle_p = Circle((p_x, p_t), 0.3, fill=False, edgecolor='blue', linewidth=2, linestyle='--')
ax2.add_patch(circle_p)
ax2.text(p_x + 0.5, p_t, 'Neighborhood of p\nintersects both\nJ⁺(Q) and its complement', 
        fontsize=8, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax2.legend(loc='upper left', fontsize=8)

# Panel 3: Interior vs boundary points
ax3 = fig3.add_subplot(2, 3, 3)
ax3.set_title('(c) Interior vs Boundary Points', fontweight='bold')
ax3.set_xlabel('Space x')
ax3.set_ylabel('Time t')
ax3.set_xlim(-2, 4)
ax3.set_ylim(-0.5, 3)
ax3.grid(True, alpha=0.3)
ax3.set_aspect('equal')

# Draw Q
Q_x2 = np.linspace(-1, 1, 100)
ax3.fill_between(Q_x2, -0.1, 0.1, color='green', alpha=0.4)

# Draw J+(Q) region
t_fill2 = np.linspace(0, 2.5, 100)
x_left2 = -1 - t_fill2
x_right2 = 1 + t_fill2
ax3.fill_betweenx(t_fill2, x_left2, x_right2, alpha=0.15, color='blue')

# Mark interior point (timelike future)
p_interior = (0.5, 1.0)
ax3.plot(*p_interior, 'bs', markersize=12, label='Interior point\n(timelike from Q)', zorder=5)

# Mark boundary point
p_boundary = (2.5, 1.5)
ax3.plot(*p_boundary, 'ro', markersize=12, label='Boundary point\n(null from ∂Q)', zorder=5)

# Draw past light cone of interior point
t_cone_int = np.linspace(0, p_interior[1], 50)
x_plus_int = p_interior[0] + (p_interior[1] - t_cone_int)
x_minus_int = p_interior[0] - (p_interior[1] - t_cone_int)
ax3.fill_betweenx(t_cone_int, x_minus_int, x_plus_int, alpha=0.2, color='blue')

ax3.legend(fontsize=8)

# Panel 4: Proof diagram
ax4 = fig3.add_subplot(2, 3, 4)
ax4.axis('off')
ax4.text(0.5, 0.95, 'Proof Strategy', 
         ha='center', fontsize=13, fontweight='bold', transform=ax4.transAxes)

proof_text = '''
Theorem: If p ∈ ∂J⁺(Q) and p ∉ Q, then p ∈ ∂J⁺(∂Q)

Proof outline:

1. Since p ∈ ∂J⁺(Q):
   • p is on the boundary of causal future
   • Can be reached by null geodesic from Q
   
2. Null geodesic γ: [0,1] → M from q ∈ Q to p

3. Suppose q ∈ Int(Q) (interior):
   • Small neighborhood U of q with U ⊂ Q
   • Can deform γ to start at points in U
   • This puts p in Int(J⁺(Q))
   • Contradiction! (p should be on boundary)
   
4. Therefore: q ∈ ∂Q

5. Thus p ∈ J⁺(∂Q), and by tangency
   arguments, p ∈ ∂J⁺(∂Q)

Key insight: Boundary of causal future is
generated by null geodesics from boundary
of original region.
'''

ax4.text(0.05, 0.5, proof_text, 
         fontsize=9, verticalalignment='center', transform=ax4.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightcyan', alpha=0.9, edgecolor='black'))

# Panel 5: 3D visualization
ax5 = fig3.add_subplot(2, 3, 5, projection='3d')
ax5.set_title('(d) Causal Future in 3D Spacetime', fontweight='bold')
ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.set_zlabel('t')

# Draw spatial region Q (disk)
theta_q = np.linspace(0, 2*np.pi, 50)
r_q = 1.0
x_q = r_q * np.cos(theta_q)
y_q = r_q * np.sin(theta_q)
z_q = np.zeros_like(theta_q)

ax5.plot(x_q, y_q, z_q, 'g-', linewidth=3)
theta_fill = np.linspace(0, 2*np.pi, 30)
r_fill = np.linspace(0, r_q, 10)
Theta_fill, R_fill = np.meshgrid(theta_fill, r_fill)
X_fill = R_fill * np.cos(Theta_fill)
Y_fill = R_fill * np.sin(Theta_fill)
Z_fill = np.zeros_like(X_fill)
ax5.plot_surface(X_fill, Y_fill, Z_fill, alpha=0.3, color='green')

# Draw future light cone from boundary
t_cone_3d = np.linspace(0, 1.5, 20)
for angle in np.linspace(0, 2*np.pi, 16):
    x_cone = r_q * np.cos(angle) + t_cone_3d * np.cos(angle) * 0.5
    y_cone = r_q * np.sin(angle) + t_cone_3d * np.sin(angle) * 0.5
    ax5.plot(x_cone, y_cone, t_cone_3d, 'r-', linewidth=1, alpha=0.4)

# Panel 6: Application to black holes
ax6 = fig3.add_subplot(2, 3, 6)
ax6.axis('off')
ax6.text(0.5, 0.95, 'Application: Black Hole Event Horizons', 
         ha='center', fontsize=13, fontweight='bold', transform=ax6.transAxes)

application_text = '''
This result is crucial for black hole physics:

Event Horizon:
The event horizon is ∂J⁻(I⁺), the boundary
of the past of future null infinity.

Key consequence of this theorem:
If a region Q is trapped, the boundary of its
causal future is determined by the boundary ∂Q.

For black holes:
• Once inside event horizon, all future-directed
  paths remain inside
  
• Event horizon is generated by null geodesics
  that neither escape nor fall in
  
• These null generators come from the boundary
  of the trapped region

Penrose-Hawking Singularity Theorems:
Use this result to show that trapped surfaces
lead to singularities - the focusing of null
geodesics (Raychaudhuri equation) causes the
generators of ∂J⁺(Q) to develop caustics.

Connection to Problem 1:
Raychaudhuri → focusing → caustics → singularity
'''

ax6.text(0.05, 0.48, application_text, 
         fontsize=8, verticalalignment='center', transform=ax6.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow', alpha=0.9, edgecolor='black'))

plt.tight_layout()
plt.savefig('../figures/causal_futures.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/causal_futures.png")

print("\n" + "="*80)
print("All Problem Set 2 visualizations complete!")
print("="*80)
print("\nGenerated files:")
print("  • problem2_1_null_hypersurfaces.png")
print("  • problem2_2_trapped_surfaces.png")
print("  • problem2_3_causal_futures.png")

plt.show()  # Commented out to avoid blocking on Windows

