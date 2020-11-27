from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp
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

MAX = 1
# PATH = 'log/newton/opt/'
TOLERANCE = 0.00000001 # 10**(-8)


def hessiana(function):
    '''  Hessian: init and set  '''
    h = hessian(function, (x, y))
    return (lambdify([x,y], h))


def hessian_inverse(function):
    '''  Hessian: init and set  '''
    h = (hessian(function, (x, y))).inv()
    return (lambdify([x,y], h))


def jacobian_transpose(function):
    '''  Jacobian: init and set  '''
    j = (Matrix([function]).jacobian([x,y])).transpose()
    return (lambdify([x,y], j))


def optimization(f, cx, cy, tol, nmax) :
    h = hessiana(f)
    j = jacobian_transpose(f)
    
    ''' X0  '''
    xy = (Matrix([[cx],[cy]]))
    print('XY =', xy.shape)
    
    for n in range(nmax) : 
        hh = h(float(xy[0]), float(xy[1]))
        jj = j(float(xy[0]), float(xy[1]))
        root = (xy) - (Matrix(hh) * Matrix(jj)) 
        print('hessiana = ',hh.shape )
        print('jacobian = ',jj.shape)
        print('kernel', root) 
        
        print('kernel =', root)
        print(xy[0], xy[1])
        print('hessiana = ',hh)
        print('jacobian = ',jj)
    return (xy)


if __name__ == "__main__" :
    f = 1 - (exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))) + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )
        
    r = optimization(f, 5.0, 2.0, TOLERANCE, MAX)
    
    print(r)