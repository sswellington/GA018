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
        ''' The difference between the measured or 
            inferred value of a quantity 
            x_(n) current and its actual value x_(n-1) 
                            
            Parameters
            ==========
                current, previous         
        '''
        self._absolute = (abs(current - previous))
        return self._absolute
    
    
    def relative(self, current, previous) :
        ''' Is the ratio of the absolute error of a measurement to the measurement being taken. 
            In other words, this type of error is relative to the size of the item being measured
                            
            Parameters
            ==========
                previous, previous
        '''
        if (current == 0):
            return ('Error 40: Current is equal 0.0') 
            breakpoint
        self._relative = abs( 1 -  (previous/current))
        return self._relative
    
    
    def matrix_norm(self, a, b):
        ''' Return float
            the Norm of a Matrix or Vector.
            In the simplest case this is the geometric size of the vector
            Other norms can be specified by the ord parameter
                            
            Parameters
            ==========
                a matrix, b matrix
        '''
        self._norm = abs(Matrix(a).norm(1) - Matrix(b).norm(1))
        return self._norm