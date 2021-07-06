def hessiana(function, c):
    '''  Hessian: init and set  '''
    h = hessian(function, c)
    return (lambdify(c, h))


def hessiana_inverse(function, c):
    '''  Hessian: init and set  '''
    h = (hessian(function, c)).inv()
    return (lambdify(c, h))


def jacobiana(function, c):
    '''  Jacobian: init and set  '''
    j = (Matrix([function]).jacobian(c))
    return (lambdify(c, j))


def jacobian_inversa(function, c):
    '''  Jacobian: init and set  '''
    j = (Matrix(function).jacobian(c)).inv()
    return (lambdify(c, j))


def jacobian_transpose(function, c):
    '''  Jacobian: init and set  '''
    j = (Matrix([function]).jacobian(c)).transpose()
    return (lambdify(c, j))


def gauss_jordan(matrix_a, matrix_b ):
    '''  Gauss: init and set  '''
    sol, params = matrix_a.gauss_jordan_solve(matrix_b)
    taus_zeroes = { tau:0 for tau in params }
    return sol.xreplace(taus_zeroes)