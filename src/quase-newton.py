from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.plotting import plot, plot3d
from sympy.abc import x,y,w,z

from Error import * 
from Log import *


MAX = 20
PATH = 'log/quase-newton/'
TOLERANCE = 0.00000001 # 10**(-8)

# L = 1       # lenght
# P = 15      # weight
PL = 15     # weight * lenght
K = 100     # proportionality
M = Matrix([[K * (x    ) - ((7 * PL) / 2 ) * cos(x) - K * (y - x)],
            [K * (y - x) - ((5 * PL) / 2 ) * cos(y) - K * (w - y)],
            [K * (w - y) - ((3 * PL) / 2 ) * cos(w) - K * (z - w)],
            [K * (z - w) - ((    PL) / 2 ) * cos(z)]]) 


def __repr__(matrix, weight_lenght, proportionality):
    print('K =', proportionality) 
    # print('P =', weight) 
    # print('L =', proportionality) 
    print('PL =', weight_lenght) 
    print(' M', matrix.shape)
    pprint(matrix) 
    

def quase_newton(fn, cx, tol, nmax) :
    l = Log()
    e = Error()
    previous = 0
    
    return False


if __name__ == "__main__" :
    __repr__(M,PL,K)
