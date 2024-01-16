class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        
        self.prefix = [[0] * cols for i in range(rows)]
        self.prefix[0][0] =matrix[0][0] 
        for i in range(1,cols):
            self.prefix[0][i]=self.prefix[0][i-1]+matrix[0][i]
        for r in range(1,rows):
            for c in range(cols):
                self.prefix[r][c]=self.prefix[r-1][c]+matrix[r][c]
                if c>0:
                    self.prefix[r][c]+=self.prefix[r][c-1]-self.prefix[r-1][c-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        first=self.prefix[row2][col2]
        second=0
        third=0
        fourth=0
        if col1>0:
            second=self.prefix[row2][col1-1]
        if row1>0:
            third=self.prefix[row1-1][col2]
        if col1>0 and row1>0:
            fourth=self.prefix[row1-1][col1-1]
        return first-second-third+fourth


        
    


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)