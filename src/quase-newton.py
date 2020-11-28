from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.plotting import plot, plot3d
from sympy.abc import N,m

from Error import * 
from Log import *


MAX = 20
PATH = 'log/quase-newton/'
TOLERANCE = 0.00000001 # 10**(-8)


angle = [0.0, 0.0, 0.0, 0.0]    # OMEGA
proportionality = 100* N * m    # K = 100Nm
length = m                      # L = 1m
weight = 0.0                    # P = 15N / rad -> pesquisar com faz o radiano


# proportionality * (angle[0]) 
# proportionality * (angle[1] - angle[0]) 
# proportionality * (angle[2] - angle[1]) 
# proportionality * (angle[3] - angle[2])


def __repr__():
    print('omega =', angle) 
    print('K =', proportionality) 
    print('L =', length) 
    print('P =', weight) 


if __name__ == "__main__" :
    __repr__()