import unittest
from matrix import Matrix

class MatrixTest(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix([[3,3,-15,9],[1,0,-2,1],[2,-1,-1,0]])
    def tearUp(self):
        self.matrix.dispose()
    def testChangeRows(self):
        self.matrix.changeRows(0,1)
        self.assertEqual(self.matrix.matrix[0],[1,0,-2,1])
        self.assertEqual(self.matrix.matrix[1],[3,3,-15,9])
    def testMultiplyRows(self):
        self.matrix.multiplyRow(3,0)
        self.assertEqual(self.matrix.matrix[0],[9,9,-45,27])
    def testScalarMultiplication(self):
        self.matrix.scalarMultiplication(3)
        self.assertEqual(self.matrix.matrix[0],[9,9,-45,27])
        self.assertEqual(self.matrix.matrix[1],[3,0,-6,3])
        self.assertEqual(self.matrix.matrix[2],[6,-3,-3,0])
    def testPrintMatrix(self):
        self.matrix.printMatrix()
    def testMatrixMultiplication(self):
        self.assertEqual(self.matrix.matrixMultiplication(Matrix([[1]])),None)
        newMatrix = self.matrix.matrixMultiplication(Matrix([[3,-1],[2,-1],[2,-1],[2,-1]]))
        self.assertEqual(newMatrix.matrix[0],[3,0])
        self.assertEqual(newMatrix.matrix[1],[1,0])
        self.assertEqual(newMatrix.matrix[2],[2,0])
    def testEchelonFormAndReducedEchelonForm(self):
        self.matrix.echelonForm()
        self.assertEqual(self.matrix.matrix[0],[3,0,-6,3])
        self.assertEqual(self.matrix.matrix[1],[0,-1,3,-2])
        self.assertEqual(self.matrix.matrix[2],[0,0,0,0])
        self.matrix.reducedEchelonForm()
        self.assertEqual(self.matrix.matrix[0],[1,0,-2,1])
        self.assertEqual(self.matrix.matrix[1],[0,1,-3,2])
        self.assertEqual(self.matrix.matrix[2],[0,0,0,0])
    
    
