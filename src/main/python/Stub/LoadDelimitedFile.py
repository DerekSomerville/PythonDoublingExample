from src.main.python.Stub.LoadFile import LoadFile

class LoadDelimitedFile:

    fileDelimiter = ","
    loadFile = LoadFile()

    def setFileDelimiter(self,delimiter):
        self.fileDelimiter = delimiter

    def setLoadFile(self,load):
        self.loadFile = load


    def getFileData(self,fileName):
        delimitedData = []
        fileData = self.loadFile.getFileData(fileName)
        for row in fileData:
            delimitedData.append(row.split(self.fileDelimiter))
        return delimitedData