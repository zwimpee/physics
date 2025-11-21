"""
Visualizations for Physics 539 - Problem Set 3 (Part 2)
Topics: Thermodynamics, Quantum Channels, Kraus Operators
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle, Wedge
from mpl_toolkits.mplot3d import Axes3D

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 14

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

print("Generating supplementary visualizations for Problem Set 3...")
print("="*80)

# ============================================================================
# PROBLEM 4: THERMODYNAMICS
# ============================================================================

print("\n[1/3] Creating visualizations for Problem 4: Thermodynamics...")

fig1 = plt.figure(figsize=(16, 10))
fig1.suptitle('Problem 4: Thermodynamics and First Law', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: Energy levels and thermal distribution
ax1 = fig1.add_subplot(2, 3, 1)
ax1.set_title('(a) Thermal State Energy Distribution', fontweight='bold')
ax1.set_xlabel('Energy Level $E_i$')
ax1.set_ylabel('Occupation Probability $p_i$')
ax1.grid(True, alpha=0.3)

# Sample energy levels
E_levels = np.array([0, 1, 2, 3, 4, 5])
temperatures = [0.5, 1.0, 2.0, 5.0]

for T in temperatures:
    beta = 1/T
    Z = np.sum(np.exp(-beta * E_levels))
    p_i = np.exp(-beta * E_levels) / Z
    ax1.plot(E_levels, p_i, 'o-', linewidth=2.5, markersize=8, label=f'T = {T}')

ax1.legend()
ax1.set_yscale('log')
ax1.set_ylim(0.001, 1)

# Panel 2: Entropy vs Temperature
ax2 = fig1.add_subplot(2, 3, 2)
ax2.set_title('(b) Entropy vs Temperature', fontweight='bold')
ax2.set_xlabel('Temperature T')
ax2.set_ylabel('Entropy S')
ax2.grid(True, alpha=0.3)

T_range = np.linspace(0.1, 10, 200)
S_vals = []

for T in T_range:
    beta = 1/T
    Z = np.sum(np.exp(-beta * E_levels))
    p_i = np.exp(-beta * E_levels) / Z
    S = -np.sum(p_i * np.log(p_i[p_i > 0]))
    S_vals.append(S)

ax2.plot(T_range, S_vals, linewidth=3, color=colors[0])
ax2.axhline(y=np.log(len(E_levels)), color='red', linestyle='--', linewidth=2, 
           label=f'S_max = ln(N) = ln({len(E_levels)})')
ax2.legend()

# Add annotation
ax2.text(5, 1.2, 'High T → Maximally mixed\nLow T → Ground state', 
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Panel 3: Energy vs Temperature
ax3 = fig1.add_subplot(2, 3, 3)
ax3.set_title('(c) Energy vs Temperature', fontweight='bold')
ax3.set_xlabel('Temperature T')
ax3.set_ylabel('Energy E = Tr(ρH)')
ax3.grid(True, alpha=0.3)

E_mean_vals = []

for T in T_range:
    beta = 1/T
    Z = np.sum(np.exp(-beta * E_levels))
    p_i = np.exp(-beta * E_levels) / Z
    E_mean = np.sum(p_i * E_levels)
    E_mean_vals.append(E_mean)

ax3.plot(T_range, E_mean_vals, linewidth=3, color=colors[1])

# Panel 4: dE vs dS showing first law
ax4 = fig1.add_subplot(2, 3, 4)
ax4.set_title('(d) First Law: dE = T dS', fontweight='bold')
ax4.set_xlabel('Entropy S')
ax4.set_ylabel('Energy E')
ax4.grid(True, alpha=0.3)

ax4.plot(S_vals, E_mean_vals, linewidth=3, color=colors[2])

# Add tangent lines at different points to show slope = T
for i in [50, 100, 150]:
    if i < len(S_vals):
        S_point = S_vals[i]
        E_point = E_mean_vals[i]
        T_point = T_range[i]
        
        # Draw tangent
        ds = 0.2
        dE = T_point * ds
        ax4.plot([S_point - ds, S_point + ds], [E_point - dE, E_point + dE], 
                '--', linewidth=2, alpha=0.7, label=f'T = {T_point:.1f}')

ax4.legend()
ax4.text(0.5, 2.5, 'Slope = T at each point', 
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

# Panel 5: Phase space trajectory
ax5 = fig1.add_subplot(2, 3, 5)
ax5.set_title('(e) Thermodynamic Process', fontweight='bold')
ax5.set_xlabel('Time t')
ax5.set_ylabel('T, E, S (normalized)')
ax5.grid(True, alpha=0.3)

# Simulate a time-varying temperature
t_vals = np.linspace(0, 10, 100)
T_t = 1 + 2 * np.sin(2 * np.pi * t_vals / 10)

E_t = []
S_t = []

for T in T_t:
    beta = 1/T
    Z = np.sum(np.exp(-beta * E_levels))
    p_i = np.exp(-beta * E_levels) / Z
    E = np.sum(p_i * E_levels)
    S = -np.sum(p_i * np.log(p_i[p_i > 0]))
    E_t.append(E)
    S_t.append(S)

# Normalize for plotting
ax5.plot(t_vals, T_t / np.max(T_t), linewidth=2.5, label='Temperature T', color=colors[0])
ax5.plot(t_vals, np.array(E_t) / np.max(E_t), linewidth=2.5, label='Energy E', color=colors[1])
ax5.plot(t_vals, np.array(S_t) / np.max(S_t), linewidth=2.5, label='Entropy S', color=colors[2])

ax5.legend()

# Panel 6: Derivation
ax6 = fig1.add_subplot(2, 3, 6)
ax6.axis('off')
ax6.text(0.5, 0.95, 'Derivation of δE = TδS', 
         ha='center', fontsize=13, fontweight='bold', transform=ax6.transAxes)

deriv_text = r'''
Thermal state: $\rho = \frac{1}{Z}e^{-\beta H}$, $\beta = 1/T$

Entropy: $S = -\text{Tr}(\rho \log \rho)$
$= -\text{Tr}(\rho(-\log Z - \beta H))$
$= \log Z + \beta E$

For arbitrary variation δρ (with Tr(δρ) = 0):
$\delta S = -\text{Tr}(\delta\rho \log \rho)$

For thermal state:
$\log \rho = -\log Z - \beta H$

Therefore:
$\delta S = -\text{Tr}(\delta\rho(-\log Z - \beta H))$
$= \text{Tr}(\delta\rho) \log Z + \beta \text{Tr}(\delta\rho H)$
$= 0 + \beta \delta E = \frac{1}{T}\delta E$

Result: $\delta E = T \delta S$

This is the FIRST LAW OF THERMODYNAMICS
for a system at fixed volume (no work term).
'''

ax6.text(0.05, 0.48, deriv_text, 
         fontsize=9, verticalalignment='center', transform=ax6.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightcyan', alpha=0.9, edgecolor='black'))

plt.tight_layout()
plt.savefig('../figures/thermodynamics.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/thermodynamics.png")

# ============================================================================
# PROBLEMS 6 & 7: QUANTUM CHANNELS AND KRAUS OPERATORS
# ============================================================================

print("\n[2/3] Creating visualizations for Problems 6 & 7: Quantum channels...")

fig2 = plt.figure(figsize=(16, 11))
fig2.suptitle('Problems 6 & 7: Quantum Channels and Kraus Operators', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: Channel schematic for Problem 6
ax1 = fig2.add_subplot(2, 3, 1)
ax1.set_title('(a) Channel: ρ → |ψ⟩⟨ψ|', fontweight='bold')
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 4)
ax1.axis('off')

# Draw multiple input states
input_states = [(0.5, 3), (0.5, 2), (0.5, 1)]
labels = ['ρ₁', 'ρ₂', 'ρ₃']

for (x, y), label in zip(input_states, labels):
    box = FancyBboxPatch((x, y), 0.5, 0.5, boxstyle="round,pad=0.05",
                         facecolor='lightblue', edgecolor='black', linewidth=2)
    ax1.add_patch(box)
    ax1.text(x + 0.25, y + 0.25, label, ha='center', va='center', fontsize=14, weight='bold')
    
    # Arrow to channel
    arrow = FancyArrowPatch((x + 0.55, y + 0.25), (1.5, 2), 
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='blue')
    ax1.add_patch(arrow)

# Channel box
channel_box = FancyBboxPatch((1.5, 1.5), 1.2, 1, boxstyle="round,pad=0.1",
                            facecolor='orange', edgecolor='black', linewidth=3)
ax1.add_patch(channel_box)
ax1.text(2.1, 2.3, '𝓔', ha='center', fontsize=24, weight='bold', style='italic')
ax1.text(2.1, 1.8, 'Collapse\nChannel', ha='center', fontsize=9)

# Output state
out_box = FancyBboxPatch((3.5, 1.75), 0.8, 0.5, boxstyle="round,pad=0.05",
                        facecolor='lightgreen', edgecolor='black', linewidth=2)
ax1.add_patch(out_box)
ax1.text(3.9, 2, '|ψ⟩⟨ψ|', ha='center', va='center', fontsize=14, weight='bold')

arrow_out = FancyArrowPatch((2.7, 2), (3.5, 2),
                           arrowstyle='->', mutation_scale=25, linewidth=3, color='green')
ax1.add_patch(arrow_out)

ax1.text(2.5, 0.3, 'All inputs → same pure state', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

# Panel 2: Kraus operators for Problem 6
ax2 = fig2.add_subplot(2, 3, 2)
ax2.axis('off')
ax2.text(0.5, 0.95, 'Kraus Operators for Problem 6', 
         ha='center', fontsize=13, fontweight='bold', transform=ax2.transAxes)

kraus6_text = r'''
Goal: $\mathcal{E}(\rho) = |\psi\rangle\langle\psi|$ for all ρ

Choose orthonormal basis $\{|i\rangle\}$:

KRAUS OPERATORS:
$K_i = |\psi\rangle\langle i|$, for $i = 1, \ldots, N$

Verification:
$\mathcal{E}(\rho) = \sum_{i=1}^N K_i \rho K_i^\dagger$
$= \sum_i |\psi\rangle\langle i|\rho|i\rangle\langle\psi|$
$= |\psi\rangle \left(\sum_i \langle i|\rho|i\rangle\right)\langle\psi|$
$= |\psi\rangle \cdot \text{Tr}(\rho) \cdot \langle\psi|$
$= |\psi\rangle\langle\psi|$ (check!)

Completeness:
$\sum_i K_i^\dagger K_i = \sum_i |i\rangle\langle\psi|\psi\rangle\langle i|$
$= \sum_i |i\rangle\langle i| = \mathbb{I}$ (check!)

Physical interpretation:
Measurement in basis {|i⟩}, then prepare |ψ⟩
regardless of measurement outcome.
'''

ax2.text(0.05, 0.48, kraus6_text, 
         fontsize=9, verticalalignment='center', transform=ax2.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightblue', alpha=0.9, edgecolor='black'))

# Panel 3: Bloch sphere showing collapse
ax3 = fig2.add_subplot(2, 3, 3, projection='3d')
ax3.set_title('(b) Collapse on Bloch Sphere', fontweight='bold')
ax3.set_xlabel('$b_x$')
ax3.set_ylabel('$b_y$')
ax3.set_zlabel('$b_z$')

# Draw Bloch sphere
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 30)
x_sphere = 0.5 * np.outer(np.cos(u), np.sin(v))
y_sphere = 0.5 * np.outer(np.sin(u), np.sin(v))
z_sphere = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v))
ax3.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.15, color='cyan')

# Show several initial states
initial_states = [
    [0.3, 0.2, 0.1],
    [-0.2, 0.3, -0.1],
    [0.1, -0.2, 0.3]
]

# Target state
target = [0, 0, 0.5]

for init in initial_states:
    ax3.scatter(*init, s=100, c='blue', marker='o', alpha=0.7)
    # Arrow to target
    ax3.plot([init[0], target[0]], [init[1], target[1]], [init[2], target[2]], 
            'b--', linewidth=1.5, alpha=0.5)

ax3.scatter(*target, s=300, c='red', marker='*', edgecolors='black', linewidths=2)
ax3.text(target[0]+0.1, target[1]+0.1, target[2]+0.1, '|ψ⟩', fontsize=12, weight='bold')

ax3.view_init(elev=20, azim=45)

# Panel 4: Channel schematic for Problem 7
ax4 = fig2.add_subplot(2, 3, 4)
ax4.set_title('(c) Channel: ρ → 𝕀/N (maximally mixed)', fontweight='bold')
ax4.set_xlim(0, 5)
ax4.set_ylim(0, 4)
ax4.axis('off')

# Draw multiple input states
for (x, y), label in zip(input_states, labels):
    box = FancyBboxPatch((x, y), 0.5, 0.5, boxstyle="round,pad=0.05",
                         facecolor='lightblue', edgecolor='black', linewidth=2)
    ax4.add_patch(box)
    ax4.text(x + 0.25, y + 0.25, label, ha='center', va='center', fontsize=14, weight='bold')
    
    arrow = FancyArrowPatch((x + 0.55, y + 0.25), (1.5, 2),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='blue')
    ax4.add_patch(arrow)

# Channel box
channel_box = FancyBboxPatch((1.5, 1.5), 1.2, 1, boxstyle="round,pad=0.1",
                            facecolor='purple', edgecolor='black', linewidth=3, alpha=0.7)
ax4.add_patch(channel_box)
ax4.text(2.1, 2.3, '𝓔', ha='center', fontsize=24, weight='bold', style='italic')
ax4.text(2.1, 1.8, 'Complete\nDephasing', ha='center', fontsize=9)

# Output state
out_box = FancyBboxPatch((3.5, 1.75), 0.8, 0.5, boxstyle="round,pad=0.05",
                        facecolor='gray', edgecolor='black', linewidth=2, alpha=0.7)
ax4.add_patch(out_box)
ax4.text(3.9, 2, '𝕀/N', ha='center', va='center', fontsize=14, weight='bold')

arrow_out = FancyArrowPatch((2.7, 2), (3.5, 2),
                           arrowstyle='->', mutation_scale=25, linewidth=3, color='purple')
ax4.add_patch(arrow_out)

ax4.text(2.5, 0.3, 'All inputs → maximally mixed', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

# Panel 5: Kraus operators for Problem 7
ax5 = fig2.add_subplot(2, 3, 5)
ax5.axis('off')
ax5.text(0.5, 0.95, 'Kraus Operators for Problem 7', 
         ha='center', fontsize=13, fontweight='bold', transform=ax5.transAxes)

kraus7_text = r'''
Goal: $\mathcal{E}(\rho) = \frac{1}{N}\mathbb{I}$ for all ρ

KRAUS OPERATORS:
$K_{ij} = \frac{1}{\sqrt{N}}|i\rangle\langle j|$
for all $i, j = 1, \ldots, N$

This gives $N^2$ Kraus operators total.

Verification:
$\mathcal{E}(\rho) = \sum_{i,j} K_{ij} \rho K_{ij}^\dagger$
$= \frac{1}{N}\sum_{i,j} |i\rangle\langle j|\rho|j\rangle\langle i|$
$= \frac{1}{N}\sum_i |i\rangle\left(\sum_j \langle j|\rho|j\rangle\right)\langle i|$
$= \frac{1}{N}\sum_i |i\rangle \cdot \text{Tr}(\rho) \cdot \langle i|$
$= \frac{1}{N}\mathbb{I}$ (check!)

Completeness:
$\sum_{i,j} K_{ij}^\dagger K_{ij} = \frac{1}{N}\sum_{i,j} |j\rangle\langle i|i\rangle\langle j|$
$= \frac{1}{N}\sum_j N|j\rangle\langle j| = \mathbb{I}$ (check!)
'''

ax5.text(0.05, 0.48, kraus7_text, 
         fontsize=9, verticalalignment='center', transform=ax5.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lavender', alpha=0.9, edgecolor='black'))

# Panel 6: Bloch sphere showing complete dephasing
ax6 = fig2.add_subplot(2, 3, 6, projection='3d')
ax6.set_title('(d) Complete Dephasing on Bloch Sphere', fontweight='bold')
ax6.set_xlabel('$b_x$')
ax6.set_ylabel('$b_y$')
ax6.set_zlabel('$b_z$')

# Draw Bloch sphere
ax6.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.15, color='cyan')

# Show several initial states collapsing to center
n_states = 15
for i in range(n_states):
    theta = 2 * np.pi * i / n_states
    phi = np.pi / 3
    init = [0.4 * np.sin(phi) * np.cos(theta), 
            0.4 * np.sin(phi) * np.sin(theta),
            0.4 * np.cos(phi)]
    
    ax6.scatter(*init, s=80, c='blue', marker='o', alpha=0.6)
    # Arrow to center
    ax6.plot([init[0], 0], [init[1], 0], [init[2], 0], 'k--', linewidth=1, alpha=0.3)

# Center (maximally mixed)
ax6.scatter(0, 0, 0, s=400, c='gray', marker='o', edgecolors='black', linewidths=3, alpha=0.9)
ax6.text(0.1, 0.1, 0.1, '𝕀/N', fontsize=12, weight='bold')

ax6.view_init(elev=20, azim=45)

plt.tight_layout()
plt.savefig('../figures/quantum_channels.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/quantum_channels.png")

# ============================================================================
# SUMMARY FIGURE: QUANTUM CHANNEL HIERARCHY
# ============================================================================

print("\n[3/3] Creating summary figure for quantum channels...")

fig3 = plt.figure(figsize=(14, 10))
fig3.suptitle('Summary: Quantum Channels and Operations', 
              fontsize=16, fontweight='bold', y=0.98)

# Panel 1: Channel types
ax1 = fig3.add_subplot(2, 2, 1)
ax1.set_title('Types of Quantum Channels', fontweight='bold')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')

# Hierarchy of channels
channels = [
    (5, 9, 'All CPTP Maps', 'lightblue', 3.5),
    (5, 7, 'Unitary Channels', 'lightgreen', 2.5),
    (5, 5, 'Measurements', 'lightyellow', 2.5),
    (5, 3, 'Decoherence', 'lightcoral', 2.5),
    (5, 1, 'Complete Dephasing', 'gray', 2.5)
]

for x, y, label, color, width in channels:
    box = FancyBboxPatch((x - width/2, y - 0.3), width, 0.6, 
                         boxstyle="round,pad=0.1",
                         facecolor=color, edgecolor='black', linewidth=2)
    ax1.add_patch(box)
    ax1.text(x, y, label, ha='center', va='center', fontsize=11, weight='bold')

# Panel 2: Entropy changes
ax2 = fig3.add_subplot(2, 2, 2)
ax2.set_title('Entropy Under Different Channels', fontweight='bold')
ax2.set_xlabel('Input Entropy S(ρ)')
ax2.set_ylabel('Output Entropy S(𝓔(ρ))')
ax2.grid(True, alpha=0.3)

S_in = np.linspace(0, np.log(4), 100)

# Unitary (preserves entropy)
ax2.plot(S_in, S_in, linewidth=3, label='Unitary', color='green')

# Dephasing (increases entropy)
S_dephasing = S_in + 0.3 * (np.log(4) - S_in)
ax2.plot(S_in, S_dephasing, linewidth=3, label='Partial dephasing', color='orange')

# Complete dephasing
ax2.plot(S_in, np.log(4) * np.ones_like(S_in), linewidth=3, 
        label='Complete dephasing', color='red')

# Measurement (can decrease)
S_measurement = 0.7 * S_in
ax2.plot(S_in, S_measurement, linewidth=3, linestyle='--',
        label='Measurement (von Neumann)', color='blue')

ax2.plot([0, np.log(4)], [0, np.log(4)], 'k--', alpha=0.5, linewidth=1)
ax2.legend()

# Panel 3: Kraus rank
ax3 = fig3.add_subplot(2, 2, 3)
ax3.set_title('Number of Kraus Operators', fontweight='bold')
ax3.set_xlabel('Hilbert Space Dimension N')
ax3.set_ylabel('Number of Kraus Operators')
ax3.grid(True, alpha=0.3)
ax3.set_yscale('log')

N_vals = np.arange(2, 11)

# Unitary: 1 Kraus operator
ax3.plot(N_vals, np.ones_like(N_vals), 'o-', linewidth=2.5, markersize=10,
        label='Unitary', color='green')

# Collapse to single state: N operators
ax3.plot(N_vals, N_vals, 's-', linewidth=2.5, markersize=10,
        label='Collapse (Problem 6)', color='blue')

# Complete dephasing: N² operators
ax3.plot(N_vals, N_vals**2, '^-', linewidth=2.5, markersize=10,
        label='Dephasing (Problem 7)', color='red')

ax3.legend()

# Panel 4: Summary table
ax4 = fig3.add_subplot(2, 2, 4)
ax4.axis('off')
ax4.text(0.5, 0.95, 'Summary of Key Results', 
         ha='center', fontsize=13, fontweight='bold', transform=ax4.transAxes)

summary_text = '''
QUANTUM CHANNEL STRUCTURE:

General form:
    𝓔(ρ) = Σᵢ Kᵢ ρ Kᵢ†
    
Completeness: Σᵢ Kᵢ†Kᵢ = 𝕀

PROBLEM 6: Collapse Channel
    Goal: 𝓔(ρ) = |ψ⟩⟨ψ|
    Kraus operators: Kᵢ = |ψ⟩⟨i|
    Number: N operators
    Physical: Measurement + state preparation

PROBLEM 7: Complete Dephasing
    Goal: 𝓔(ρ) = 𝕀/N
    Kraus operators: Kᵢⱼ = (1/√N)|i⟩⟨j|
    Number: N² operators
    Physical: Maximum noise/decoherence

KEY PROPERTIES:
• Unitary channels preserve entropy
• Dephasing increases entropy
• Complete dephasing → S_max = ln N
• Measurements can decrease entropy
• All channels: S(𝓔(ρ)||σ) ≤ S(ρ||σ)
  if 𝓔(σ) = σ (data processing inequality)
'''

ax4.text(0.05, 0.48, summary_text, 
         fontsize=9, verticalalignment='center', transform=ax4.transAxes,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightcyan', alpha=0.9, edgecolor='black'),
         family='monospace')

plt.tight_layout()
plt.savefig('../figures/summary_channels.png', dpi=200, bbox_inches='tight')
print("  [OK] Saved: ../figures/summary_channels.png")

print("\n" + "="*80)
print("All supplementary visualizations complete!")
print("="*80)
print("\nGenerated files:")
print("  • problem3_4_thermodynamics.png")
print("  • problem3_6_7_quantum_channels.png")
print("  • problem3_summary_channels.png")

plt.show()

