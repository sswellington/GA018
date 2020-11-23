import math
import numpy as np
import matplotlib.pyplot as plt


PATH = 'view/'
GRAPH = 'bisection'
MAX = 30
TOLERANCE = 0.00001

log = [] # a, b, c, fnc

def function ( x ): 
    return ( x**3 - x - 2 )


def same_sign(product_a , product_b) :
    return ((product_a * product_b) > 0)


def bisection (fn, a, b, tol, nmax):
    ''' description
        is a root-finding method that applies to any continuous functions 
            for which one knows two values with opposite signs
        The method consists of repeatedly bisecting the interval defined 
            by these values and 
            then selecting the subinterval in which the function changes sign, 
            and therefore must contain a root.
    '''
    # Bolzano's Theorem: check the intermediate value of functions a and b
    if same_sign(fn(a), fn(b)):
        return "Error 32: Bolzano of Theorem"
        breakpoint
        
    # limit iterations to prevent infinit loop
    for n in range(nmax) : 
        # midpoint 
        c = ( (a+b) / 2)
        fn_c = fn(c) 
        log.append([ a, b, c, fn_c ])
        if (fn_c) == 0 or ((b-a)/2) < tol : 
            # soluction found
            return c
            breakpoint
        if same_sign(fn(a), fn_c) :
            a = c
        else :
            b = c
    return False


def graph(name) :
    len_log = len(log)
    x = np.arange(1,(len_log+1),1) 
    y = np.zeros((len_log), dtype=float)

    for i in range(len_log) :
        y[i] = ( math.log2(abs( log[i][3] )) )

    plt.plot(x, y, label = "blue", color="#6776FE", marker=".")

    x[:] = (x[:]-1)*(-1)
    plt.plot(x, label = "blue", color="#FF5733")

    plt.title(GRAPH+' '+name)
    plt.xlabel("Iteration axis")
    plt.ylabel("ln(|x0 - xn|) axis")
    plt.savefig(PATH+GRAPH+name+'.pdf', dpi=300)

if __name__ == "__main__":
    ''' Tests
        * test_0 = fx = ( x**3 - x - 2 ), a = 1, b = 2, c = 2.23606  
        * test_1 = fx = ( x**2 - 5 ), a = 0, b = 4, c = 1.521385
        * test_2 = fx = ( x**2 - 3 ), a = 0, b = 4, c = (3)^1/2
        * test_3 = fx = ( x**3 + x - 3), a = 0, b = 4, c = 1.2134170    
        * http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/07/bisection.html
   '''
    a = 1
    b = 2

    result = ( bisection(function, a, b, TOLERANCE, MAX) )
    print(result)
    result = str(int(result*10000))
    graph(result)