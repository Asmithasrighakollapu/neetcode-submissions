class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        col=len(matrix[0])
        for i in range(rows):
            for j in range(col):
                if matrix[i][j]==target:
                    return True
        return False
        