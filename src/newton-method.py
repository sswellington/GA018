''' Método de Newton: encontrar o mínimo dessa função '''

import csv
from sympy import *

MAX = 50
PATH = 'log/newton/'
TOLERANCE = 0.00000001 # 10**(-8)

log = [] # x, erro, fn, dx
x = Symbol('x')


def list_repr( list ) :
    c = 0  
    for l in list : 
        print('i =', c, 'x =', l[0], 'e =', l[1], 'fx =', l[2], 'dx =', l[3])    
        c = c + 1 
    return list[-1]


def list2file( my_list, path ) :
    with open(path, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['x', 'error', 'function', 'derivative'])
        for l in my_list :
            spamwriter.writerow(l)

                                 
def newton(fn, cx, tol, nmax) :
    previous = 0
    
    dx = fn.diff(x)
    dx = lambdify(x, dx)
    fn = lambdify(x, fn)
    
    if (dx(cx) == 0) :
        return False
        breakpoint
        
    for n in range(nmax) : 
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
    
    a = 0.0000001
    f =  (x**2 - 612)

    print(newton(f, a, TOLERANCE, MAX))

    list2file(log, (PATH+'xp2-612.csv') )