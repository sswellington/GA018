# from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
# from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
# from sympy.abc import x,y,w,z

from Linear_system import *
from Error import * 
from Log import *


MAX = 20
PATH = 'log/newton-sys/'
TOLERANCE = 0.00000001 # 10**(-8)

PL = 15     # weight * lenght
K = 100     # proportionality
M = Matrix([[K * (x    ) - ((7 * PL) / 2 ) * cos(x) - K * (y - x)],
            [K * (y - x) - ((5 * PL) / 2 ) * cos(y) - K * (w - y)],
            [K * (w - y) - ((3 * PL) / 2 ) * cos(w) - K * (z - w)],
            [K * (z - w) - ((    PL) / 2 ) * cos(z)]]) 
    

def newton(fn, point, tol, nmax) :
    l = Log()
    e = Error()
    ls = Linear_system()
    j = ls.jacobiana_inverse(fn,[x,y,w,z])
    f = lambdify([x,y,w,z], fn)
    previous = point
    
    for n in range(nmax) : 
        ff = f(float(point[0]),float(point[1]),float(point[2]),float(point[3]))
        jj = j(float(point[0]),float(point[1]),float(point[2]),float(point[3]))
        point = point - (Matrix(jj) * Matrix(ff)) 
        e.matrix_norm(point, previous)
        
        # l.append([float(point[0]), float(point[1]), float(point[2]), float(point[3]), 
        #           float(previous[0]),float(previous[1]),float(previous[2]),float(previous[3]), 
        #           float(e._norm)])

        if (e._norm < tol) :
            # l.set_header(['X axes'  ,'Y axes',  'W axes'  ,'Z axes',
            #               'X-1 axes','Y-1 axes','W-1 axes','Z-1 axes',  
            #               'Matrix Norm'])
            # l.list2file((PATH+'main-inversa'))
            # l.time(PATH+'time-n-sys-inversa')
            return point
            breakpoint
        previous = point
    return False
    

if __name__ == "__main__" :
    seed = Matrix([[1],[2],[3],[4]])
    for i in range(1):
        r = newton(M, seed, TOLERANCE, MAX)
    pprint(r)