import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy.linalg import norm
from math import isnan


def jacobian_1(x):
    """Jacobiano do sistema 5.7.2 da pagina 175 do livro 
    Numerical Methods in Economics, de Keneth Judd."""
    return np.array([[.2 * x[0] ** (-.8), .2 * x[1] ** (-.8)],
                     [.1 * x[0] ** (-.9), .4 * x[1] ** (-.6)]])


def jacobian_2(x):
    """Jacobiano do sistema 5.7.3 da pagina 175 do livro 
    Numerical Methods in Economics, de Keneth Judd."""
    return np.array([[5. * (x[0] ** .2 + x[1] ** .2) ** 4. * .2 * x[0] ** (-.8),
                      5. * (x[0] ** .2 + x[1] ** .2) ** 4. * .2 * x[1] ** (-.8)],
                     [4. * (x[0] ** .1 + x[1] ** .4) ** 3. * .1 * x[0] ** (-.9),
                      4. * (x[0] ** .1 + x[1] ** .4) ** 3. * .4 * x[1] ** (-.6)]])


def function_1(x):
    """Sistema 5.7.2 da pagina 175 do livro 
    Numerical Methods in Economics, de Keneth Judd."""
    return np.array([x[0] ** .2 + x[1] ** .2 - 2.,
                     x[0] ** .1 + x[1] ** .4 - 2.])


def function_2(x):
    """Sistema 5.7.2 da pagina 175 do livro 
    Numerical Methods in Economics, de Keneth Judd."""
    return np.array([(x[0] ** .2 + x[1] ** .2) ** 5. - 32.,
                     (x[0] ** .1 + x[1] ** .4) ** 4. - 16.])


def newton(function, jacobian, initial, e=0.00001, d=0.00001, print_iter=True,
           plot_iter = False):
    """Funcao que aplica o metodo de Newton-Raphson a funcao 'function' com
    jacobiano 'jacobian' inseridos como funcoes do Python. 'initial' e o ponto
    inicial para as iteracoes. 'e' e o nivel de precisao desejado e d e a
    precisao desejada em relacao ao resultado. 'print_iter' escolhe se quer
    que imprima os pontos intermediarios das iteracoes e 'plot_iter' escolhe
    se quer imprimir estes pontos num grafico."""
    x = initial
    iter = 0
    while True:
        try:
            if print_iter:
                print(x)
            if plot_iter:
                plt.scatter(x[0], x[1])
            s = np.dot(-inv(jacobian(x)), function(x)) # Equacao do metodo
            x_ante = x
            x = x + s
            iter += 1
            if norm(x_ante - x) <= e * (1 + norm(x)) or isnan(x[0]) or\
               isnan(x[1]): # Verifica criterio de convergencia
                break
        except:
            print("Erro")
            break
    if norm(function(x)) <= d: # Verifica se a solucao atende criterio
        print("Convergiu em " + str(iter) + " iterações iniciando em " +\
              str(np.round(initial, 2)))
        return x
    else:
        print("Método não convergiu iniciando em " + str(np.round(initial, 2)))

# O loop abaixo roda o metodo no retangulo [0,2]**2 para function_1
for i in (np.array(range(20))+1.)/10:
    for j in (np.array(range(20))+1.)/10:
        newton(function_1, jacobian_1, [i, j], print_iter=False)

# O loop abaixo roda o metodo no retangulo [0,2]**2 para function_2
for i in (np.array(range(20))+1.)/10:
    for j in (np.array(range(20))+1.)/10:
        newton(function_2, jacobian_2, [i, j], print_iter=False)

###############################################################################
# Note que os loops acima mostram que a transformacao da function_2 tornou    #
# a convergencia mais rapida, exigindo em media uma iteracao a menos no       #
# dominio testado                                                             #
###############################################################################

# O comando abaixo imprime um grafico com os pontos da iteracao da function_1
newton(function_1, jacobian_1, [2, 2], plot_iter=True)

# O comando abaixo imprime um grafico com os pontos da iteracao da function_2
newton(function_2, jacobian_2, [2, 2], plot_iter=True)