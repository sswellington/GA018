def newton_inv(fn, point, tol, nmax) :
    l = Log()
    e = Error()
    j = jacobian_inversa(fn,[x,y,w,z])
    f = lambdify([x,y,w,z], fn)
    previous = point
    
    for n in range(nmax) : 
        ff = f(float(point[0]),float(point[1]),
               float(point[2]),float(point[3]))
        jj = j(float(point[0]),float(point[1]),
               float(point[2]),float(point[3]))
        point = point - (Matrix(jj) * Matrix(ff)) 
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
            l.list2file((PATH+'main-inversa'))
            l.time(PATH+'time-n-sys-inversa')
            return point
            breakpoint
        previous = point
    return False