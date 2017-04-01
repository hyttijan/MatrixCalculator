class Matrix:
    
    
    def __init__(self, matrix):
        self.matrix = matrix
        
    #swaps two rows in matrix
    def changeRows(self, row1, row2):
        tempRow = self.matrix[row1][:]
        self.matrix[row1] = self.matrix[row2]
        self.matrix[row2] = tempRow
        
    #multiplies one row in matrix with multiplier
    def multiplyRow(self, multiplier, row):
        for column in range(len(self.matrix[row])):
            self.matrix[row][column] = self.matrix[row][column]*multiplier
            
    #adds one row to another with multiplier
    def addRowToAnother(self, row1, row2, multiplier):
        for column in range(len(self.matrix[row1])):
            self.matrix[row2][column]=(self.matrix[row2][column]
                                       + self.matrix[row1][column]
                                       * multiplier)
                    
    def printMatrix(self):
        for row in range(len(self.matrix)):
            print("[ ",end="")
            for column in range(len(self.matrix[row])):
                print(self.matrix[row][column], " ", end="")
            print("]")
        print("")
        
    #multiplies matrix with another matrix
    def matrixMultiplication(self, secondMatrix):
        #check that matrixes can be multiplied
        #first matrixes column count must equal second matrixe's row count
        if (len(self.matrix[0]) == len(secondMatrix.matrix)):
            #init empty two-dimensional matrixList for new matrix
            matrixList = [0 for row in range(len(self.matrix))]
            for row in range(len(matrixList)):
                matrixList[row] = [0 for column in range(len(secondMatrix.matrix[0]))]
            #count the new matrix
            for row in range(len(matrixList)):
                for column in range(len(matrixList[0])):
                    for k in range(len(self.matrix[0])):
                        matrixList[row][column] = (matrixList[row][column]
                                                   + self.matrix[row][k]
                                                   * secondMatrix.matrix[k][column])
            return Matrix(matrixList)
        #if matrixes cannot be multiplied return None
        return None
    
    #multiplies matrix with scalar
    def scalarMultiplication(self, scalar):
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                #multiplies each row and column with scalar
                self.matrix[row][column] = scalar*self.matrix[row][column]
                
    def gaussJordanElimination(self):
        self.echelonForm()
        self.reducedEchelonForm()
        
    #forms echelon form from the matrix
    def echelonForm(self):
        column = 0
        for row in range(len(self.matrix)):
            self.pushZeroRowsDown(row,column)
            if (self.matrix[row][column] != 0):
                self.decrementToZero(column)
                #if there are more columns than rows
                #cannot increment column index
                #last rows will be zero rows
                if (column < len(self.matrix[0])-1):
                    column = column+1
                    
    #forms reduced echelon form from echelon form matrix
    def reducedEchelonForm(self):
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])-1):
                #leave alone if value in current entry is already 1 or 0
                if (self.matrix[row][column] != 1 and self.matrix[row][column] != 0):
                    #otherwise count the multiplier so that the leading coefficient is 1
                    multiplier = 1/self.matrix[row][column]
                    #apply the multiplier to all the other entries on the current row
                    self.multiplyRow(multiplier,row)
                    break
                
    #decrements all the elements in rows in this column to zero except the one where row's index equals column's index
    def decrementToZero(self, column):   
        for row in range(len(self.matrix)):
            if (row != column):
                multiplier = self.matrix[row][column]/self.matrix[column][column]
                if (multiplier != 0):
                    multiplier = -multiplier
                self.addRowToAnother(column, row, multiplier)
                
    #pushes all the rows with zeros in the current column down
    def pushZeroRowsDown(self, row, column):
        #start pushing down rows from current row
        for row2 in range(row,len(self.matrix)-1):
            #if row has zero column in current column check for non-zero rows from bottom to up
            if (self.matrix[row2][column] == 0):
                for row3 in range(len(self.matrix)-1,row2,-1):
                    if (self.matrix[row3][column] != 0):
                        self.changeRows(row3, row2)
                        break
                    
    def generateList(self,removedCol):
        #init empty two-dimensional list which has one column and one row less, than the original
        newList = [0 for row in range(len(self.matrix)-1)]
        for row in range(len(newList)):
            newList[row] = [0 for removedCol in range(len(self.matrix)-1)]
        #fill new matrixList, remove first row and removedCol column from original matrix 
        for row in range(1,len(self.matrix)):
            col = 0
            for col2 in range(len(self.matrix[0])):
                #skip the removed column
                if(col2==removedCol):
                    continue
                newList[row-1][col] = self.matrix[row][col2]
                col = col+1
        return Matrix(newList)
    #counts the determinant of the matrix
    def countDeterminant(self):
        #check that matrix is square matrix
        if (len(self.matrix) == len(self.matrix[0])):
            #special case, if matrix is 1x1
            if (len(self.matrix) == 1):
                return self.matrix[0][0]
            #special case, if matrix is 2x2
            elif(len(self.matrix) == 2):
                return self.matrix[0][0]*self.matrix[1][1]-self.matrix[1][0]*self.matrix[0][1]
            #solution for NxN matrixes
            #det(A) = Σ(-1)^(1+j)*a1j*det(A1j)
            determinant = 0
            for col in range(len(self.matrix)):
                newMatrix = self.generateList(col)
                determinant = determinant+pow(-1,(col+2))*self.matrix[0][col]*newMatrix.countDeterminant()
            return determinant
        return None    