# Polybrutus D19 — Exact twenty-four-point Euclidean configuration

**Immutable parent:** `Topbrutus/polybrutus-d18@v0.1.0`, source commit `b42aae51d92b817008c823a34162e1eb94c13cae`, Zenodo parent DOI `10.5281/zenodo.24409207`.

Let `p1,...,p23` be the exact frozen 18D radius-one points in nineteen coordinate-storage slots. The centered five-point regular-simplex block imposes one exact linear coordinate relation. Embed `q_i=(p_i,0)` in twenty storage slots for every `i=1,...,23`, and add `q24=e20=(0,...,0,1)`, orthogonal to all preceding points.

Every parent labelled squared distance is unchanged, and for each old point

```
||q24-q_i||²=||q24||²+||q_i||²-2<q24,q_i>=2.
```

At general radius `R>0`, squared distances scale by `R²`, so all 23 new values are `2R²`. There are `C(24,2)=276` unordered labelled pairs: **253 conserved** plus 23 new.

The normalized histogram for `k=4d²/R²` is `{4:6,7:2,8:245,9:3,10:10,12:6,13:2,16:2}`; `sum(d²)=2255R²/4`. At normalized radius the 20-slot centroid is `(0,0,1/48,0,0,0,0,0,1/24,1/24,1/24,1/24,1/24,1/24,1/24,1/24,1/24,1/24,1/24,1/24)`.

The intrinsic affine rank is **19**, although 20 coordinate slots are used; one simplex coordinate relation remains.

## Chosen theoretical weighted graph

Define a mathematical equal-unit-mass scalar oscillator on each point with all-pairs weights `w_ij=R²/d_ij²`. The 24th vertex couples uniformly to each preceding vertex with weight 1/2:

```
L19 = [ L18 + (1/2)I23        -(1/2)1 ]
      [ -(1/2)1ᵀ                   23/2 ].
```

With `f6(z)=chiP7(z)/z` the six-nonzero-mode factor of the original seven-point model graph,

```
chi24(z)=z(z-12)*chi23(z-1/2)/(z-1/2)
        =z(z-12)^13(z-23/2)^4*f6(z-17/2).
```

Eigenvalue **12** has exact multiplicity **13** and eigenvalue **23/2** has exact multiplicity **4**. Both refer only to the chosen ideal graph model.
