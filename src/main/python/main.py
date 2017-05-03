
from matrix import Matrix
from formulaparser import FormulaParser
#program's main-method
def main():
    parser = FormulaParser()
    expression = input(">")
    while(expression!="quit"):
        try:
            answer = parser.parseExpression(expression)
            if(isinstance(answer[0],Matrix)):
                answer[0].printMatrix()
            else:
                print(answer[0])
        except Exception:
            print("bad expression")
        expression = input(">")
    
        
if __name__ == "__main__":
    main()
    
