#!/usr/bin/env python

# from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
# from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.abc import x,y,w,z

from Linear_system import *
from Error import * 
from Log import *


MAX = 20
PATH = 'log/newton-opt/'
TOLERANCE = 0.00000001  # 10**(-8)
F = 1 - (exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))) + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )


def optimization(fn, point, tol, nmax) :
    # l = Log() 
    e = Error()
    ls = Linear_system()
    h = ls.hessiana(fn,[x,y])
    j = ls.jacobiana_transpose(fn,[x,y])
    previous = point
    
    for n in range(nmax) : 
        hh = h(float(point[0]), float(point[1]))
        jj = j(float(point[0]), float(point[1]))
        L, U, _ = Matrix(hh).LUdecomposition()
        
        gauss = ls.gauss_jordan(Matrix(L), Matrix(-jj))   
        point = point + ls.gauss_jordan(Matrix(U), Matrix(gauss))  
        e.matrix_norm(point, previous)
        
        # l.append([float(point[0]), float(point[1]), 
        #           float(previous[0]), float(previous[1]), 
        #           float(e._norm)])
        
        if (e._norm < tol) :
            # l.set_header(['X axes', 'Y axes','X-1 axes', 'Y-1 axes',  'Matrix Norm'])
            # l.list2file(PATH+'main-lu')
            # l.time(PATH+'time-n-opt-lu')
            return point
            breakpoint   
        previous = point
    return False


if __name__ == "__main__" :
    seed = Matrix([[0.0],[0.0]])
    for i in range(1):
        r = optimization(F, seed, TOLERANCE, MAX)
    pprint(r)
    