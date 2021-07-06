from sympy.matrices import Matrix


class Error(object):
    _absolute = None
    _relative = None
    _norm = None
    
    
    def __init__(self):
        _absolute = -10.987654321
        _relative = -10.987654321 
        _norm = -10.987654321
    
    
    def absolute(self, current, previous) :
        self._absolute = (abs(current - previous))
       
        return self._absolute
    
    
    def relative(self, current, previous) :
        if (current == 0):
            return ('Error 16: Current is equal 0.0') 
            breakpoint
        self._relative = abs( 1 -  (previous/current))
        
        return self._relative
    
    
    def matrix_norm(self, a, b) :
        self._norm = abs(Matrix(a).norm(1) - Matrix(b).norm(1))
        
        return self._norm