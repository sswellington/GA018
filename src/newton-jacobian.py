from sympy import lambdify, diff, Matrix, cos, sin, exp
from sympy.plotting import plot, plot3d
from sympy.abc import x,y

import matplotlib.pyplot as plt

from Error import * 
from Log import *


MAX = 50
PATH = 'log/newton-jacobian/'
TOLERANCE = 0.00000001 # 10**(-8)


if __name__ == "__main__" :
    euler = exp(-( ( ((x-1)**2)/(2*(0.75**2)) ) + ( ((y-2)**2)/(2*(0.5**2)) )  ))
    f = 1 - euler + ( 0.04 * (((x-1)**2) + ((y-2)**2)) )
    
    # fn = (lambdify(['x','y'], fn))
    # print(fn(1,1))
    
    print(f)
    plot3d(f, show=False).save('view/function/3D/job')
