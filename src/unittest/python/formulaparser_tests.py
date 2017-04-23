import unittest
from formulaparser import FormulaParser

class ParserTest(unittest.TestCase):
    
    def setUp(self):
        self.parser = FormulaParser()
    
    def tearUp(self):
        self.matrix.dispose()
    def testParseExpression(self):
        self.assertEqual(self.parser.parseExpression("det([-2,3,2,0,1,-1,1,2,4,cols=3,rows=3])"),[-17])
        invertedMatrix = self.parser.parseExpression("inv([-2,3,2,0,1,-1,1,2,4,cols=3,rows=3])")
        self.assertEqual(invertedMatrix[0].matrix[0],[-0.3529411764705882,0.47058823529411764, 0.2941176470588235])
        self.assertEqual(invertedMatrix[0].matrix[1],[0.0588235294117647,0.5882352941176471, 0.1176470588235294])
        self.assertEqual(invertedMatrix[0].matrix[2],[0.058823529411764705,-0.411764705882353, 0.11764705882352941])
    def testParseMatrix(self):
        matrix = self.parser.parseMatrix("3,3,-15,9,1,0,-2,1,2,-1,-1,0,cols=4,rows=3")
        self.assertEqual(matrix.matrix[0],[3,3,-15,9])
        self.assertEqual(matrix.matrix[1],[1,0,-2,1])
        self.assertEqual(matrix.matrix[2],[2,-1,-1,0])
    