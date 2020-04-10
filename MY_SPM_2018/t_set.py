from sympy import Symbol, pprint
from sympy.abc import i, j, k
from sympy import Range

n = Symbol('n', integer=True)
r = Range(n, n + 20, 3)
r.inf
pprint(r)
