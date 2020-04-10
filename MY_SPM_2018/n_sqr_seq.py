from sympy import SeqFormula, oo, Symbol
n = Symbol('n')
print SeqFormula(n**2, (-oo, 0))[0:6]
