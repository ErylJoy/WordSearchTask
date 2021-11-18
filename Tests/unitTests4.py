import unittest
import sys
import os.path
import random as r
# Make tools and solutions accessible 
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

from Tools import PuzzleGenerator
from Tools import RandomWordGen
from Solutions import versionFour as v 

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
with open("../Resources/testwords.txt", "r") as f: testWords = f.read().splitlines()
with open("../Resources/testgrid.txt", "r") as f: testGrid = f.read().splitlines()
solver = v.WordSearch(testGrid, 1000);


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        global testGrid
        global testWords
        global solver
        self.testGrid = testGrid
        self.testWords = testWords
        self.solver = solver
        

    def testFindsAWordInThePuzzle(self):
        result = self.solver.is_present(self.testWords[r.randint(0,len(self.testWords))]);
        self.assertEqual(result, True)

    def testDoesNotFindNonPresentWords(self):
        result = self.solver.is_present("thisisimpossible");
        self.assertEqual(result, False)
    
    def testRejectsWordsWithCapitals(self):
        testWordAsArr = list(self.testWords[r.randint(0,len(self.testWords)-1)])
        indexInWord = r.randint(0, len(testWordAsArr)-1)
        testWordAsArr[indexInWord] = testWordAsArr[indexInWord].upper()
        testWord = "".join(testWordAsArr)
        result = self.solver.is_present(testWord);
        self.assertEqual(result, False)

    def testRejectsStringsWithSpaces(self):
        result = self.solver.is_present("not possible");
        self.assertEqual(result, False)
    
    def testRejectsStringsWithSpecialCharacters(self):
        result = self.solver.is_present("notpossible!");
        self.assertEqual(result, False)

    def testRejectsStringsLongerThan24(self):
        result = self.solver.is_present("aaaaaaaaaaaaaaaaaaaaaaaah")# 25 char long
        self.assertEqual(result, False)

    def testFindsAllProvidedWordsInSearch(self):
        result = True
        for word in self.testWords:
            if not self.solver.is_present(word):
                result = False
        self.assertEqual(result, True)

    def testOneCharInUniformGrid(self):
        localSolver = v.WordSearch(['b','b','b','b'], 2)
        result = localSolver.is_present("a") 
        self.assertEqual(result, False)

    def testRowOverFlow(self):
        localSolver = v.WordSearch(['a','b','b','a'], 2)
        result = localSolver.is_present("bb") 
        self.assertEqual(result, False)

    def testHidingAtEnd(self):
        localSolver = v.WordSearch(['a','a','a','b'], 2)
        result = localSolver.is_present("b") 
        self.assertEqual(result, True)

    def testHidingAtBeginning(self):
        localSolver = v.WordSearch(['b','a','a','a'], 2)
        result = localSolver.is_present("b") 
        self.assertEqual(result, True)
        
if __name__ == '__main__':
    unittest.main()