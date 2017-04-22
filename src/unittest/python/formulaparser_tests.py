import unittest
from formulaparser import FormulaParser

class ParserTest(unittest.TestCase):
    
    def setUp(self):
        self.parser = FormulaParser()
    
    def tearUp(self):
        self.matrix.dispose()
    
    def testParseMatrix(self):
        matrix = self.parser.parseMatrix("3,3,-15,9,1,0,-2,1,2,-1,-1,0,cols=4,rows=3")
        self.assertEqual(matrix.matrix[0],[3,3,-15,9])
        self.assertEqual(matrix.matrix[1],[1,0,-2,1])
        self.assertEqual(matrix.matrix[2],[2,-1,-1,0])
    