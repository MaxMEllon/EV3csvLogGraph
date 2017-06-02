import os
from path import GetPath

class CsvFile:
    def pathlist(self):
        path = GetPath()

        listPath = path.path()

        csvFiles = os.listdir(listPath)

        print("--- csv file list---\n")
        for file in csvFiles:
            print(file)
