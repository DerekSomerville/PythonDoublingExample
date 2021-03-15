import unittest
from src.main.python.Stub.LoadFile import LoadFile
from src.main.python.Stub.LoadDelimitedFile import LoadDelimitedFile
from src.main.python.Stub.LoadStub import LoadStub

class LoadDelimitedFileTest(unittest.TestCase):

    def testGetFileDataFirstLineFirstColumn(self):
        loadDelimitedFile = LoadDelimitedFile()
        self.assertEqual("Game",loadDelimitedFile.getFileData("Games.csv")[0][0])


    def testSetFileDelimiter(self):
        loadDelimitedFile = LoadDelimitedFile()
        loadDelimitedFile.setFileDelimiter("e")
        self.assertEqual("Gam",loadDelimitedFile.getFileData("Games.csv")[0][0])

    def testGetFileDataFirstLineSize(self):
        loadDelimitedFile = LoadDelimitedFile()
        self.assertEqual(4, len(loadDelimitedFile.getFileData("Games.csv")[0]))

    def testGetFileDataFirstLineSizeStub(self):
        loadDelimitedFile = LoadDelimitedFile()
        loadDelimitedFile.setLoadFile(LoadStub())
        self.assertEqual(2, len(loadDelimitedFile.getFileData("Games.csv")[0]))

    def testSetFileDelimiter(self):
        loadDelimitedFile = LoadDelimitedFile()
        loadDelimitedFile.setLoadFile(LoadStub())
        loadDelimitedFile.setFileDelimiter("k")
        self.assertEqual("Dere",loadDelimitedFile.getFileData("Games.csv")[0][0])
