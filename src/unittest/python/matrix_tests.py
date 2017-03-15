import unittest
from matrix import Matrix

class MatrixTest(unittest.TestCase):
    def setUp(self):
         self.matrix = Matrix([[1,2],[2,1]])
    def tearUp(self):
        self.matrix.dispose()
    def testChangeRows(self):
        self.matrix.changeRows(0,1)
        self.assertEqual(self.matrix.matrix[0],[2,1])
        self.assertEqual(self.matrix.matrix[1],[1,2])
    def testMultiplyRows(self):
        self.matrix.multiplyRow(3,0)
        self.assertEqual(self.matrix.matrix[0],[3,6])
    
