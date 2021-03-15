from abc import ABC, abstractmethod

class Load(ABC):

    def getFileData(self,fileName):
        pass

    def getLastLines(self, fileName,numberOfLines):
        pass