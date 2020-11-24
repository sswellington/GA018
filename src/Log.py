import csv

class Log(object):
    
    _list = []
    _header = None
    
    def __init__(self, list):
        self._list = list

    def __repr__(self):
        return self._list


    def set_header(self, header): 
        self._header = header

    
    def list2file(self, path):
             
        with open(path+'.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(self._header)
            for l in (self._list) :
                spamwriter.writerow(l)