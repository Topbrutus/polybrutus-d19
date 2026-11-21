# POLYBRUTUS 19D — Exact Euclidean 24-point metric and thirteenfold model graph mode

**Human researcher and scientific responsibility:** Gabriel St-Pierre, independent researcher.  
**Research status:** exactly reproducible mathematical case study, **not independently peer reviewed by a human**.  
**AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted the symbolic mathematical verification, separately implemented rational verifier, theoretical graph spectrum, drafting, and publication. AI is not an author.

## Certified results (normalized radius R=1)

- **24 labelled points**, **276 exact pairwise squared distances**, and exact minimum Euclidean affine embedding dimension **19**.
- All **253/253** labelled squared distances from frozen 18D are preserved, point-for-point. One additional perpendicular unit vector adds **23 new squared pair distances**, each exactly **2**.
- Eight normalized squared-distance classes `k=4d²/R²`: `{4:6,7:2,8:245,9:3,10:10,12:6,13:2,16:2}`.
- Sum of squared pairwise distances exactly `2255 R²/4`.
- Exact coordinate-difference rank **19**, centered squared-distance Gram rank **19**, and positive-semidefinite identity `B=(HX)(HX)^T`. 20 coordinate-storage slots contain one constrained original regular-simplex direction.
- **Chosen ideal scalar-oscillator weighted graph:** equal unit scalar masses and weights `w_ij=R²/d_ij²`. The Laplacian has exact eigenvalue **12** of multiplicity **13**, and **23/2** of multiplicity **4**. These are dimensionless model eigenvalues, **not measured physical frequencies**.
- Two separately implemented symbolic/rational programs reproduce all **276/276** labelled squared distances and exact spectral multiplicities; the primary program also rejects **four intentionally incorrect cases**.

## Reproduction

```sh
python -m pip install sympy==1.14.0
python src/verify_d19.py
python tests/independent_d19.py
```

The second verifier derives every squared distance directly from rational geometric rules and **does not import any point generator**. `prior/` preserves source files and certificates copied directly from immutable `Topbrutus/polybrutus-d18@v0.1.0`, source commit `b42aae51d92b817008c823a34162e1eb94c13cae`.

## Research materials

- `src/verify_d19.py`: exact metric, Gram rank, PSD factorization, theoretical graph characteristic polynomial and negative controls.
- `tests/independent_d19.py`: independent rational distance matrix, Gram rank and exact characteristic-polynomial derivative tests.
- `results/certificate_d19.json`: exact squared distances for **all 276 labelled pairs** and complete spectral certificate.
- `SPECIFICATION_D19.md`, `PREUVE_D19.md`, `PROVENANCE.md`: mathematical specification, proof and immutable source lineage.
- `publication/POLYBRUTUS_19D_NOTE.pdf` and `.md`: mathematical preprint, prose CC BY 4.0; source software MIT.
- `SHA256SUMS.txt`: frozen source Git blob hash index.

**Published parent:** [Polybrutus D18, DOI 10.5281/zenodo.24409207](https://doi.org/10.5281/zenodo.24409207).  
**Canonical seven-point geometry:** https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md

**Scientific scope:** Orthogonal Euclidean point extension and uniform weighted-graph spectral shifts are existing mathematical methods. This work certifies a **specific 19D labelled Euclidean metric**, not a newly observed physical dimension, measured resonance, or novel universal theorem.
