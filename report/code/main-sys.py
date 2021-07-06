MAX = 200
PATH_N = 'log/newton-sys/'
PATH_Q = 'log/quasi-newton/'
TOLERANCE = 0.00000001 # 10**(-8)

PL = 15     # weight * lenght
K = 100     # proportionality

M = Matrix([[K * (x    ) - ((7 * PL) / 2 ) * cos(x) - K * (y - x)],
            [K * (y - x) - ((5 * PL) / 2 ) * cos(y) - K * (w - y)],
            [K * (w - y) - ((3 * PL) / 2 ) * cos(w) - K * (z - w)],
            [K * (z - w) - ((    PL) / 2 ) * cos(z)]]) 
            

if __name__ == "__main__" :
    
    seed_pr = Matrix([[1],[1],
                      [1],[1]])
                     
    seed = Matrix   ([[1],[2],
                      [3],[4]])
    
    for i in range(101):
        q = quasi_newton(M, seed_pr, TOLERANCE, MAX)
        n = newton(M, seed_pr, TOLERANCE, MAX)
        
        q = quasi_newton(M, seed, TOLERANCE, MAX)
        n = newton(M, seed, TOLERANCE, MAX)
