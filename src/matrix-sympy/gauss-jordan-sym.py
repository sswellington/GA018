from sympy import Matrix


A = Matrix([[1, 2, 1, 1], [1, 2, 2, -1], [2, 4, 0, 6]])
B = Matrix([7, 12, 4])

print(A.gauss_jordan_solve(B))

z = Matrix.zeros(2,1)

print(z)