''' Método de Newton: encontrar o mínimo dessa função '''

from sympy import lambdify, diff, cos, sin, exp
from sympy.abc import x

from Error import * 
from Log import *


MAX = 50
PATH = 'log/newton-opt/'
TOLERANCE = 0.00000001 # 10**(-8)
                                 
                                 
def newton_optimization(fn, cx, tol, nmax) :
    l = Log()
    e = Error()
    previous = 0
    
    dx = fn.diff(x)
    dx2 = dx.diff(x)
    
    dx = lambdify(x, dx)
    dx2 = lambdify(x, dx2)

    for n in range(nmax) : 
        if (dx2(cx) == 0) :
            return "Error 27: derivative less than zero"
            breakpoint
        cx = cx - (dx(cx) / dx2(cx) )
        e.absolute(cx, previous)
        l.append([cx, e._absolute, dx(cx), dx2(cx)])
        if (e._absolute < tol) :
            l.set_header(['x', 'absolute_error', 'function', 'derivative'])
            l.list2file((PATH+str(fn)))
            return cx
            breakpoint
        previous = cx
    return False


def run_test(function, a, TOLERANCE, MAX): 
    m = newton_optimization(function, a, TOLERANCE, MAX)
    print('f(x) =',function, '-> newton optimization =', m)
    return m



if __name__ == "__main__":
    
    ''' Tests
        https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization
    '''
    
    log = []
    a = .0000005
    fx = [(cos(x) - x**3), (x**2 - 612), ((x**3)-(2*x)+2), (x**6 - x - 1), (x**3-6*x**2+4*x+2)]
    
    euler = exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((x-2)**2)/(2*(0.5**2)) )  ))
    fx = [1 - euler + ( 0.04 * (((x-1)**2) + ((x-2)**2)) )]
   
    for f in fx:
        run_test(f, a, TOLERANCE, MAX)