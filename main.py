from csvList import CsvFile
from path import GetPath
from graph import Graph

def main():
    csvList = CsvFile()
    path = GetPath()
    graph = Graph()

    fileList = csvList.pathlist()
    graph.graph()

if __name__ == '__main__':
    main()
