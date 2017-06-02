class GetPath:
    def path(self):
        path = open('path.txt', 'r')

        for csvPath in path:
            csvPath
        path.close()

        csvPath = csvPath.rstrip("\n")
        return csvPath + "/"
