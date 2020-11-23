from sympy import Function, hessian, pprint
from sympy.abc import x, y


f = Function('f')(x, y)
g1 = Function('g')(x, y)
g2 = x**2 + 3*y


''' Hessian matrix 
    Compute Hessian matrix 
    for a function f wrt parameters in varlist 
    which may be given as a sequence or a row/column vector. 
    A list of constraints may optionally be given.
    
    References:  https://en.wikipedia.org/wiki/Hessian_matrix
'''

print(hessian(f, (x, y), [g1, g2]))