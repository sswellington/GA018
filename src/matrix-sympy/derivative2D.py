#!/usr/bin/env python

from sympy import *
from sympy.abc import x, y


def diff2D(function) : 
    dxy = (function.diff(x) + function.diff(y)) 
    return (lambdify(['x','y'], dxy))


if __name__ == "__main__":    
    euler = exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))
    fn = 1 - euler + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )
    
    f = x**6 - y**2 - 1
    
    a = diff2D(f)
    print(a(2,5))
    