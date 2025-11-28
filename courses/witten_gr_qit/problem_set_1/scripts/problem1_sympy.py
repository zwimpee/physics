import sympy as sp

# Define symbolic variables
t = sp.Symbol('t', real=True, positive=True)
n = sp.Symbol('n', positive=True, integer=True)

# Define the curve γₙ: x = sin(πnt)
x = sp.sin(sp.pi * n * t)

# --- NEW: Compute dx/dt ---
dx_dt = sp.diff(x, t)
print("dx/dt =", dx_dt)

# --- Minkowski interval ds² = -dt² + dx² ---
# Factor out dt² to get ds²/dt²
ds2_over_dt2 = -1 + dx_dt**2
ds2_over_dt2_simplified = sp.simplify(ds2_over_dt2)
print("\nds²/dt² =", ds2_over_dt2_simplified)

# --- Euclidean arclength element ds_E = √(1 + (dx/dt)²) dt ---
ds_E_over_dt = sp.sqrt(1 + dx_dt**2)
ds_E_over_dt_simplified = sp.simplify(ds_E_over_dt)
print("\nds_E/dt =", ds_E_over_dt_simplified)