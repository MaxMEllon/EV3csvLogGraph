class ModuleList:
    def colums(self):
        return [
                'time',
                'turn',
                'speed',
                'battery',
                'angleL',
                'angleR',
                'bright',
                'gyro',
                'sonar'
                ]
    def show(self):
        for colum in self.colums():
            print(colum)
