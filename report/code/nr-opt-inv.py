def optimization_inv(f, xy, tol, nmax) :
    
    l = Log() 
    e = Error()
    h = hessiana_inverse(f)
    j = jacobian_transpose(f)
    previous = xy
    
    for n in range(nmax
    
        hh = (h(float(xy[0]), float(xy[1])))
        jj = (j(float(xy[0]), float(xy[1])))
        
        xy = xy - (Matrix(hh) * Matrix(jj)) 
        
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
            
            return list(xy)
            breakpoint
            
        previous = xy
        
    return (xy)