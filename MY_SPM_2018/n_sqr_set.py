from sympy import Symbol, pprint
from sympy.abc import i, j, k
from sympy import Range

n = Symbol('n', integer=True)
r = Range(n, n * n, 3)
r.inf
pprint(r)
