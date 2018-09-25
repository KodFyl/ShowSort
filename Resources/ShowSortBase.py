import sys
import os
import re
import shelve
import shutil

'''                             Show Sort.
A tool for organising TV Shows and their episodes. 

Author Name: Labeeb Latheef
Version: 1.0 Beta'''

class Sort():
    def __init__(self, dirPath, pattern, dest, showName):
        
        if dirPath == '':
            self.dirPath = os.getcwd()
        else:
            self.dirPath = dirPath
        
        self.pattern = pattern
        self.newPattern = '.*' + pattern.replace('*', '[0-9]') + '.*'
        self.showName = showName
        
        if dest =='':
            self.dest = os.getcwd()
        else:
            self.dest = dest
    
    def start_operation(self):
        checkDir = False
        if not self.dirPath =='':
            try:
                os.chdir(self.dirPath)
            except:
                return False                
            else:
                checkDir = True
        else:
            checkDir = True

        if checkDir == True:    
            self.cwd = os.getcwd()
            return True

    def extract_data(self):
        
        self.dataShelve = shelve.open("ShowSort.dat")
        self.dataShelve.clear()
        
        patRegX = re.compile(self.newPattern)
        for curDir, incDir, incFiles in os.walk(self.dirPath):
            for files in incFiles:
                match = patRegX.search(files)
                if not match == None:
                    sNo = match.group(1)
                    eNo = match.group(2)
                    if sNo in self.dataShelve.keys():
                        temp = self.dataShelve[sNo]
                        temp.update({eNo : os.path.join(curDir, files)})
                        self.dataShelve[sNo] = temp
                    else:
                        self.dataShelve[sNo] = {eNo : os.path.join(curDir, files)}
       
        self.filecount = len(self.dataShelve)
        return self.filecount
