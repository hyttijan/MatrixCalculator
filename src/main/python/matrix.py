class Matrix:
    
    def __init__(self, matrix):
        self.matrix = matrix
     
    # Inits empty two-dimensional list
    def initEmptyMatrixList(self,rows,columns):
        matrixList = [0 for row in range(rows)]
        for row in range(rows):
            matrixList[row] = [0 for column in range(columns)]
        return matrixList;
  
    # Swaps two rows in matrix
    def changeRows(self, row1, row2):
        tempRow = self.matrix[row1][:]
        self.matrix[row1] = self.matrix[row2]
        self.matrix[row2] = tempRow
        
    # Multiplies one row in matrix with multiplier
    def multiplyRow(self, multiplier, row):
        for column in range(len(self.matrix[row])):
            self.matrix[row][column] = self.matrix[row][column]*multiplier
            
    # Adds one row to another with multiplier
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
        
    # Multiplies matrix with another matrix
    def matrixMultiplication(self, secondMatrix):
        # Check that matrixes can be multiplied
        # First matrixes column count must equal second matrixe's row count
        if (len(self.matrix[0]) == len(secondMatrix.matrix)):
            # Init empty two-dimensional matrixList for new matrix
            matrixList = self.initEmptyMatrixList(len(self.matrix),len(secondMatrix.matrix[0]))
            # Count the new matrix
            for row in range(len(matrixList)):
                for column in range(len(matrixList[0])):
                    for k in range(len(self.matrix[0])):
                        matrixList[row][column] = (matrixList[row][column]
                                                   + self.matrix[row][k]
                                                   * secondMatrix.matrix[k][column])
            return Matrix(matrixList)
        # If matrixes cannot be multiplied return None
        return None
    
    # Multiplies matrix with scalar
    def scalarMultiplication(self, scalar):
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                # Multiplies each row and column with scalar
                self.matrix[row][column] = scalar*self.matrix[row][column]
    
    # Performs Gauss-Jordan elimination for the matrix
    def gaussJordanElimination(self):
        self.echelonForm()
        self.reducedEchelonForm()
        
    # Forms echelon form from the matrix
    def echelonForm(self):
        column = 0
        for row in range(len(self.matrix)):
            self.pushZeroRowsDown(row,column)
            if (self.matrix[row][column] != 0):
                self.decrementToZero(column)
                # If there are more columns than rows
                # Cannot increment column index
                # Last rows will be zero rows
                if (column < len(self.matrix[0])-1):
                    column = column+1
                    
    # Forms reduced echelon form from echelon form matrix
    def reducedEchelonForm(self):
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])-1):
                # Leave alone if value in current entry is already 1 or 0
                if (self.matrix[row][column] != 1 and self.matrix[row][column] != 0):
                    # Otherwise count the multiplier so that the leading coefficient is 1
                    multiplier = 1/self.matrix[row][column]
                    # Apply the multiplier to all the other entries on the current row
                    self.multiplyRow(multiplier,row)
                    break
                
    # Decrements all the elements in rows in this column to zero except the one where row's index equals column's index
    def decrementToZero(self, column):   
        for row in range(len(self.matrix)):
            if (row != column):
                multiplier = self.matrix[row][column]/self.matrix[column][column]
                if (multiplier != 0):
                    multiplier = -multiplier
                self.addRowToAnother(column, row, multiplier)
                
    # Pushes all the rows with zeros in the current column down
    def pushZeroRowsDown(self, row, column):
        # Start pushing down rows from current row
        for row2 in range(row,len(self.matrix)-1):
            # If row has zero column in current column check for non-zero rows from bottom to up
            if (self.matrix[row2][column] == 0):
                for row3 in range(len(self.matrix)-1,row2,-1):
                    if (self.matrix[row3][column] != 0):
                        self.changeRows(row3, row2)
                        break
    
    # Forms transpose of matrix
    def transpose(self):
        matrixList = self.initEmptyMatrixList(len(self.matrix[0]),len(self.matrix))
        for row in range(len(matrixList)):
            for column in range(len(matrixList[0])):
                matrixList[row][column] = self.matrix[column][row]
        return Matrix(matrixList)
    
    # Forms inverse matrix
    def invertMatrix(self):
        # Check that matrix is square matrix
        if (len(self.matrix) == len(self.matrix[0])):
            identityMatrix = self.formIdentityMatrix()
            attachedMatrices = self.attachMatrices(identityMatrix)
            attachedMatrices.gaussJordanElimination()
            if(attachedMatrices.isIdentityMatrix()):
                invertedMatrix = attachedMatrices.separateMatrices()
                return invertedMatrix
            else:
                return None
            
    # Forms Identity matrix      
    def formIdentityMatrix(self):
        # Check that matrix is square matrix
        if(len(self.matrix)==len(self.matrix[0])):
            matrixList = self.initEmptyMatrixList(len(self.matrix),len(self.matrix[0]))
            # Form identity matrix list
            for row in range(len(matrixList)):
                for column in range(row,len(matrixList[0])):
                    matrixList[row][column] = 1
                    break
            return Matrix(matrixList);
        else:
            return None
    
    # Checks if matrix is identity matrix
    def isIdentityMatrix(self):
        for row in range(len(self.matrix)):
            if(self.matrix[row][row] != 1):
                return False
        return True
    
    # Separates help matrix from matrix
    def separateMatrices(self):
        matrixList = self.initEmptyMatrixList(len(self.matrix),1)
        for row in range(len(self.matrix)):
            matrixList[row] = self.matrix[row][int(len(self.matrix[0])/2):]
        return Matrix(matrixList)
    
    # Attaches help matrix to matrix
    def attachMatrices(self,anotherMatrix):
        matrixList = self.initEmptyMatrixList(len(self.matrix),1)
        for row in range(len(self.matrix)):
            matrixList[row] = self.matrix[row]+anotherMatrix.matrix[row]
        return Matrix(matrixList)
    
    # Counts the determinant of the matrix
    def countDeterminant(self):
        # Check that matrix is square matrix
        if (len(self.matrix) == len(self.matrix[0])):
            # Special case, if matrix is 1x1
            if (len(self.matrix) == 1):
                return self.matrix[0][0]
            # Special case, if matrix is 2x2
            elif (len(self.matrix) == 2):
                return (self.matrix[0][0]*self.matrix[1][1] 
                        - self.matrix[1][0]*self.matrix[0][1])
            # Solution for NxN matrixes
            else:
                return self.detForNxNmatrix()
        return None    
    
    def detForNxNmatrix(self):
        determinant = 0
        # Det(A) = Σ(-1)^(1+j)*a1j*Det(A1j)
        for col in range(len(self.matrix)):
            newMatrix = self.generateList(col)
            determinant = (determinant 
                            + pow(-1,(col+2)) 
                            * self.matrix[0][col] 
                            * newMatrix.countDeterminant())
        return determinant
    
    def generateList(self,removedCol):
        # Init empty two-dimensional list which has one column and one row less, than the original
        newList = self.initEmptyMatrixList(len(self.matrix)-1,len(self.matrix[0])-1) 
        # Fill new matrixList, remove first row and removedCol column from original matrix 
        for row in range(1,len(self.matrix)):
            col = 0
            for col2 in range(len(self.matrix[0])):
                # Skip the removed column
                if(col2==removedCol):
                    continue
                newList[row-1][col] = self.matrix[row][col2]
                col = col+1
        return Matrix(newList)
    
    