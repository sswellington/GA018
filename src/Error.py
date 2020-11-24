class Error(object):
    
    _absolute = None
    _relative = None
    
    def __init__(self):
        _absolute = -9.9
        _relative = -9.9 
    
    def absolute(self, current, previous) :
        self._absolute = (abs(current - previous))
        return self._absolute
    
    def relative(self, current, previous) :
        self._relative = (abs(current - previous)) / (abs(current))
        return self._relative