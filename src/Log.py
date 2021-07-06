#!/usr/bin/env python

import sys
import csv
import time


class Log(object):
    _header = None
    
    
    def __init__(self):
        self._list = []
        self._start = time.time()


    def __repr__(self):
        ''' Return log file '''
        return self._list
    
    
    def time(self, path):
        ''' Return program execution time '''
        end = time.time()
        end -= self._start
        f = open(path+'.txt', 'a')
        f.write(str(end))
        f.write('\n')
        f.close()
        return (end)


    def set_header(self, header): 
        ''' set header of log file
                            
            Parameters
            ==========
                header
        '''
        self._header = header
    
    
    def append(self, value): 
        ''' Append value to the end of the log file 
                            
            Parameters
            ==========
                value
        '''
        self._list.append(value)
        
    
    def list2file(self, path):
        ''' Convert list to log file format .csv
                            
            Parameters
            ==========
                path: log file destination
        '''
        with open(path+'.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(self._header)
            for l in (self._list) :
                spamwriter.writerow(l)
                