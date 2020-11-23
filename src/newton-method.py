''' Método de Newton: encontrar o mínimo dessa função '''

from sympy import *

from Log import *


MAX = 50
PATH = 'log/newton/'
TOLERANCE = 0.00000001 # 10**(-8)
                                 
def newton(fn, cx, tol, nmax) :
    previous = 0
    
    dx = fn.diff(x)
    dx = lambdify(x, dx)
    fn = lambdify(x, fn)
     
    for n in range(nmax) : 
        if (dx(cx) == 0) :
            return "Error 21: derivative less than zero"
            breakpoint
        cx = cx - (fn(cx) / dx(cx) )
        error = (abs(previous - cx))
        log.append([cx, error, fn(cx), dx(cx)])
        if (error < tol) :
            return cx
            breakpoint
        previous = cx
        
    return False
      

if __name__ == "__main__":
    
    ''' Tests
        * test_0 = f(x) = (x**2 - 612); f'(x) = 2x;  x = 10
        * test_1 = f(x) = cos(x) - x**3; f'(x) = - sin(x) - 3x**2; x = 0.5
            * f(x) = ((cos(x)) - x**3 )
            * d(x) = ( - (sin(x)) - 3*(x**2) )
        * test_3 = f(x) = x**6 - x - 1; f'(x) = 6*(x**5) - 1
    '''
    
    log = [] # x, erro, fn, dx
    x = Symbol('x')
    
    a = 0.0000001
    f =  (x**2 - 612)

    print(newton(f, a, TOLERANCE, MAX))
    
    t = Log(log)
    # t.list2file((PATH+'xp2-612.csv'), ['x', 'error', 'function', 'derivative'])