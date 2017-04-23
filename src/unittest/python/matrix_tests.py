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
        self.assertIsNone(self.matrix.matrixMultiplication(Matrix([[1]])))
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
        self.assertIsNone(Matrix([[1],[1]]).countDeterminant())
        self.assertEqual(Matrix([[1]]).countDeterminant(),1)
        self.assertEqual(self.matrix2.countDeterminant(),4)
        self.assertEqual(self.matrix3.countDeterminant(),-17)
        
    def testTranspose(self):
        transposedMatrix = self.matrix.transpose()
        self.assertEqual(transposedMatrix.matrix[0],[3,1,2])
        self.assertEqual(transposedMatrix.matrix[1],[3,0,-1])
        self.assertEqual(transposedMatrix.matrix[2],[-15,-2,-1])
        self.assertEqual(transposedMatrix.matrix[3],[9,1,0])
    
    def testInvertMatrix(self):
        self.assertIsNone(self.matrix.invertMatrix())
        invertedMatrix = self.matrix3.invertMatrix()
        self.assertEqual(invertedMatrix.matrix[0],[-0.3529411764705882,0.47058823529411764, 0.2941176470588235])
        self.assertEqual(invertedMatrix.matrix[1],[0.0588235294117647,0.5882352941176471, 0.1176470588235294])
        self.assertEqual(invertedMatrix.matrix[2],[0.058823529411764705,-0.411764705882353, 0.11764705882352941])
    
    
    def testAttachMatrices(self):
        attachedMatrix = self.matrix3.attachMatrices(Matrix([[1,0,0],[0,1,0],[0,0,1]]))
        self.assertEqual(attachedMatrix.matrix[0],[-2,3,2,1,0,0])
        self.assertEqual(attachedMatrix.matrix[1],[0,1,-1,0,1,0])
        self.assertEqual(attachedMatrix.matrix[2],[1,2,4,0,0,1])
    
    def testFormIdentityMatrix(self):
        identityMatrix = self.matrix.formIdentityMatrix()
        self.assertIsNone(identityMatrix)
        identityMatrix = self.matrix3.formIdentityMatrix()
        self.assertEqual(identityMatrix.matrix[0],[1,0,0])
        self.assertEqual(identityMatrix.matrix[1],[0,1,0])
        self.assertEqual(identityMatrix.matrix[2],[0,0,1])
    