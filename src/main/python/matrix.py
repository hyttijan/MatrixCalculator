class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
    #method to change in matrix
    def changeRows(self,row1,row2):
        tempRow = self.matrix[row1][:]
        self.matrix[row1] = self.matrix[row2]
        self.matrix[row2] = tempRow
    def multiplyRow(self,multiplier,row):
        for i in range(len(self.matrix[row])):
            self.matrix[row][i] = self.matrix[row][i]*multiplier
    def addRowToAnother(self,row1,row2,multiplier):
        for i in range(len(self.matrix[row1])):
            self.matrix[row2][i]=self.matrix[row2][i]+self.matrix[row1][i]*multiplier
    def printMatrix(self):
        for i in range(len(self.matrix)):
            print("[ ",end="")
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j]," ",end="")
            print("]")
        print("")
    def matrixMultiplication(self,secondMatrix):
        if(len(self.matrix[0])==len(secondMatrix.matrix)):
            list = [0 for x in range(len(self.matrix))]
            for i in range(len(list)):
                list[i] = [0 for y in range(len(secondMatrix.matrix[0]))]
            for i in range(len(list)):
                for j in range(len(list[0])):
                    for k in range(len(self.matrix[0])):
                        list[i][j] = list[i][j]+self.matrix[i][k]*secondMatrix.matrix[k][j]
            return Matrix(list)
        return None
    def scalarMultiplication(self,scalar):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = scalar*self.matrix[i][j];
    def gaussJordanElimination(self):
        self.echelonForm();
        self.reducedEchelonForm();
    def echelonForm(self):
        column = 0;
        for i in range(len(self.matrix)):
            self.pushZeroRowsDown(i,column);
            if(self.matrix[i][column]!=0):
                self.decrementToZero(column);
                column=column+1;
            self.printMatrix();
    def reducedEchelonForm(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])-1):
                if(self.matrix[i][j]!=1 and self.matrix[i][j]!=0):
                    multiplier = 1/self.matrix[i][j]
                    self.multiplyRow(multiplier,i)
                    break;
        self.printMatrix();
        
    def decrementToZero(self,column):   
        for i in range(len(self.matrix)):
            if(i!=column):
                multiplier = self.matrix[i][column]/self.matrix[column][column];
                if(multiplier!=0):
                    multiplier=-multiplier
                self.addRowToAnother(column,i,multiplier)        
    def pushZeroRowsDown(self,column,k):
        for i in range(k,len(self.matrix)-1):
            if(self.matrix[i][column]==0):
                for j in range(len(self.matrix)-1,i,-1):
                    if(self.matrix[j][column]!=0):
                        self.changeRows(i,j)
                        break;
