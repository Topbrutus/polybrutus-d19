# Polybrutus D19 — Exact Euclidean distance and graph spectral proof

## 1. Conservative labelled Euclidean metric

From frozen Polybrutus D18, take the 23 radius-one vectors with 253 exact labelled squared distances. Append a zero coordinate to each, then add a new perpendicular unit point. Every old squared distance remains identical and every new pair has squared distance `1+1=2`. Thus `C(24,2)=276=253+23` labelled unordered pairs. The exact `k=4d²/R²` histogram is `{4:6,7:2,8:245,9:3,10:10,12:6,13:2,16:2}`; their squared-distance sum is `2255R²/4`.

## 2. Exact minimal affine rank and positive-semidefinite Gram

Let `X` be the exact 24-by-20 stored coordinate matrix, `D` the exact 24-by-24 **squared Euclidean distance matrix**, and `H=I-11ᵀ/24` the centering projection. The symbolic verifier proves without floating point:

```
rank([q2-q1,...,q24-q1])=19
rank(B)=19
B=-(1/2)HDH=(HX)(HX)^T.
```

The last identity proves `B` positive semidefinite. A complete *labelled* squared Euclidean distance matrix determines its centered Gram uniquely, so every Euclidean realization with the same 276 labelled distances has affine rank exactly **19**. Although the coordinate representation uses 20 storage slots, the centered simplex block contributes one exact redundancy.

## 3. Exact chosen graph spectrum

Let `L18` denote the predecessor 23-vertex Laplacian under the chosen model of equal unit scalar masses and couplings `w_ij=1/d_ij²` at `R=1`. Uniform attachment of the 24th vertex gives

```
L19=[ L18+(1/2)I23     -(1/2)1 ]
    [ -(1/2)1ᵀ              23/2 ].
```

The previous zero mode is replaced by a global uniform zero mode and an intergroup mode at eigenvalue `24/2=12`, while every old zero-sum eigenmode shifts upward by 1/2. For exact monic characteristic polynomials,

```
chi24(z)=z(z-12)chi23(z-1/2)/(z-1/2).
```

The frozen D18 predecessor had `chi23(z)=z(z-23/2)^12(z-11)^4 f6(z-8)`, with `f6(z)=chiP7(z)/z` derived from the canonical seven-point graph. Substituting yields

```
chi24(z)=z(z-12)^13(z-23/2)^4 f6(z-17/2).
```

The primary program calculates the full **24-by-24 exact characteristic polynomial** and verifies both recurrence and closed form. The exact checks `f6(7/2)!=0` and `f6(3)!=0` prove no extra factors coincide with eigenvalue 12 or 23/2; their exact multiplicities are **13** and **4** respectively.

The separately implemented rational verifier reconstructs all 276 squared distances, Gram rank 19 and the complete weighted graph, verifying the same eigenvalue multiplicities independently via characteristic-polynomial derivatives.

## 4. Adversarial controls, reproducibility and scientific limits

Four invalid configurations are detected: a corrupted squared-distance entry, repeated vertex lowering affine rank, tilted nonorthogonal new point, and a label swap preserving unlabelled histogram but breaking labelled metric.

This is a reproducible **particular synthetic Euclidean metric** and an explicitly chosen mathematical graph model. Orthogonal extensions and uniform weighted joins are established methods. There is no experimental frequency in hertz, physical nineteen-dimensional spacetime claim, particle discovery or novel universal theorem. Independent human peer review is outstanding.
