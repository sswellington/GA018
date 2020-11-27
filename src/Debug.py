import sys


class Debug(object): 
    def __init__(self, path):
        self._path = path 
        self._buff = ''
    
    
    def buff(self, msg): 
        self._buff = msg
        
    
    def save(self):
        original_stdout = sys.stdout # Save a reference to the original standard output
        with open(self._path+'.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print(self._buff)
            sys.stdout = original_stdout # Reset the standard output to its original value
