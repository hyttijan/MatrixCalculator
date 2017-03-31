import re
from matrix import Matrix

#parses string to matrix
def parseMatrix(matrixStr):
    #parses numbers
    numbers = re.findall('(?<!=)-*[0-9]+',matrixStr)
    #parses amount of columns
    cols = int(re.search('(?<=cols=)[1-9]+',matrixStr).group(0))
    #parses amount of rows
    rows = int(re.search('(?<=rows=)[1-9]+',matrixStr).group(0))
    #inits empty two-dimensional list for matrix
    matrixList = [[0 for col in range(cols)] for row in range(rows)]
    #puts numbers in the matrix
    for row in range(len(matrixList)):
        for col in range(cols):
            matrixList[row][col] = int(numbers[row*cols+col])
    return Matrix(matrixList)

#program's main-method
def main():
    #dictionary for variables eg. matrixes,scalars
    variables = {}
    #regexes for things
    variableCommand = '[a-z]+'
    matrixCommand ='\[(([0-9]+),)+cols=[1-9][0-9]*,rows=[1-9][0-9]*\]'
    equalCommand = '='
    quitCommand = 'quit'

if __name__ == "__main__":
    main()
    
