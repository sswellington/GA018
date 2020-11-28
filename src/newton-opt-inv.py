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

MAX = 50
PATH = 'log/newton-opt/'
TOLERANCE = 0.00000001 # 10**(-8)
F = 1 - (exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))) + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )


def hessiana(function):
    '''  Hessian: init and set  '''
    h = hessian(function, (x, y))
    return (lambdify([x,y], h))


def hessiana_inverse(function):
    '''  Hessian: init and set  '''
    h = (hessian(function, (x, y))).inv()
    return (lambdify([x,y], h))


def jacobian_transpose(function):
    '''  Jacobian: init and set  '''
    j = (Matrix([function]).jacobian([x,y])).transpose()
    return (lambdify([x,y], j))


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


def optimization(f, cx, cy, tol, nmax) :
    l = Log() 
    e = Error()
    h = hessiana_inverse(f)
    j = jacobian_transpose(f)
    xy = (Matrix([[cx],[cy]]))
    previous = xy
    
    for n in range(nmax) : 
        hh = (h(float(xy[0]), float(xy[1])))
        jj = (j(float(xy[0]), float(xy[1])))
        xy = Matrix(xy) - (Matrix(hh) * Matrix(jj)) 
        
        e.absolute(xy, previous)
        l.append([float(xy[0]), float(xy[1]), 
                  float(previous[0]), float(previous[1]), 
                  float(e._absolute[0]), float(e._absolute[1])])
        
        if (e._absolute[0] < tol and e._absolute[1] < tol ) :
            l.set_header(['X axes', 'Y axes','X-1 axes', 'Y-1 axes',  'absolute error of X axes', 'absolute error Y axes'])
            l.list2file((PATH+'main-inversa'))
            l.time(PATH+'time-n-opt-inversa')
            return list(xy)
            breakpoint
        previous = xy
    return (xy)


if __name__ == "__main__" :        
    for i in range(101):
        r = optimization(F, 0.0, 0.0, TOLERANCE, MAX)
    print(r)