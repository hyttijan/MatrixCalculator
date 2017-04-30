
from matrix import Matrix
from formulaparser import FormulaParser
import time
#program's main-method
def main():
    parser = FormulaParser()
    for i in range(1,10):
        print(i)
        matrix = Matrix([[0]])
        matrix2 = Matrix([[0]])
        matrix = Matrix(matrix.initEmptyMatrixList(i,i))
        matrix = matrix.formIdentityMatrix()
        matrix2 = Matrix(matrix2.initEmptyMatrixList(i,i))
        matrix2 = matrix2.formIdentityMatrix()
        start = time.time()
        matrix.addMatrix(matrix2)
        end = time.time()
        print(end-start)
        
if __name__ == "__main__":
    main()
    
