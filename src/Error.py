class Error(object):
    ''' https://en.wikipedia.org/wiki/Approximation_error '''
    _absolute = None
    _relative = None
    
    def __init__(self):
        _absolute = -9.9
        _relative = -9.9 
    
    def absolute(self, current, previous) :
        self._absolute = (abs(current - previous))
        return self._absolute
    
    def relative(self, current, previous) :
        if (current == 0):
            return ('Error 16: Current is equal 0.0') 
            breakpoint
        self._relative = abs( 1 -  (previous/current))
        return self._relative