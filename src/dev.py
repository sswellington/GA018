from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.plotting import plot, plot3d
from sympy.abc import x,y

from Error import * 
from Log import *

''' Reference
    https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
    http://people.duke.edu/~ccc14/sta-663-2016/12_MultivariateOptimizationAlgorithms.html
    https://sistemas.eel.usp.br/docentes/arquivos/519033/LOM3026/Metodos_numericos_calculo_sistemas_equacoes_nao_lineares.pdf

    https://andreask.cs.illinois.edu/cs357-s15/public/demos/12-optimization/Newton's%20Method%20in%20n%20dimensions.html
'''

MAX = 1
PATH = 'log/newton/'
TOLERANCE = 0.00000001 # 10**(-8)


def hessian_inverse(function):
    '''  Hessian: init and set  '''
    h = (hessian(function, (x, y))).inv()
    return (lambdify([x,y], h))


def jacobian_transpose(function):
    '''  Jacobian: init and set  '''
    j = (Matrix([function]).jacobian([x,y])).transpose()
    return (lambdify([x,y], j))


def optimization(f, cx, cy, tol, nmax) :
    h = hessian_inverse(f)
    j = jacobian_transpose(f)
    
    ''' X0  '''
    xy = (Matrix([[cx],[cy]]))
    print('XY =', xy.shape)
    
    for n in range(nmax) : 
        hessiana = h(xy[0], xy[1])
        jj = j(xy[0], xy[1])
        root = (xy) - (Matrix(hessiana) * Matrix(jj)) 
        print('hessiana = ',hessiana.shape )
        print('jacobian = ',jj.shape)
        print('kernel', root) 
        
        # print('kernel =', kernel)
        # # print(xy[0], xy[1])
        # print('hessiana = ',hessiana)
        # print('jacobian = ',jj)
    
    return (xy)


if __name__ == "__main__" :
    # euler = exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))
    # f = 1 - euler + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )
    
    # f = 1 - (exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))) + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )
     
    f = x**2 * y**3
        
    r = optimization(f, 5, 2, TOLERANCE, MAX)
    
    # print(r)