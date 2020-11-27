from sympy import Matrix


''' Solves Ax = B using Gauss Jordan elimination.
    There may be zero, one, or infinite solutions. 
    If one solution exists, it will be returned. 
    f infinite solutions exist, it will be returned parametrically. 
    If no solutions exist, It will throw ValueError
'''

def gauss_jordan(matrix_a, matrix_b ):
    sol, params = matrix_a.gauss_jordan_solve(matrix_b)
    taus_zeroes = { tau:0 for tau in params }
    return sol.xreplace(taus_zeroes)
    

a = Matrix([[1,3,1],[1,1,-1],[3,11,5]])
b = Matrix([[9],[1],[35]])

# a = Matrix([[1,0],[0,1]])
# b = Matrix([[0.32],[0]])

print(gauss_jordan(a,b))