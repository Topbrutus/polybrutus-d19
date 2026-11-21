# Polybrutus 19D: Exact Conservative Euclidean Completion and a Thirteenfold Weighted-Graph Mode

**Research author:** Gabriel St-Pierre  
**Affiliation:** Independent researcher  
**Programme:** Polybrutus-X72  
**Date:** 20 November 2026  
**Version:** 0.1.0  
**Status:** Reproducible computational mathematics preprint; no independent human peer review  
**Parent publication:** Polybrutus 18D, DOI 10.5281/zenodo.24409207  
**Scientific source:** https://github.com/Topbrutus/polybrutus-d19/tree/v0.1.0 (after release)

## Abstract

We construct an exact **twenty-four-point labelled Euclidean distance configuration** with minimum affine embedding dimension **nineteen**, conservatively extending the archived Polybrutus 18D metric. All **253 preceding labelled pairwise squared distances** are preserved exactly. A new orthogonal radius-R point contributes **23 new pairwise squared distances of 2R²**, giving **276 labelled pairs** in eight exact normalized squared-distance families. Exact coordinate-difference rank and centered Euclidean-distance Gram rank both equal nineteen; an explicit positive-semidefinite Gram factorization certifies realizability. A separate rational-arithmetic checker reconstructs all 276 labelled squared distances without importing the primary geometry generator.

In a deliberately **chosen ideal complete weighted-graph scalar-oscillator model** with equal scalar masses and weights `w_ij=R²/d_ij²`, the exact 24-by-24 Laplacian has eigenvalue **12 of multiplicity thirteen** and eigenvalue **23/2 of multiplicity four**. Two separate programs verify these values and exact multiplicities. The results concern a specific mathematical metric and stipulated graph model, **not a newly measured physical dimension, experimental resonance or novel universal mathematical theorem**.

## 1. Immutable scientific lineage

Polybrutus begins with seven analytically defined points on a radius-R two-sphere embedded in three-dimensional Euclidean space. A seven-dimensional conservative completion adjoined five vertices of a regular four-dimensional simplex in a subspace perpendicular to the original three-dimensional geometry, preserving the original seven labelled points. That initial 12-vertex 7D metric contains 66 labelled pair distances (DOI **10.5281/zenodo.24407952**).

The dimension-specific sequence subsequently archived exact computational cases with a new perpendicular unit point at each stage: 8D, 13 vertices, 78 pairs (DOI **10.5281/zenodo.24408344**); 9D, 14 vertices, 91 pairs (**10.5281/zenodo.24408448**); 10D, 15 vertices, 105 pairs (**10.5281/zenodo.24408569**); 11D, 16 vertices, 120 pairs (**10.5281/zenodo.24408650**); 12D, 17 vertices, 136 pairs (**10.5281/zenodo.24408720**); 13D, 18 vertices, 153 pairs (**10.5281/zenodo.24408769**); 14D, 19 vertices, 171 pairs (**10.5281/zenodo.24408836**); 15D, 20 vertices, 190 pairs (**10.5281/zenodo.24408887**); 16D, 21 vertices, 210 pairs (**10.5281/zenodo.24408979**); 17D, 22 vertices, 231 pairs (**10.5281/zenodo.24409067**); and 18D, 23 vertices, 253 pairs (**10.5281/zenodo.24409207**).

The present nineteen-dimensional case is derived exclusively from the **immutable scientific Git tag** `Topbrutus/polybrutus-d18@v0.1.0`, source commit **`b42aae51d92b817008c823a34162e1eb94c13cae`**. Source programs and exact certificates copied from this frozen predecessor into `prior/` preserve the complete source lineage. No old geometry, publication, DOI or tag is changed.

## 2. Exact twenty-four-point Euclidean geometry

Normalize the sphere radius to `R=1`. Let `p1,...,p23` be the frozen 18D unit vectors, represented in nineteen coordinate-storage slots. The five-simplex block lies in a centered four-dimensional hyperplane and therefore introduces one exact coordinate relation.

Append a zero coordinate to each old vector:

```
q_i=(p_i,0),         i=1,...,23.
```

Introduce the twenty-fourth vertex as a perpendicular unit basis vector in the new twentieth storage slot:

```
q24=e20=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1).
```

All twenty-four vectors have norm one and the new point is orthogonal to every preceding vector. Every one of the **253 old labelled pairwise squared distances** remains identical. Each of the 23 newly introduced pair distances obeys exactly:

```
||q24-q_i||²=||q24||²+||q_i||²-2<q24,q_i>=2.
```

Scaling the complete configuration by radius `R>0` multiplies each squared distance by `R²`. Thus the newly introduced squared distances are `2R²` and the total number of unordered labelled pairs is:

```
C(24,2)=276=253+23.
```

For normalized squared-distance family parameter `k=4d²/R²`, the complete exact histogram is:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of labelled pairs | 6 | 2 | **245** | 3 | 10 | 6 | 2 | 2 |

The counts sum to **276**. Their total squared length is exactly:

```
sum_{i<j} d_ij²/R²=2255/4.
```

For `R=1`, the centroid in twenty storage slots is:

```
G=(0,0,1/48,0,0,0,0,0,1/24,1/24,1/24,1/24,1/24,1/24,
   1/24,1/24,1/24,1/24,1/24,1/24).
```

The metric has **nineteen independent affine dimensions** despite using twenty storage slots, because the simplex block maintains one linear constraint.

## 3. Exact Gram rank and minimum embedding dimension

Write `X` for the exact 24-by-20 coordinate array, `D` for the symmetric 24-by-24 **squared Euclidean distance matrix**, and `H=I-11ᵀ/24` for the centering projection. Define the centered Euclidean distance Gram matrix:

