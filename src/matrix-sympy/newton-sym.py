from sympy import symbols, cos
from sympy.codegen.algorithms import newtons_method_function
from sympy.codegen.pyutils import render_as_module
from sympy.core.compatibility import exec_


x = symbols('x')
expr = cos(x) - x**3

func = newtons_method_function(expr, x)
py_mod = render_as_module(func)  # source code as string
namespace = {}
exec_(py_mod, namespace, namespace)

res = eval('newton(0.5)', namespace)
abs(res - 0.865474033102) < 1e-12

print(res)