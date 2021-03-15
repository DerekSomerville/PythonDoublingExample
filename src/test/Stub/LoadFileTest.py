import unittest
from src.main.python.Stub.LoadFile import LoadFile



class LoadFileTest(unittest.TestCase):

    loadFile = LoadFile()

    def testGetFileDataSize(self):
        self.assertEqual(9,len(self.loadFile.getFileData("Games.csv")))

    def testGetFileDataFirstRow(self):
        self.assertEqual("Game,Release Date,Developer,Price", self.loadFile.getFileData("Games.csv")[0])

    def testGetFileDataSecondRow(self):
        self.assertEqual("DOOM,1993,id Software,£9.99", self.loadFile.getFileData("Games.csv")[1])

    def testGetLastLinesOne(self):
        self.assertEqual("God of War,2005,SCE,£19.99",self.loadFile.getLastLines("Games.csv",1)[0])
