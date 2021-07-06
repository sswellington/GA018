MAX = 20
PATH = 'log/newton-opt/'
TOLERANCE = 0.00000001 # 10**(-8)
F = 1 - (exp(
            - ((((x-1)**2) / (2*(0.75**2))) 
            + (( (y-2)**2) / (2*(0.5**2)))))) 
            + ( 0.04 * (((x-1)**2) + ((y-2)**2)))


if __name__ == "__main__" :
    seed = Matrix([[0.0],[0.0]])
    for i in range(1):
        n = optimization(F, seed, TOLERANCE, MAX)
        t = optimization_inv(F, seed, TOLERANCE, MAX)