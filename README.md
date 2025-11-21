# Physics Problem Sets Repository

A comprehensive collection of solutions and visualizations for advanced physics problem sets, with emphasis on General Relativity and Quantum Information Theory.

---

## Repository Structure

```
physics/
├── README.md
└── courses/
    └── witten_gr_qit/              # E. Witten's GR & QIT Course (Physics 539)
        ├── problem_set_1/
        │   ├── solutions.md        # Complete solutions with embedded figures
        │   ├── extended_notes_problem2.md
        │   ├── extended_notes_problem3.md
        │   ├── figures/
        │   │   ├── curves.png
        │   │   └── insight.png
        │   └── scripts/
        │       └── visualizations.py
        ├── problem_set_2/
        │   ├── solutions.md
        │   ├── figures/
        │   │   ├── null_hypersurfaces.png
        │   │   ├── trapped_surfaces.png
        │   │   └── causal_futures.png
        │   └── scripts/
        │       └── visualizations.py
        └── problem_set_3/
            ├── solutions.md
            ├── figures/
            │   ├── entropy.png
            │   ├── bloch_sphere.png
            │   ├── entropy_inequalities.png
            │   ├── thermodynamics.png
            │   ├── quantum_channels.png
            │   └── summary_channels.png
            └── scripts/
                ├── visualizations_part1.py
                └── visualizations_part2.py
```

---

## Course: Witten's General Relativity & Quantum Information Theory

**Source:** Physics 539, Fall 2022  
**Instructor:** Edward Witten  
**Institution:** Institute for Advanced Study

### Problem Set 1: Causal Structure and Raychaudhuri's Equation

**Topics:**
- Convergence of curves in Minkowski space
- Compactness of causal curves in globally hyperbolic spacetimes
- Ricci tensor calculations for Raychaudhuri's equation

**Key Concepts:** Euclidean arclength parametrization, global hyperbolicity, Cauchy surfaces, null geodesic congruences

**Visualizations:** 2 figures illustrating curve convergence and arclength accumulation

### Problem Set 2: Null Hypersurfaces and Trapped Surfaces

**Topics:**
- Computing R_uu along null hypersurfaces
- Trapped surfaces in conformally flat spacetimes
- Boundaries of causal futures and black hole horizons

**Key Concepts:** Raychaudhuri equation (null case), conformal geometry, trapped surfaces, event horizons

**Visualizations:** 3 comprehensive multi-panel figures

### Problem Set 3: Quantum Information Theory

**Topics:**
1. Maximum von Neumann entropy
2. Density matrices and Bloch sphere representation
3. Strong subadditivity of entropy
4. First law of thermodynamics from quantum mechanics
5. Relative entropy and monotonicity
6. Kraus operators for collapse channels
7. Kraus operators for complete dephasing

**Key Concepts:** von Neumann entropy, density matrices, Bloch sphere, strong subadditivity, quantum channels, Kraus representation

**Visualizations:** 6 detailed figures covering entropy, quantum states, and quantum channels

---

## How to Use This Repository

### Reading Solutions

Navigate to the appropriate problem set directory and open `solutions.md`. Each solution document includes:

- Complete problem statements as originally assigned
- Step-by-step derivations with detailed explanations
- Embedded figures providing visual intuition
- Physical interpretations and connections to broader theory

### Generating Visualizations

Each problem set includes Python scripts to regenerate all figures:

```bash
# Problem Set 1
cd courses/witten_gr_qit/problem_set_1/scripts
python visualizations.py

# Problem Set 2
cd courses/witten_gr_qit/problem_set_2/scripts
python visualizations.py

# Problem Set 3
cd courses/witten_gr_qit/problem_set_3/scripts
python visualizations_part1.py
python visualizations_part2.py
```

**Dependencies:** numpy, matplotlib, scipy

**Installation:**
```bash
pip install numpy matplotlib scipy
```

### Extended Notes

Problem Set 1 includes additional detailed derivations:
- `extended_notes_problem2.md`: Comprehensive discussion of compactness and causal structure
- `extended_notes_problem3.md`: Complete step-by-step R_tt calculation with all Christoffel symbols

---

## Key Results and Formulas

### General Relativity

**Raychaudhuri Equation (Null):**
$$\frac{d\theta}{du} = -\theta^2 - \sigma_{ab}\sigma^{ab} + \omega_{ab}\omega^{ab} - R_{ab}k^ak^b$$

**Trapped Surface Condition (Conformally Flat):**
For metric $ds^2 = (t^2-1)(-dt^2 + d\vec{x}^2)$, surface at $t=t_0$, $|\vec{x}|=R$ is trapped when:
$$|t_0| > 1 \quad \text{and} \quad R > |t_0| - \frac{1}{|t_0|}$$

