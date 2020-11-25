from sympy import Function, hessian, pprint
from sympy.abc import x, y

''' Hessian matrix 
    Compute Hessian matrix 
    for a function f wrt parameters in varlist 
    which may be given as a sequence or a row/column vector. 
    A list of constraints may optionally be given.
    
    References:  https://en.wikipedia.org/wiki/Hessian_matrix
'''

if __name__ == "__main__" :
    
    # f = 2*x - y + 2*x*y - x**2 - y**2
    f = x**2 + y**2

    print((hessian(f, (x, y))).inv())