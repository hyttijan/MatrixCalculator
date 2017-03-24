from matrix import Matrix
from sys import exit
import re
#parses string to matrix
def parseMatrix(matrixStr):
    #parses numbers
    numbers = re.findall('(?<!=)[0-9]+',matrixStr)
    #parses amount of columns
    cols = int(re.search('(?<=cols=)[1-9]+',matrixStr).group(0))
    #parses amount of rows
    rows = int(re.search('(?<=rows=)[1-9]+',matrixStr).group(0))
    #inits empty two-dimensional list for matrix
    matrixList = [[0 for col in range(cols)] for row in range(rows)]
    #puts numbers in the matrix
    for row in range(len(matrixList)):
        for col in range(cols):
            matrixList[row][col] = numbers[row*cols+col]
    return Matrix(matrixList)
def main():
    #dictionary for variables eg. matrixes,scalars
    variables = {}
    #regexes for things
    variableCommand = '[a-z]+'
    matrixCommand ='\[(([0-9]+),)+cols=[1-9][0-9]*,rows=[1-9][0-9]*\]'
    equalCommand = '='
    quitCommand = 'quit'
    #main-loop
    
    matrix = Matrix([[3,3,-15,9],[1,0,-2,1],[2,-1,-1,0]])
    newMatrix = matrix.matrixMultiplication(Matrix([[3,-1],[2,-1],[2,-1],[2,-1]]))
    newMatrix.printMatrix()
    while(True):
        matrix = Matrix([[3,2,1],[3,2,1],[2,2,2],[2,1,3]])
        matrix.gaussJordanElimination()
        matrix.printMatrix()
        userInput = input("")
        if(re.match(quitCommand,userInput)):
            break
        elif(re.match(equalCommand,userInput)):
            print("equal")
        elif(re.match(matrixCommand,userInput)):
            print("matrix")
            matrix = parseMatrix(userInput)
        elif(re.match(variableCommand,userInput)):
            print("variable")
        
if __name__ == "__main__":
    main()
    
