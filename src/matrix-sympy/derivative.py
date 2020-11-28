from sympy import Symbol, diff, lambdify, sin, cos, tan

c = 10
x = Symbol('x')

f = ((cos(x)) - x**3 )
dx = f.diff(x)

print(f)
print(dx)

f = lambdify(x, f)
dx = lambdify(x, dx)

print(f(c))
print(dx(c))
