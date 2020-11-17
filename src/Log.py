import csv

class Log(object):
    
    _list = []
    
    def __init__(self, list):
        self._list = list


    def __repr__(self):
        return self._list
    
    def list2file(self, path, header ):
             
        with open(path, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(header)
            for l in (self._list) :
                spamwriter.writerow(l)