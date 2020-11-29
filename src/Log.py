import csv
import sys
import time


class Log(object):
    _header = None
    
    
    def __init__(self):
        self._list = []
        self._start = time.time()


    def __repr__(self):
        return self._list
    
    
    def p_time(self):
        end = time.time()
        end -= self._start
        return end 
    
    
    def time(self, path):
        end = time.time()
        end -= self._start
        f = open(path+'.txt', 'a')
        f.write(str(end))
        f.write('\n')
        f.close()
        return (end)


    def set_header(self, header): 
        self._header = header
    
    
    def append(self, value): 
        self._list.append( value)
        
    
    def list2file(self, path):
        with open(path+'.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(self._header)
            for l in (self._list) :
                spamwriter.writerow(l)