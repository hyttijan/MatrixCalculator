import re
from matrix import Matrix

class Parser:
    
    def __init__(self):
        self.variables = {}
        self.variableCommand = re.compile('(^([cols]|[rows]))[a-z]+')
        self.matrixCommand = re.compile('\[(([0-9]+),)+cols=[1-9][0-9]*,rows=[1-9][0-9]*\]')
        self.equalCommand = re.compile('=')
        self.addCommand = re.compile('\+')
        self.addCommand = re.compile('\-')
        self.multiplyCommand = re.compile('\*')
        self.quitCommand = re.compile('quit')
        
    # Parses expression 
    def parseExpression(self,expression):
        matrixMatches = self.parseMatches(expression,self.matrixCommand)
        
    # Parses matches of given command
    def parseMatches(self,expression,command):
        matchIterator = command.finditer(expression)
        return list(matchIterator)
    
    # Parses string to matrix
    def parseMatrix(self,matrixStr):
        #parses list of numbers as strings
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
                matrixList[row][col] = float(numbers[row*cols+col])  #convert string to float before assigning
        return Matrix(matrixList)
    
    