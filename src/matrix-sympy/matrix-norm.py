#!/usr/bin/env python

from sympy import Matrix, pprint


a = Matrix([[-3, 5, 7],
            [ 2, 6, 4],
            [ 0, 2, 8]])

b = Matrix([[ 2,-2, 1],
            [-1, 3,-1],
            [ 2,-4, 1]])

pprint(b.norm())    # Frobenius norm
