from matrix import Matrix
from sys import exit
import re
def parseMatrix(matrixStr):
    numbers = re.findall('(?<!=)[0-9]+',matrixStr)
    cols = int(re.search('(?<=cols=)[1-9]+',matrixStr).group(0))
    rows = int(re.search('(?<=rows=)[1-9]+',matrixStr).group(0))
    matrixList = [[0 for col in range(cols)] for row in range(rows)]
    for row in range(len(matrixList)):
        for col in range(cols):
            matrixList[row][col] = numbers[row*cols+col]
    return Matrix(matrixList)
def main():
    variables = {}
    variableCommand = '[a-z]+'
    equalCommand = '='
    matrixCommand ='\[(([0-9]+),)+cols=[1-9][0-9]*,rows=[1-9][0-9]*\]'
    quitCommand = 'quit'

    while(True):
        userInput = input("")
        
        if(re.match(quitCommand,userInput)):
            break
        elif(re.match(equalCommand,userInput)):
            variableName = userInput[0:userInput.find('=')]
            variableValue =userInput[userInput.find('=')+1:len(userInput)]
            if(variableName in list(variables.keys())==False):
                variables.update({variableName:variableValue})
            else:
                variables[variableName] = variableValue
        elif(re.match(equalMatrixCommand,userInput)):
            print("toimii")
        elif(re.match(variableCommand,userInput)):
            if(userInput in list(variables.keys())):
                print(variables[userInput])
            else:
                print("No variable named ",userInput)
        
if __name__ == "__main__":
    main()
    
