from sympy import lambdify, diff, hessian, jacobi, cos, sin, exp, pprint
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
# from sympy.abc import x,y,w,z

class Linear_system(object):
    
    def __init__(self):
        pass
    
    
    def hessiana(self, function, coefficient):
        ''' Compute Hessian matrix for a function 
                and the inverse of matrix
                
            Parameters
            ==========
                function, coefficient
        '''
        h = hessian(function, coefficient)
        self._hessiana = (lambdify(coefficient, h))
        return self._hessiana
    
    
    def hessiana_inverse(self, function, coefficient):
        ''' Compute Hessian matrix for a function 
                
            Parameters
            ==========
                function, coefficient
        '''
        h = (hessian(function, coefficient)).inv()
        self._hessiana_inverse = (lambdify(coefficient, h))
        return self._hessiana_inverse


    def jacobiana(self, function, coefficient):
        ''' Calculates the Jacobian matrix 
                (derivative of a vector-valued function).
            
            Parameters
            ==========
                function, coefficient
        '''
        j = (Matrix([function]).jacobian(coefficient))
        self._jacobiana = (lambdify(coefficient, j))
        return self._jacobiana
    
    
    def jacobiana_inverse(self, function, coefficient):
        ''' Calculates the Jacobian matrix 
                (derivative of a vector-valued function).
                and the inverse of matrix
                            
            Parameters
            ==========
                function, coefficient
        '''
        j = (Matrix(function).jacobian(coefficient)).inv()
        self._jacobiana_inverse = (lambdify(coefficient, j))
        return self._jacobiana_inverse
    
    
    def jacobiana_transpose(self, function, coefficient):
        ''' Calculates the Jacobian matrix 
                (derivative of a vector-valued function).
                and the transpose of matrix
                            
            Parameters
            ==========
                function, coefficient
        '''
        j = (Matrix([function]).jacobian(coefficient)).transpose()
        self._jacobiana_transpose = (lambdify(coefficient, j))
        return self._jacobiana_transpose


    def gauss_jordan(self, matrix_a, matrix_b ):
        ''' Solves linear equation where the unique solution exists. 
                            
            Parameters
            ==========
                a matrix, b matrix
        '''
        sol, params = matrix_a.gauss_jordan_solve(matrix_b)
        taus_zeroes = { tau:0 for tau in params }
        self._gauss_jordan = sol.xreplace(taus_zeroes)
        return self._gauss_jordan