class ModuleList:
    def columns(self):
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
        for column in self.columns():
            print(column)
