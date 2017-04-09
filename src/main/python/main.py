
from matrix import Matrix
from parser import Parser

#program's main-method
def main():
    parser = Parser()
    parser.parseExpression("a=[3,2,1,2,rows=2,cols=2]")
    
if __name__ == "__main__":
    main()
    
