from sympy import lambdify, diff, Matrix, cos, sin, exp
from sympy.plotting import plot, plot3d
from sympy.abc import x,y

''' Reference
    https://sistemas.eel.usp.br/docentes/arquivos/519033/LOM3026/Metodos_numericos_calculo_sistemas_equacoes_nao_lineares.pdf
'''


if __name__ == "__main__" :
    euler = exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))
    f = 1 - euler + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )

    j = (Matrix([f]).jacobian([x,y]))
    
    j = lambdify([x,y], j)
    print(j(-1,2))
    