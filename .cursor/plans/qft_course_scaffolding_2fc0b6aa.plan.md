---
name: QFT Course Scaffolding
overview: Create a comprehensive, ADHD-friendly scaffolding structure for working through MIT 8.323 QFT I, integrating the OCW materials with your existing Witten course approach and supplementary resources like David Tong's notes.
todos:
  - id: create-structure
    content: Create qft_i/ directory structure with subdirectories
    status: completed
  - id: main-readme
    content: Write main README.md with course overview and connections
    status: completed
    dependencies:
      - create-structure
  - id: progress-tracker
    content: Create PROGRESS.md visual checklist tracker
    status: completed
    dependencies:
      - create-structure
  - id: resource-links
    content: Write resources/links.md with Tong, Coleman, errata URLs
    status: completed
    dependencies:
      - create-structure
  - id: prerequisites
    content: Write resources/prerequisites.md with self-assessment checklist
    status: completed
    dependencies:
      - create-structure
  - id: week0-warmup
    content: Write week_00_warmup/ QM and classical mechanics review
    status: completed
    dependencies:
      - create-structure
  - id: week1-scaffold
    content: Write week_01_ps01/ README, readings, and socratic_guide
    status: completed
    dependencies:
      - create-structure
---

# QFT I Course Scaffolding Plan

## Context Summary

**What you have:**
- MIT 8.323 QFT I (Spring 2023) downloaded at [`courses/8.323-spring-2023/`](courses/8.323-spring-2023/)
- 26 lecture videos, 12 problem sets + solutions, 10 recitation notes
- Existing approach from Witten's GR/QIT course (Socratic guides, solutions.md, computational verification)

**Key discoveries from browser research:**
- **David Tong's QFT Notes** (Cambridge): Free, highly pedagogical notes that parallel P&S chapters — perfect supplementary reading
- **Sidney Coleman's Harvard Lectures**: Legendary video lectures from the 1970s, available free
- **Prerequisites**: 8.321 Quantum Theory I (assumes solid QM: density matrices, perturbation theory, spin)

**ADHD Scaffolding Philosophy:**
- Explicit "what to do next" at every point
- Small, completable chunks with clear boundaries
- Self-testing format (externalized executive function)
- Visual organization and multiple entry points

---

## Directory Structure

```
courses/
├── 8.323-spring-2023/           # Raw OCW download (untouched)
└── qft_i/                        # Your working directory
    ├── README.md                 # Course overview, connections, how to use
    ├── PROGRESS.md               # Checklist tracker (ADHD-friendly)
    ├── resources/
    │   ├── links.md              # URLs to Tong notes, Coleman videos, etc.
    │   └── prerequisites.md      # "What you should already know" review
    ├── week_00_warmup/           # Pre-course prep (bridge the gap)
    │   ├── qm_review.md          # Key QM concepts refresher
    │   └── classical_mechanics_review.md  # Lagrangians, Hamiltonians
    ├── week_01_ps01/
    │   ├── README.md             # "This week" overview
    │   ├── readings.md           # What to read (P&S 2.1-2.2, Tong Ch.1)
    │   ├── lecture_notes.md      # Your notes from Lectures 1-2
    │   ├── socratic_guide.md     # Self-testing questions
    │   ├── ps01_attempt.md       # Your work (before looking at solutions)
    │   └── ps01_solutions.md     # Cleaned-up solutions after comparison
    ├── week_02_ps02/
    │   └── ... (same structure)
    └── connections/
        └── geometry_of_fields.md # How QFT connects to your GR work
```

---

## Files to Create

### 1. Main README ([`courses/qft_i/README.md`](courses/qft_i/README.md))
- Course overview and why you're taking it
- Connection to Witten course and clinical trajectories work
- Quick reference: where to find videos, PDFs, textbooks
- "How to use this directory" guide

### 2. Progress Tracker ([`courses/qft_i/PROGRESS.md`](courses/qft_i/PROGRESS.md))
- Visual checklist for each week
- States: Not Started / In Progress / Complete / Verified
- Designed for quick glance to see where you are

### 3. Resources and Links ([`courses/qft_i/resources/links.md`](courses/qft_i/resources/links.md))
- David Tong's QFT notes: https://www.damtp.cam.ac.uk/user/tong/qft.html
- Sidney Coleman videos: https://www.physics.harvard.edu/events/videos/Phys253
- Peskin & Schroeder errata: https://s3df.slac.stanford.edu/people/mpeskin/QFT.html
- YouTube playlists for MIT 8.323 lectures

### 4. Prerequisites Review ([`courses/qft_i/resources/prerequisites.md`](courses/qft_i/resources/prerequisites.md))
- Checklist of QM concepts you should know
- Checklist of classical mechanics concepts
- Quick self-tests with answers
- Links to review materials if gaps found

### 5. Week 0 Warmup Materials
- [`week_00_warmup/qm_review.md`](courses/qft_i/week_00_warmup/qm_review.md): Operators, commutators, Heisenberg picture, second quantization preview
- [`week_00_warmup/classical_mechanics_review.md`](courses/qft_i/week_00_warmup/classical_mechanics_review.md): Lagrangians, Euler-Lagrange, Hamiltonians, Noether's theorem

### 6. Week 1 / PS1 Scaffolding
- [`week_01_ps01/README.md`](courses/qft_i/week_01_ps01/README.md): This week's overview, what to watch/read, estimated time
- [`week_01_ps01/readings.md`](courses/qft_i/week_01_ps01/readings.md): Detailed reading guide with page numbers and key equations
- [`week_01_ps01/socratic_guide.md`](courses/qft_i/week_01_ps01/socratic_guide.md): Self-testing format matching your Witten approach

---

## Key Design Principles

**For ADHD:**
1. **Chunk boundaries**: Each file is one session's work
2. **No open loops**: Every file ends with "Next: [specific file]"
3. **Visual progress**: PROGRESS.md shows completion at a glance
4. **Multiple entry points**: Can start from README, PROGRESS, or any week
5. **Flexible pacing**: Structure supports going slower without shame

**For depth (matching your existing approach):**
1. Socratic self-testing before looking at solutions
2. Space for your own derivations and notes
3. Connections to broader themes (geometry, optimization)
4. Computational verification hooks (future: SymPy/JAX notebooks)

---

## Implementation Order

1. Create directory structure
2. Write main README with course overview and connections
3. Write PROGRESS.md tracker
4. Write resources/links.md with all URLs
5. Write resources/prerequisites.md with self-assessment
6. Write week_00_warmup/ review materials
7. Write week_01_ps01/ scaffolding for first problem set

After scaffolding is complete, you'll be ready to begin with Week 0 warmup or dive directly into Week 1 depending on your confidence with prerequisites.