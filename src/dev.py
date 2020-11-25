from sympy import lambdify, diff, hessian, cos, sin, exp
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.plotting import plot, plot3d
from sympy.abc import x,y

from Error import * 
from Log import *

''' Reference
    https://sistemas.eel.usp.br/docentes/arquivos/519033/LOM3026/Metodos_numericos_calculo_sistemas_equacoes_nao_lineares.pdf
'''

MAX = 50
PATH = 'log/newton/'
TOLERANCE = 0.00000001 # 10**(-8)

def optimization(f, cx, cy, tol, nmax) :
    h = (hessian(f, (x, y))).inv()
    h = lambdify([x,y], h)

    j = (Matrix([f]).jacobian([x,y]))
    j = lambdify([x,y], j)
    
    xy = (Matrix([cx,cy]))
    
    kernel = h(xy[0], xy[1]) * j(xy[0], xy[1])
    xy = kernel * xy
    
    return (xy[0], xy[1])


if __name__ == "__main__" :
    euler = exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))
    f = 1 - euler + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )
     
    f = x**2 + y**2
        
    r = optimization(f, 5, 7, TOLERANCE, MAX)
    
    print(r)