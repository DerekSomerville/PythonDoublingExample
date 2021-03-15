from src.main.python.Stub.Load import Load
class LoadStub(Load):
    def getFileData(self,fileName):
        result = []
        result.append("Derek,Somerville")
        result.append("Matt,Barr")
        return result

    def getLastLines(self, fileName,numberOfLines):
        pass