```
B=-(1/2) H D H.
```

The primary symbolic exact verifier establishes all three identities without numerical approximations:

```
rank([q2-q1,...,q24-q1])=19;
rank(B)=19;
B=(H X)(H X)^T.
```

The last equation gives an explicit **positive-semidefinite factorization**. A complete labelled Euclidean squared-distance matrix determines its centered Gram uniquely; therefore **every Euclidean realization of this same exact 276-entry labelled pair-distance metric** has minimum affine embedding dimension precisely **nineteen**. This is a mathematical rank certificate, not an observation of new spacetime dimensions.

The separately written rational verifier does not import the primary point generator or any predecessor geometry generator. It rebuilds all 276 squared distances from the rational coefficients of the canonical seven points, the five-simplex internal squared distances `5/2`, and the orthogonality of twelve appended unit-axis points. It confirms **276/276** labelled squared distances, **253/253** parent pairs and exact centered Gram rank **19**.

## 4. Thirteenfold eigenvalue in a chosen ideal weighted graph

To illustrate one mathematical model, assign each point a hypothetical scalar displacement and equal unit scalar mass, and join every pair of vertices with selected coupling `w_ij=R²/d_ij²`. This **defines** a weighted complete graph; no physical apparatus or measured dynamical response is assumed.

The new twenty-fourth vertex lies at squared radius-normalized distance 2 from each of the preceding 23, so all new couplings have weight 1/2. Let `L18` be the old 23-by-23 graph Laplacian and `L19` the new 24-by-24 Laplacian. Their exact block relation is:

```
L19=[ L18+(1/2)I23      -(1/2)1 ]
    [ -(1/2)1ᵀ              23/2 ].
```

Writing monic characteristic polynomials `chi23(z)=det(zI-L18)` and `chi24(z)=det(zI-L19)`, the uniform global zero mode, intergroup mode and shifted old zero-sum modes yield the recurrence:

```
chi24(z)=z(z-12)chi23(z-1/2)/(z-1/2).
```

The frozen 18D case has the exact factorization

```
chi23(z)=z(z-23/2)^12(z-11)^4 f6(z-8),
f6(z)=chiP7(z)/z,
```

where `chiP7` is the characteristic polynomial of the original seven-point complete weighted graph and `f6` comprises its six nonzero modes. Substitution yields the following exact new closed form:

```
chi24(z)=z(z-12)^13(z-23/2)^4 f6(z-17/2).
```

The primary checker directly calculates the full exact **24-by-24 characteristic polynomial** and verifies both the recurrence and the closed form. It proves `f6(7/2)!=0` and `f6(3)!=0`, excluding accidental additional factors at eigenvalues 12 and 23/2. Hence the chosen model has eigenvalue **12 with multiplicity exactly thirteen** and eigenvalue **23/2 with multiplicity exactly four**.

The independent rational-metric verifier reconstructs the complete graph and tests the root multiplicities of its full exact characteristic polynomial by vanishing and nonvanishing of successive derivatives. These eigenvalues are **dimensionless properties of the stipulated graph model**, not observed frequencies in hertz.

## 5. Reproducibility, adversarial controls and release integrity

The archive includes `src/verify_d19.py`, `tests/independent_d19.py`, `results/certificate_d19.json` containing **all 276 exact labelled squared distances**, predecessor source and JSON certificates in `prior/`, mathematical specification, proof and provenance, GitHub Actions workflow, and an SHA-256 Git-blob index.

Reproduce the exact verifications:

```sh
python -m pip install sympy==1.14.0
python src/verify_d19.py
python tests/independent_d19.py
```

Both programs must report PASS and reproduce the **same SHA-256** for the generated 276-entry JSON certificate. Four deliberately invalid configurations are rejected: one changed squared-distance entry; a duplicated vertex destroying the new affine dimension; a tilted nonorthogonal new unit vector; and a label swap that keeps an unlabelled distance histogram unchanged but violates the labelled complete metric.

The archival Zenodo release will contain exactly three attachments: immutable Git-tagged source ZIP, the scientific PDF and the exact labelled metric certificate. Their byte lengths and checksums permit validation. The frozen source tag identifies exactly which Git source produced the ZIP.

## 6. Research precedence, limitations and authorship

Euclidean orthogonal extensions, centered squared-distance Gram rank and uniformly joined weighted-graph spectra are **established techniques**. The specific Polybrutus 19D configuration supplies an exact reproducible **case study**, not discovery of those general mathematical methods or a novel universal theorem.

The rank nineteen statement describes the minimum affine Euclidean dimension of **twenty-four mathematical points**. It does **not** establish physical nineteen-dimensional spacetime, measured resonances, particle phenomena or a new physical oscillator. Independent human peer review has not occurred.

**Research author and responsible investigator:** Gabriel St-Pierre, independent researcher. He originated the Polybrutus research programme, established the stepwise publication protocol and directs this investigation.

**Generative AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted exact mathematical proofs, symbolic calculations, separately implemented rational verification code, theoretical graph spectral analysis, provenance auditing, manuscript drafting and GitHub/Zenodo release preparation. The AI is **not listed as an author**.

**Licenses:** scientific preprint and accompanying prose CC BY 4.0; source software MIT.

**References:** original Polybrutus seven-point specification https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md ; parent research DOI https://doi.org/10.5281/zenodo.24409207 ; frozen parent code https://github.com/Topbrutus/polybrutus-d18/tree/v0.1.0 ; complete preceding DOI series in `PROVENANCE.md`.
