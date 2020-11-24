from sympy import *
from sympy.abc import x, y

from Error import * 
from Log import *


MAX = 1
PATH = 'log/newton/'
TOLERANCE = 0.00000001 # 10**(-8)


def newton2D(fn, cx, cy, tol, nmax) :
    previous = 0
    f = (lambdify(['x','y'], fn))
    
    for n in range(nmax) : 
        cx = cx
    
    # for n in range(nmax) : 
    #     if (dx(cx) == 0) :
    #         return "Error 21: derivative less than zero"
    #         breakpoint
    #     cx = cx - (fn(cx) / dx(cx) )
    #     error = (abs(previous - cx))
    #     log.append([cx, error, fn(cx), dx(cx)])
    #     if (error < tol) :
    #         return cx
    #         breakpoint
    #     previous = cx
        
    return cx

if __name__ == "__main__" :
    # euler = exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))
    # fn = 1 - euler + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )
    
    log = [] # x, erro, fn, dx
    a = 0.0000001
    f =  (x**2 - 612)

    
    print( newton2D(f, a, 2, TOLERANCE, MAX) )
    
    