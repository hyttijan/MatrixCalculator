
from matrix import Matrix
from formulaparser import FormulaParser
import time
#program's main-method
def main():
    parser = FormulaParser()
    matrix = Matrix([[1,0,0],[1,0,0],[1,0,0]])
    matrix2 = Matrix([[1,1,1],[0,0,0],[0,0,0]])
    matrix.matrixMultiplication(matrix2).printMatrix()
if __name__ == "__main__":
    main()
    
