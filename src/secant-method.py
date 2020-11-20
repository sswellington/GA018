MAX = 50
TOLERANCE = 0.00000001 # 10**(-8)


def function ( x ): 
    return x ** 2 - 612


def secant_method(f, a, b, tol, nmax):
    ''' Secant method
        Return the root calculated using the secant method.
    '''
    previous = 0
    for i in range(nmax):
        c = b - f(b) * (b - a) / (float(f(b) - f(a)))
        error = (abs(previous - c))
        log.append([c, error, f(a), f(b)])
        if (error < tol) :
            return c
            breakpoint
        a, b = b, c
        previous = c
    return False


if __name__ == "__main__":
    log = [] # x, erro, fn_a, fn_b

    print(secant_method(function, 10, 30, TOLERANCE, MAX))