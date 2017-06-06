from csvList import CsvFile
from path import GetPath
from graph import Graph

def main():
    csvList = CsvFile()
    path = GetPath()
    graph = Graph()

    filePathList = csvList.pathlist()
    graph.graph(filePathList)

if __name__ == '__main__':
    main()
