def quasi_newton(fn, point, tol, nmax) :
    l = Log()
    e = Error()
    j = jacobiana(fn,[x,y,w,z])
    f = lambdify([x,y,w,z], fn)
    previous = point
    
    jj = j(float(point[0]),float(point[1]),
          float(point[2]),float(point[3]))
    L, U, _ = Matrix(jj).LUdecomposition()
    
    for n in range(nmax) : 
        ff = f(float(point[0]),float(point[1]),
              float(point[2]),float(point[3]))
        g = gauss_jordan(Matrix(L), Matrix(-ff))
        point = point + gauss_jordan(Matrix(U), Matrix(g))  
        e.matrix_norm(point, previous)
        
        l.append([float(point[0]), float(point[1]), 
                  float(point[2]), float(point[3]), 
                  float(previous[0]),float(previous[1]),
                  float(previous[2]),float(previous[3]), 
                  float(e._norm)])
        
        if (e._norm < tol) :
            l.set_header(['X axes'  ,'Y axes',  'W axes'  ,'Z axes',
                          'X-1 axes','Y-1 axes','W-1 axes','Z-1 axes',  
                          'Matrix Norm'])
            l.list2file((PATH_Q+'main-jab-pr'))
            l.time(PATH_Q+'time-qn-sys_pr')
            return point
            breakpoint
        previous = point
    pprint(point)
    return False
