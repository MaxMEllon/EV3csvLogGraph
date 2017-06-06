import glob
from path import GetPath

class CsvFile:
    def pathlist(self):
        path = GetPath()

        csvFiles = glob.glob(path.path() + '*.csv')

        print("--- csv file list---\n")
        for index, file in enumerate(csvFiles):
            print('{0} : {1}' . format(index, file))
        return csvFiles
