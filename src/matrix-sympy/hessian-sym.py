from sympy import Function, lambdify, diff, hessian, pprint
from sympy.abc import x, y

''' Hessian matrix 
    Compute Hessian matrix 
    for a function f wrt parameters in varlist 
    which may be given as a sequence or a row/column vector. 
    A list of constraints may optionally be given.
    
    References:  https://en.wikipedia.org/wiki/Hessian_matrix
        http://people.duke.edu/~ccc14/sta-663-2016/12_MultivariateOptimizationAlgorithms.html
        https://www.youtube.com/watch?v=tWh1S8oCglA
        https://www.youtube.com/watch?v=H4rwPpfkPHw
'''

def hessian_inverse(function):
    '''  Hessian: init and set  '''
    h = (hessian(function, (x, y))).inv()
    return (lambdify([x,y], h))

if __name__ == "__main__" :
    
    # f = 2*x - y + 2*x*y - x**2 - y**2
    f = x**2 * y**3
    
    h = hessian_inverse(f)
    print(h(5, 2))
    
    # pprint((hessian(f, (x, y))).inv())

    

    
    