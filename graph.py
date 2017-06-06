import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from path import GetPath
from moduleList import ModuleList

class Graph:
    def graph(self):
        path = GetPath()
        csvPath = path.path()
        module = ModuleList()

        csvFile = input("select csv file => ")
        if csvFile == 'exit':
            exit()
        csv = csvPath + csvFile

        module.module()

        selectModule = input("select module => ")
        if selectModule == 'exit':
            exit()


        df = pd.read_csv(csv, names=['time', 'turn', 'speed', 'battery', 'angleL', 'angleR', 'bright', 'gyro', 'sonar'])
        print(df.describe())
        plt.plot(range(0,29999), df[selectModule], marker="o")
        plt.title("sample code")
        plt.xlabel("sec")
        plt.ylabel("value")
        plt.xlim(xmax = 120, xmin = 0)
        plt.show()
