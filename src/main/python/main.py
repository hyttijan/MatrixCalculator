
from matrix import Matrix
from formulaparser import FormulaParser
import time
#program's main-method
def main():
    parser = FormulaParser()
    numbers = [3,9,12]
    matrices = [Matrix for i in range(len(numbers))]
    for i in range(len(numbers)):
        matrixList = [0 for k in range(numbers[i])]
        for j in range(numbers[i]):
            matrixList[j] = [0 for z in range(j)]
            matrixList[j].extend([1 for z in range(j,numbers[i])])
        matrices[i] = Matrix(matrixList)
    for i in range(len(numbers)):
        first = time.time()
        matrices[i].invertMatrix()
        print(time.time()-first)
if __name__ == "__main__":
    main()
    
