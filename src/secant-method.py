from sympy import lambdify, diff, cos, sin
from sympy.abc import x

from Error import * 
from Log import *


MAX = 50
PATH = 'log/secant/'
TOLERANCE = 0.00000001 # 10**(-8)


def secant(f, a, b, tol, nmax):
    ''' Secant method
        Return the root calculated using the secant method.
    '''
    l = Log()
    e = Error()
    previous = 0
    fn = f 
    
    f = lambdify(x, f)
    if (f(a) == f(b)) :
        return 'Error 20: a and b functions have the same value'
        breakpoint
    for i in range(nmax):
        c = b - f(b) * (b - a) / (float(f(b) - f(a)))
        e.absolute(c, previous)
        e.relative(c, previous)
        l.append([c, e._absolute, e._relative, f(a), f(b)])
        if (e._absolute < tol) :
            l.set_header(['x', 'absolute_error', 'relative_error', 'function(a)', 'function(b)'])
            l.list2file((PATH+str(fn)))
            return c
            breakpoint
        a, b = b, c
        previous = c
    return False

def run_test(function, a, b, TOLERANCE, MAX):
    m = secant(function, a, b, TOLERANCE, MAX)
    print('f(x) =',function,' >>> secant =', m)
    return m

if __name__ == "__main__":
    a = 0.5
    fx = [(cos(x) - x**3), (x**2 - 612), ((x**3)-(2*x)+2), (x**6 - x - 1)]
    fn = (cos(x) - x**3)

    for f in fx:
        run_test(f, a, a*2, TOLERANCE, MAX)