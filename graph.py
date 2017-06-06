import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from path import GetPath
from moduleList import ModuleList

class Graph:
    def graph(self, filePathList):
        index = input("select csv file. if you want to close this program, then select `q` => ")
        print(filePathList)
        csvFile = filePathList[int(index)]

        if csvFile == 'q':
            exit()

        module = ModuleList()
        module.module()

        selectModule = input("select module => ")
        if selectModule == 'exit':
            exit()
        csv = open(csvFile)
        df = pd.read_csv(csv, names=['time', 'turn', 'speed', 'battery', 'angleL', 'angleR', 'bright', 'gyro', 'sonar'], encoding='utf-8', engine='python')
        print(df.describe())
        plt.plot(range(0,29999), df[selectModule], marker="o")
        plt.title("sample code")
        plt.xlabel("sec")
        plt.ylabel("value")
        plt.xlim(xmax = 120, xmin = 0)
        plt.show()
