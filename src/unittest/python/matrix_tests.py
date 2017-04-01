import unittest
from matrix import Matrix

class MatrixTest(unittest.TestCase):
    

    def setUp(self):
        self.matrix = Matrix([[3,3,-15,9],[1,0,-2,1],[2,-1,-1,0]])
        self.matrix2 =  Matrix([[1,2,3,4],[5,6,7,0],[0,0,-1,0],[8,9,-4,-2]])
        self.matrix3 = Matrix([[-2,3,2],[0,1,-1],[1,2,4]])
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
    
    def testCountDeterminant(self):
        self.assertEqual(Matrix([[1],[1]]).countDeterminant(),None)
        self.assertEqual(Matrix([[1]]).countDeterminant(),1)
        self.assertEqual(self.matrix2.countDeterminant(),4)
        self.assertEqual(self.matrix3.countDeterminant(),-17)