#!/usr/bin/env python3
"""Independent Polybrutus D19 rational metric and theoretical graph spectrum.

No imports of any geometric generator. Reconstructs all 276 labelled
squared distances from elementary rational geometry, independently.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/"results"/"certificate_d19.json").read_text(encoding="utf8"))
parent=json.loads((ROOT/"prior"/"certificate_d18.json").read_text(encoding="utf8"))
core=[
 (F(0),F(0),F(1)),(F(1,2),F(0),F(1,2)),
 (F(-1,4),F(3,4),F(1,2)),(F(-1,4),F(-3,4),F(1,2)),
 (F(0),F(0),F(-1)),(F(1,2),F(0),F(-1,2)),
 (F(-1,2),F(0),F(-1,2))
]
def squared_distance(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(core[i][k]-core[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

pairs=list(combinations(range(24),2))
exact={(i+1,j+1):squared_distance(i,j) for i,j in pairs}
cert={(int(e["i"]),int(e["j"])):F(e["d2"])
      for e in report["labelled_squared_distances"]}
assert len(exact)==276 and exact==cert
former={(int(e["i"]),int(e["j"])):F(e["d2"])
        for e in parent["labelled_squared_distances"]}
assert len(former)==253 and all(exact[k]==v for k,v in former.items())
assert all(squared_distance(i,23)==F(2) for i in range(23))
hist=Counter(4*squared_distance(i,j) for i,j in pairs)
assert hist==Counter({F(4):6,F(7):2,F(8):245,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(exact.values(),F(0))==F(2255,4)
D=s.Matrix(24,24,lambda i,j:s.Rational(squared_distance(i,j).numerator,squared_distance(i,j).denominator))
H=s.eye(24)-s.ones(24)/24
B=-H*D*H/2
assert B.rank()==19
oldD=D[:23,:23];Hold=s.eye(23)-s.ones(23)/23
assert (-Hold*oldD*Hold/2).rank()==18

L=s.zeros(24)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w
    L[i,j]-=w;L[j,i]-=w
z=s.Symbol("z");chi=L.charpoly(z).as_expr()
for value,multiplicity in [(s.Integer(12),13),(s.Rational(23,2),4)]:
    assert all(s.simplify(s.diff(chi,z,k).subs(z,value))==0 for k in range(multiplicity))
    assert s.simplify(s.diff(chi,z,multiplicity).subs(z,value))!=0
assert report["affine_rank"]==report["centered_gram_rank"]==19
assert report["parent_distances_preserved"]==253 and report["new_distances"]==23
p=ROOT/"results"/"certificate_d19.json"
print("INDEPENDENT D19 PASS: 276 exact rational labelled distances, 253 parent preserved, Gram rank 19")
print("INDEPENDENT IDEAL GRAPH PASS: eigenvalue 12 x13, eigenvalue 23/2 x4")
print("CERTIFICATE_SHA256="+hashlib.sha256(p.read_bytes()).hexdigest())