**R_tt Formula:**
$$R_{tt} = -\frac{1}{2}\partial_t\text{Tr}(g^{-1}\dot{g}) - \frac{1}{4}\text{Tr}(g^{-1}\dot{g})^2$$

### Quantum Information Theory

**Maximum Entropy:**
$$S(\rho) \leq \log N, \quad \text{equality iff } \rho = \frac{1}{N}\mathbb{I}$$

**Bloch Sphere (Qubits):**
$$\rho = \frac{1}{2}(\mathbb{I} + \vec{b} \cdot \vec{\sigma}), \quad |\vec{b}| \leq \frac{1}{2}$$

**Strong Subadditivity:**
$$S_{AB} + S_{BC} \geq S_B + S_{ABC}$$

**First Law (Quantum):**
$$\delta E = T \delta S$$

**Quantum Channel:**
$$\mathcal{E}(\rho) = \sum_k K_k \rho K_k^\dagger, \quad \sum_k K_k^\dagger K_k = \mathbb{I}$$

---

##  Expanding the Repository

### Adding New Problem Sets

To add a new problem set to the Witten course:

```bash
cd courses/witten_gr_qit
mkdir problem_set_N
mkdir problem_set_N/scripts
mkdir problem_set_N/figures
```

Create `solutions.md` following the existing format:
1. Problem statement (as originally assigned)
2. Detailed solution with step-by-step derivations
3. Embedded figures with descriptive captions
4. Physical interpretation and connections

### Adding New Courses

To add a new course or problem set collection:

```bash
cd courses
mkdir course_name
mkdir course_name/problem_set_1
# ... follow structure above
```

Update this README with:
- Course description
- Key topics covered
- Notable results

### Creating Visualizations

Follow the existing pattern:
- Save figures to `../figures/` relative to script location
- Use clear, descriptive filenames
- Include comprehensive multi-panel figures when appropriate
- Add figure captions in the solutions document
- Use LaTeX math rendering in figure text boxes

---

## Mathematical Notation

- **Manifolds:** $M$ (spacetime), $S$ (spacelike hypersurface)
- **Metrics:** $g_{\mu\nu}$ (spacetime), $g_{ij}$ (spatial)
- **Causal structure:** $J^+(p)$ (causal future), $I^+(p)$ (chronological future)
- **Quantum states:** $|\psi\rangle$ (pure state), $\rho$ (density matrix)
- **Operators:** $H$ (Hamiltonian), $\sigma_i$ (Pauli matrices)
- **Information:** $S(\rho)$ (von Neumann entropy), $S(\rho\|\sigma)$ (relative entropy)

---

## References

### General Relativity
- **Wald**, *General Relativity* - Rigorous mathematical treatment
- **Hawking & Ellis**, *The Large Scale Structure of Space-Time* - Classic reference
- **Poisson**, *A Relativist's Toolkit* - Computational methods

### Quantum Information  
- **Nielsen & Chuang**, *Quantum Computation and Quantum Information* - Comprehensive textbook
- **Preskill**, Quantum Information Lecture Notes - Detailed and pedagogical
- **Wilde**, *Quantum Information Theory* - Advanced treatment

---

## Pedagogical Features

### Visual-Spatial Intuition

Every solution includes carefully designed visualizations:
- **Multi-panel figures** showing different aspects of the same concept
- **Phase space diagrams** illustrating dynamical behavior
- **3D visualizations** for geometric intuition
- **Parameter space plots** showing regimes and boundaries

### Step-by-Step Derivations

All calculations include:
- Clear statement of what is being computed and why
- Intermediate steps (never skipping "obvious" steps)
- Physical interpretation at each stage
- Verification of results when possible

### Connections and Context

Solutions emphasize:
- How problems relate to each other
- Connections to broader theoretical frameworks
- Applications to physical systems
- Historical context and significance

---

## Contributing

This repository is designed to be extended with:
- Additional problem sets from Physics 539
- Problem sets from other advanced physics courses
- Original problems exploring related topics
- Enhanced visualizations
- Extended notes on particularly subtle points

When adding content:
1. Follow the established directory structure
2. Include complete problem statements
3. Provide detailed, pedagogical solutions
4. Create informative visualizations
5. Update this README

---

## License

These solutions are for educational purposes. Problem statements are from Physics 539 (Fall 2022) taught by Edward Witten at the Institute for Advanced Study.

---

## Acknowledgments

- **Edward Witten** for the original course and problem sets
- The Physics 539 course for providing excellent problems spanning GR and QIT

---

**Last Updated:** November 2024

**Maintainer:** Physics 539 Student

*This repository demonstrates the deep connections between General Relativity and Quantum Information Theory, two of the most fundamental frameworks in modern theoretical physics.*
