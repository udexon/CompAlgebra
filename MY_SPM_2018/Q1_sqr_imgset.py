from sympy import Symbol, S, pi, Dummy, Lambda
from sympy.sets.sets import FiniteSet, Interval
from sympy.sets.fancysets import ImageSet
x = Symbol('x')
N = S.Naturals
squares = ImageSet(Lambda(x, x**2), N) # {x**2 for x in N}
print 4 in squares
print squares
print FiniteSet(0, 1, 2, 3, 4, 5, 6, 7, 9, 10).intersect(squares)
print FiniteSet(9, 16, 25).intersect(squares)
