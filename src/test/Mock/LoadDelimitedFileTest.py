import unittest
from src.main.python.Mock.LoadFile import LoadFile
from src.main.python.Mock.LoadDelimitedFile import LoadDelimitedFile

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