def optimization(f, xy, tol, nmax) :
    l = Log() 
    e = Error()
    h = hessiana(f,[x,y])
    j = jacobian_transpose(f,[x,y])
    previous = xy
    
    for n in range(nmax) : 
        hh = h(float(xy[0]), float(xy[1]))
        jj = j(float(xy[0]), float(xy[1]))
        
        L, U, _ = Matrix(hh).LUdecomposition()
        
        gauss = gauss_jordan(Matrix(L), Matrix(-jj))   
        xy = xy + gauss_jordan(Matrix(U), Matrix(gauss))  

        e.matrix_norm(xy, previous)
        l.append([float(xy[0]), float(xy[1]), 
                  float(previous[0]), float(previous[1]), 
                  float(e._norm)])
        
        if (e._norm < tol) :
            l.set_header(['X axes'  ,'Y axes',  'W axes'  ,'Z axes',
                          'X-1 axes','Y-1 axes','W-1 axes','Z-1 axes',  
                          'Matrix Norm'])
            l.list2file((PATH+'main-inversa'))
            l.time(PATH+'time-n-opt-inversa')
            
            return xy
            breakpoint
            
        previous = xy
    return False