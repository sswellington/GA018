def newton(fn, point, tol, nmax) :
    l = Log()
    e = Error()
    j = jacobiana(fn,[x,y,w,z])
    f = lambdify([x,y,w,z], fn)
    previous = point
    
    for n in range(nmax) : 
        jj = j(float(point[0]),float(point[1]),
               float(point[2]),float(point[3]))
        ff = f(float(point[0]),float(point[1]),
               float(point[2]),float(point[3]))
        L, U, _ = Matrix(jj).LUdecomposition()
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
            l.list2file((PATH_N+'main-lu-pr'))
            l.time(PATH_N+'time-n-sys-lu-pr')
            return point
            breakpoint
        previous = point
    return False