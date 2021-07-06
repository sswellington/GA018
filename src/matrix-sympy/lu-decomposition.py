#!/usr/bin/env python

from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt

''' LU decomposition
Returns (L, U, perm) where L is a lower triangular matrix with unit diagonal, 
U is an upper triangular matrix, 
and perm is a list of row swap index pairs. 

If A is the original matrix, 
then A = (L*U).permuteBkwd(perm), and 
the row permutation matrix P such that P*A = L*U can be computed by P=eye(A.row).
permuteFwd(perm).
'''

a = Matrix([[4, 3], [6, 3]])
L, U, _ = a.LUdecomposition()

print(L)
print(U)
