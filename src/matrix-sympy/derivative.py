from sympy import Symbol, diff, lambdify, sin, cos, tan
from sympy.abc import x

a = 10
f = ((cos(x)) - x**3 )
dx = f.diff(x)

print(f)
print(dx)

f = lambdify(x, f)
dx = lambdify(x, dx)

print(f(a))
print(dx(a))
