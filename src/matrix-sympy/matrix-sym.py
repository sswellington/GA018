#!/usr/bin/env python

from sympy import Symbol
from sympy.interactive.printing import init_printing
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt


''' Source
    https://docs.sympy.org/latest/modules/matrices/matrices.html
'''
x = Symbol('x')

identity_matrix = eye(3)
M =  identity_matrix * x

print(M)

print(M.subs(x, 4))
print(M.subs(x, 4).det())

M = Matrix(( [1, 2, 3], [3, 6, 2], [2, 0, 1] ))
print(M.transpose())
print(M.inv())
