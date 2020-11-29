from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.plotting import plot, plot3d
from sympy.abc import x,y

from Error import * 
from Log import *

''' Reference
    https://codetobuy.com/downloads/newton-raphson-optimization-finding-min-or-max/
    https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
    http://people.duke.edu/~ccc14/sta-663-2016/12_MultivariateOptimizationAlgorithms.html
    https://sistemas.eel.usp.br/docentes/arquivos/519033/LOM3026/Metodos_numericos_calculo_sistemas_equacoes_nao_lineares.pdf
    https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization
    
    https://andreask.cs.illinois.edu/cs357-s15/public/demos/12-optimization/Newton's%20Method%20in%20n%20dimensions.html
    https://www.youtube.com/watch?v=H4rwPpfkPHw
'''

MAX = 20
PATH = 'log/newton-opt/'
TOLERANCE = 0.00000001 # 10**(-8)
F = 1 - (exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))) + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )


def hessiana(function):
    '''  Hessian: init and set  '''
    h = hessian(function, (x, y))
    return (lambdify([x,y], h))


def jacobian_transpose(function):
    '''  Jacobian: init and set  '''
    j = (Matrix([function]).jacobian([x,y])).transpose()
    return (lambdify([x,y], j))


def gauss_jordan(matrix_a, matrix_b ):
    sol, params = matrix_a.gauss_jordan_solve(matrix_b)
    taus_zeroes = { tau:0 for tau in params }
    return sol.xreplace(taus_zeroes)


def __repr__(xy, previous, hessian, jacobian, L, U, gauss_n, gauss_d):
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
    print('\n   Gauss D')
    pprint(Matrix(gauss_d))
    print('\n   Guass N')
    pprint(Matrix(gauss_n))
    print('_____________________________________________________\n')


def optimization(f, xy, tol, nmax) :
    l = Log() 
    e = Error()
    h = hessiana(f)
    j = jacobian_transpose(f)
    previous = xy
    
    for n in range(nmax) : 
        hh = h(float(xy[0]), float(xy[1]))
        jj = j(float(xy[0]), float(xy[1]))
        L, U, _ = Matrix(hh).LUdecomposition()
        
        gauss = gauss_jordan(Matrix(L), Matrix(-jj))   
        xy = xy + gauss_jordan(Matrix(U), Matrix(gauss))  

        e.matrix_norm(xy, previous)
        l.append([float(xy[0]), float(xy[1]), 
                  float(previous[0]), float(previous[1]), 
                  float(e._norm)])
        
        if (e._norm < tol) :
            l.set_header(['X axes', 'Y axes','X-1 axes', 'Y-1 axes',  'Matrix Norm'])
            l.list2file(PATH+'main-lu')
            l.time(PATH+'time-n-opt-lu')
            return list(xy)
            breakpoint   
        previous = xy
    return False


if __name__ == "__main__" :
    seed = Matrix([[0.0],[0.0]])
    for i in range(101):
        r = optimization(F, seed, TOLERANCE, MAX)
    print(r)