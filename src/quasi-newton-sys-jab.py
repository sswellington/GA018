from sympy import lambdify, diff, hessian, jacobi, cos, sin, pprint
from sympy.matrices import Matrix
from sympy.abc import x,y,w,z

from Error import * 
from Log import *


MAX = 200
PATH = 'log/quasi-newton/'
TOLERANCE = 0.00000001 # 10**(-8)

PL = 15     # weight * lenght
K = 100     # proportionality
M = Matrix([[K * (x    ) - ((7 * PL) / 2 ) * cos(x) - K * (y - x)],
            [K * (y - x) - ((5 * PL) / 2 ) * cos(y) - K * (w - y)],
            [K * (w - y) - ((3 * PL) / 2 ) * cos(w) - K * (z - w)],
            [K * (z - w) - ((    PL) / 2 ) * cos(z)]]) 


def __repr__(matrix, weight_lenght, proportionality):
    print('K =', proportionality) 
    print('PL =', weight_lenght) 
    print(' M', matrix.shape)
    pprint(matrix) 


def jacobiana(f, c):
    '''  Jacobian: init and set  '''
    j = (Matrix(f).jacobian(c))
    return (lambdify(c, j))


def gauss_jordan(matrix_a, matrix_b ):
    sol, params = matrix_a.gauss_jordan_solve(matrix_b)
    taus_zeroes = { tau:0 for tau in params }
    return sol.xreplace(taus_zeroes)

    
def quasi_newton(fn, point, tol, nmax) :
    ''' Quasi-Newton Broyden
        Referência    
            Cálculo Numérico - Ruggiero: Pag 2020 do livro 
            https://www.youtube.com/watch?v=wvszn8KlihUs
    '''
    l = Log()
    e = Error()
    j = jacobiana(fn,[x,y,w,z])
    f = lambdify([x,y,w,z], fn)
    previous = point
    
    jj = j(float(point[0]),float(point[1]),float(point[2]),float(point[3]))
    L, U, _ = Matrix(jj).LUdecomposition()
    
    for n in range(nmax) : 
        ff = f(float(point[0]),float(point[1]),float(point[2]),float(point[3]))
        g = gauss_jordan(Matrix(L), Matrix(-ff))
        point = point + gauss_jordan(Matrix(U), Matrix(g))  
        e.matrix_norm(point, previous)
        
        l.append([float(point[0]), float(point[1]), float(point[2]), float(point[3]), 
                  float(previous[0]),float(previous[1]),float(previous[2]),float(previous[3]), 
                  float(e._norm)])
        
        if (e._norm < tol) :
            l.set_header(['X axes'  ,'Y axes',  'W axes'  ,'Z axes',
                'X-1 axes','Y-1 axes','W-1 axes','Z-1 axes',  
                'Matrix Norm'])
            l.list2file((PATH+'main-jab-pr'))
            l.time(PATH+'time-qn-sys_pr')
            return point
            breakpoint
        previous = point
    pprint(point)
    return False


if __name__ == "__main__" :
    seed = Matrix([[1],[1],[1],[1]])
    for i in range(101):
        r =  quasi_newton(M, seed, TOLERANCE, MAX)
    pprint(r)