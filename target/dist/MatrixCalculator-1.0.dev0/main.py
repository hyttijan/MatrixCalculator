
from matrix import Matrix
from formulaparser import FormulaParser
import time
#program's main-method
def main():
    parser = FormulaParser()
    print(parser.parseExpression("det([-2,3,2,0,1,-1,1,2,4,cols=3,rows=3])"))
if __name__ == "__main__":
    main()
    
