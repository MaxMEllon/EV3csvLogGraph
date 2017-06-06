import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from path import GetPath
from moduleList import ModuleList

class Graph:
    def graph(self, filePathList):
        index = input("select csv file. if you want to close this program, then select `q` => ")
        if index == 'q':
            exit()

        module = ModuleList()
        module.show()

        selectedColumn = input("select colum. if you want to close this program, then select `q` => ")

        if selectedModule == 'q':
            exit()

        csvFile = filePathList[int(index)]
        df = pd.read_csv(open(csvFile), names=module.columns(), encoding='utf-8', engine='python')
        print(df.describe())
        lineNum = sum(1 for line in open(csvFile))
        plt.plot(range(0, lineNum), df[selectedColumn], marker="o")
        plt.title("sample code")
        plt.xlabel("sec")
        plt.ylabel("value")
        plt.xlim(xmax = 120, xmin = 0)
        plt.show()
