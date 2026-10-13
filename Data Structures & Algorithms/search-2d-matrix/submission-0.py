class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows * columns

        while (left < right):
            center = int((left + right)/2)

            column = center%columns
            row = center // columns

            if(matrix[row][column] == target):
                return True

            elif(matrix[row][column] < target):
                left = center + 1

            else :
                right = center

        return False

