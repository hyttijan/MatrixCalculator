
import unittest
from matrix import Matrix
from main import parseMatrix
class MainTest(unittest.TestCase):
    
    def testParseMatrix(self):
        matrix = parseMatrix("3,3,-15,9,1,0,-2,1,2,-1,-1,0,cols=4,rows=3")
        self.assertEqual(matrix.matrix[0],[3,3,-15,9])
        self.assertEqual(matrix.matrix[1],[1,0,-2,1])
        self.assertEqual(matrix.matrix[2],[2,-1,-1,0])

if __name__ == '__main__':
    unittest.main()
