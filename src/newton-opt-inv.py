from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.plotting import plot, plot3d
from sympy.abc import x,y

from Error import * 
from Log import *


MAX = 50
PATH = 'log/newton-opt/'
TOLERANCE = 0.00000001 # 10**(-8)
F = 1 - (exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))) + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )


def hessiana_inverse(function, c):
    '''  Hessian: init and set  '''
    h = (hessian(function, c)).inv()
    return (lambdify(c, h))


def jacobian_transpose(function, c):
    '''  Jacobian: init and set  '''
    j = (Matrix([function]).jacobian(c)).transpose()
    return (lambdify(c, j))


def __repr__(xy, previous, hessian, jacobian, L, U):
    ''' signature: __repr__(xy,previous,hh,jj,L,U,gauss_Lj,gauss_ULj) ''' 
    print('   Root_n-1')
    pprint(Matrix(previous))
    print('\n   Root_n')
    pprint(Matrix(xy))
    print('\n   Hessian')
    pprint(Matrix(hessian))
    print('\n   Jacobian')
    pprint(Matrix(jacobian))
    print('\n   L')
    pprint(Matrix(L))
    print('\n   U')
    pprint(Matrix(U))
    print('_____________________________________________________\n')


def optimization(f, xy, tol, nmax) :
    l = Log() 
    e = Error()
    h = hessiana_inverse(f, [x,y])
    j = jacobian_transpose(f, [x,y])
    previous = xy
    
    for n in range(nmax) : 
        hh = (h(float(xy[0]), float(xy[1])))
        jj = (j(float(xy[0]), float(xy[1])))
        xy = xy - (Matrix(hh) * Matrix(jj)) 
        
        e.matrix_norm(xy, previous)
        l.append([float(xy[0]), float(xy[1]), 
                  float(previous[0]), float(previous[1]), 
                  float(e._norm)])
        
        if (e._norm < tol) :
            l.set_header(['X axes', 'Y axes','X-1 axes', 'Y-1 axes',  'Matrix Norm'])
            l.list2file((PATH+'main-inversa'))
            # l.time(PATH+'time-n-opt-inversa')
            return list(xy)
            breakpoint
        previous = xy
    return (xy)


if __name__ == "__main__" :  
    seed = Matrix([[0.0],[0.0]])      
    for i in range(1):
        r = optimization(F, seed, TOLERANCE, MAX)
    print(r)