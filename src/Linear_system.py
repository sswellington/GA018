from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.abc import x,y,w,z

class Linear_system(object):
    
    def __init__(self):
        pass
    
    
    def hessiana(self, function, c):
        h = hessian(function, c)
        self._hessiana = (lambdify(c, h))
        return self._hessiana
    
    
    def hessiana_inverse(self, function, c):
        h = (hessian(function, c)).inv()
        self._hessiana_inverse = (lambdify(c, h))
        return self._hessiana_inverse


    def jacobiana(self, function, c):
        j = (Matrix([function]).jacobian(c))
        self._jacobiana = (lambdify(c, j))
        return self._jacobiana
    
    
    def jacobiana_inverse(self, function, c):
        j = (Matrix(function).jacobian(c)).inv()
        self._jacobiana_inverse = (lambdify(c, j))
        return self._jacobiana_inverse
    
    
    def jacobiana_transpose(self, function, c):
        j = (Matrix([function]).jacobian(c)).transpose()
        self._jacobiana_transpose = (lambdify(c, j))
        return self._jacobiana_transpose


    def gauss_jordan(self, matrix_a, matrix_b ):
        sol, params = matrix_a.gauss_jordan_solve(matrix_b)
        taus_zeroes = { tau:0 for tau in params }
        self._gauss_jordan = sol.xreplace(taus_zeroes)
        return self._gauss_jordan