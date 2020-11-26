from sympy import lambdify, diff, Matrix, cos, sin, exp, pprint
from sympy.plotting import plot, plot3d
from sympy.abc import x,y

''' Reference
    https://sistemas.eel.usp.br/docentes/arquivos/519033/LOM3026/Metodos_numericos_calculo_sistemas_equacoes_nao_lineares.pdf
'''


def jacobian_transpose(function):
    '''  Jacobian: init and set  '''
    j = (Matrix([function]).jacobian([x,y])).transpose()
    return (lambdify([x,y], j))


if __name__ == "__main__" :
    euler = exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))
    f = 1 - euler + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )

    f = x**2 * y**3
    j = (Matrix([f]).jacobian([x,y]))
    j = j.transpose()
    
    j = lambdify([x,y], j)
    pprint(j(5,2))
    