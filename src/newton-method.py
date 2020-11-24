''' Método de Newton: encontrar o mínimo dessa função '''

from sympy import lambdify, diff, cos, sin
from sympy.plotting import plot, plot3d
from sympy.abc import x


from Error import * 
from Log import *


MAX = 50
PATH = 'log/newton/'
TOLERANCE = 0.00000001 # 10**(-8)

                                 
def newton(fn, cx, tol, nmax) :
    l = Log()
    e = Error()
    previous = 0
    function = fn
    
    dx = fn.diff(x)
    dx = lambdify(x, dx)
    fn = lambdify(x, fn)
     
    for n in range(nmax) : 
        if (dx(cx) == 0) :
            return "Error 25: derivative less than zero"
            breakpoint
        cx = cx - (fn(cx) / dx(cx) )
        e.absolute(cx, previous)
        e.relative(cx, previous)
        l.append([cx, e._absolute, e._relative, fn(cx), dx(cx)])
        if (e._absolute < tol) :
            l.set_header(['x', 'absolute_error', 'relative_error', 'function', 'derivative'])
            l.list2file((PATH+str(function)))
            return cx
            breakpoint
        previous = cx
    return False


def run_test(function, a, TOLERANCE, MAX): 
    m = newton(function, a, TOLERANCE, MAX)
    print('f(x) =',f, '-> newton =', m)
    return m
    

if __name__ == "__main__":
    ''' Tests '''
    a = 0.5
    fx = [(cos(x) - x**3), ((x**3)-(2*x)+2), (x**2-4*x-5), (x ** 2 - 10), 
          (x**2 - 612), (x ** 3 - 2 * x - 5),((3*(x**3))-2), (x**6 - x - 1), (x**2-4*x-5)]
    
    for f in fx:
        r = run_test(f, a, TOLERANCE, MAX)
        # graph = plot(f, show=False)
        # graph.save('view/function/'+str(f))
        
        # graph = plot3d(f, show=False)
        # graph.save('view/function/3D/'+str(f))

        
