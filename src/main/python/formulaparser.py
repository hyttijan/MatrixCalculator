import re
from matrix import Matrix

class FormulaParser:
    
    def __init__(self):
        self.constantPattern = re.compile("(<?=matrix)-*([0-9]|[1-9][0-9]+)")
        self.numberPattern = re.compile("-*([0-9]|[1-9][0-9]+)")
        self.detPattern = re.compile("det")
        self.invPattern = re.compile("inv")
        self.transposePattern = re.compile("trans")
        self.matrixPattern = re.compile("matrix([1-9][0-9]+|[0-9])")
        self.matrixPattern2 = re.compile("(det|inv|trans)\(matrix([1-9][0-9]+|[0-9])\)")
        self.matrixCommand = re.compile('\[(-*([0-9]|[1-9][0-9]+),)+((cols=[1-9][0-9]*,rows=[1-9][0-9]*)|(rows=[1-9][0-9]*,cols=[1-9][0-9]*))\]')
        self.multiplyPattern = re.compile('(matrix([1-9][0-9]+|[0-9])*matrix([1-9][0-9]+|[0-9]))|(matrix([1-9][0-9]+|[0-9])*(-*([1-9][0-9]|[0-9])))')
        self.addCommand = re.compile('\+')
        self.substractCommand = re.compile('\-')
        self.multiplyCommand = re.compile('\*')
        self.quitCommand = re.compile('quit')
        
    """ Parses matches of given command  and returns list of matches. """
    def parseMatches(self,expression,command):
        matchIterator = command.finditer(expression)
        return list(matchIterator)
    
    """ Parses expression """
    def parseExpression(self,expression):
        self.expression = expression
        matrices = self.parseMatrices()
        matrices = self.parseMatrices2(matrices)
        return matrices
    
    """ Parses matrices and stores them into matrices array. Also replaces matrices with 'matrix' and index. """             
    def parseMatrices(self):
        matricesMatches = self.parseMatches(self.expression,self.matrixCommand)
        matrices = []
        for i in range(len(matricesMatches)):
            matrices.append(self.parseMatrix(matricesMatches[i].group(0)));
            self.expression = self.expression.replace(matricesMatches[i].group(0),"matrix"+repr(i),1)
        return matrices
    
    """ Parses determinant,inversion and transpose functions """
    def parseMatrices2(self,matrices):
        result = self.parseMatches(self.expression,self.matrixPattern2);
        while(len(result)!= 0):
            for i in range(len(result)):
                """ Parses the matrixe's index """
                index = self.numberPattern.search(result[i].group(0)).group(0)
                if(self.detPattern.search(result[i].group(0))!=None):
                    matrices[int(index)] = matrices[int(index)].countDeterminant()
                elif(self.invPattern.search(result[i].group(0))!=None):
                    matrices[int(index)] = matrices[int(index)].invertMatrix()
                else:
                    matrices[int(index)] = matrices[int(index)].transpose()
                self.expression = self.expression.replace(result[i].group(0),"matrix"+index)
            result = list(self.matrixPattern2.finditer(self.expression))
        return matrices
    
    """ Parses string to matrix. """
    def parseMatrix(self,matrixStr):
        
        #parses list of numbers as strings
        numbers = re.findall('(?<!=)-*[0-9]+',matrixStr)
        #parses amount of columns
        cols = int(re.search('(?<=cols=)[1-9]+',matrixStr).group(0))
        #parses amount of rows
        rows = int(re.search('(?<=rows=)[1-9]+',matrixStr).group(0))
        #inits empty two-dimensional list for matrix
        matrixList = [[0 for col in range(cols)] for row in range(rows)]
        if(len(numbers) != cols*rows):
            print("Amount of numbers in matrix does not equal rows x cols")
            return None;
        #puts numbers in the matrix
        for row in range(len(matrixList)):
            for col in range(cols):
                matrixList[row][col] = float(numbers[row*cols+col])  #convert string to float before assigning
        return Matrix(matrixList)
            