
from matrix import Matrix
from formulaparser import FormulaParser
import time
#program's main-method
def main():
    parser = FormulaParser()
    expression = input(">")
    while(expression!="quit"):
        answer = parser.parseExpression(expression)
        if(len(answer)==0):
            print("bad expression")
        elif(isinstance(answer[0],Matrix)):
            answer[0].printMatrix()
        else:
            print(answer[0])
        expression = input(">")
    
        
if __name__ == "__main__":
    main()
    
