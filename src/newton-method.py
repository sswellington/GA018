''' Método de Newton
    * encontrar o mínimo dessa função:
'''

from sympy import *

MAX = 200
TOLERANCE = 0.00000001 # 10**(-8)

log = [] # x, erro
x = Symbol('x')


def list_repr( list ) :
    c = 0  
    for l in list : 
        print('i =', c, 'x =', l[0], 'e =', l[1] )   
        c = c + 1 
    return list[-1]


def newton(fn, y, tol, nmax) :
    previous = 0
    
    dx = fn.diff(x)
    dx = lambdify(x, dx)
    fn = lambdify(x, fn)
    
    if (dx == 0) :
        return False
        breakpoint
        
    for n in range(nmax) : 
        y = y - (fn(y) / dx(y) )
        error = (abs(previous - y))
        log.append([y, error])
        
        if (error < tol) :
            return y
            breakpoint
        previous = y
        
    return False
      

if __name__ == "__main__":
    
    ''' Tests
        * test_0 = f(x) = (x**2 - 612); f'(x) = 2x;  x = 10
        * test_1 = f(x) = cos(x) - x**3; f'(x) = - sin(x) - 3x**2; x = 0.5
            * f(x) = ((cos(x)) - x**3 )
            * d(x) = ( - (sin(x)) - 3*(x**2) )
        * test_3 = f(x) = x**6 - x - 1; f'(x) = 6*(x**5) - 1
    '''
    
    a = 0.0000001
    f = ((cos(x)) - x**3 )

    r = newton(f, a, TOLERANCE, MAX)   
    # print(r) 
    
    list_repr(log)
    
