from src.main.python.Foundation.LoadFile import LoadFile

class LoadDelimitedFile:

    fileDelimiter = ","

    def setFileDelimiter(self,delimiter):
        self.fileDelimiter = delimiter

    def getFileData(self,fileName):
        delimitedData = []
        loadFile = LoadFile()
        fileData = loadFile.getFileData(fileName)
        for row in fileData:
            delimitedData.append(row.split(self.fileDelimiter))
        return delimitedData