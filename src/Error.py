class Error(object):
    
    _absolute = None
    _relative = None
    
    def __init__(self):
        _absolute = -9.9
        _relative = -9.9 
    
    def absolute(self, atual, previous) :
        self._absolute = (abs(atual - previous))
        return self._absolute
    
    def relative(self, atual, previous) :
        self._relative = (abs(atual - previous)) / (abs(atual))
        return self._relative