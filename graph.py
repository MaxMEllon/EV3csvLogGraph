import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from path import GetPath
from moduleList import ModuleList

class Graph:
    def graph(self, filePathList):
        index = input("select csv file. if you want to close this program, then select `q` => ")
        csvFile = filePathList[int(index)]

        if csvFile == 'q':
            exit()

        module = ModuleList()
        module.show()

        selectModule = input("select module => ")
        if selectModule == 'exit':
            exit()
        df = pd.read_csv(open(csvFile), names=module.colums(), encoding='utf-8', engine='python')
        print(df.describe())
        lineNum = sum(1 for line in open(csvFile))
        print(lineNum)
        plt.plot(range(0, lineNum), df[selectModule], marker="o")
        plt.title("sample code")
        plt.xlabel("sec")
        plt.ylabel("value")
        plt.xlim(xmax = 120, xmin = 0)
        plt.show()
