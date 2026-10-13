class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.summat = [[0]*(cols+1)for _ in range(rows+1)]

        for r in range(1,rows+1):
            for c in range(1,cols+1):
                self.summat[r][c] = matrix[r-1][c-1] + self.summat[r-1][c] + self.summat[r][c-1] - self.summat[r - 1][c - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.summat[row1][col1]
        above = self.summat[row1][col2+1]
        org = self.summat[row2+1][col2+1]
        left_low = self.summat[row2+1][col1]

        return org - above - left_low + left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)