# coding: utf-8
from src.main.python.Stub.Load import Load
class LoadFile(Load):
    filePathPrefix = "src/main/resource/"

    def getFileData(self,fileName):
        propertyFile = open(self.filePathPrefix + fileName,"r")
        fileData = propertyFile.read().replace('Â','').splitlines()
        propertyFile.close();
        return fileData

    def getLastLines(self, fileName,numberOfLines):
        lastLines = []
        fileData = self.getFileData(fileName);
        for counter in range(len(fileData)-numberOfLines,len(fileData)):
            lastLines.append(fileData[counter]);
        return lastLines