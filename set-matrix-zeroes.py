class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        indices = []

        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    indices.append((row, col))
        
        for row, col in indices:
            matrix[row] = [0] * m
            for i in range(n):
                matrix[i][col] = 0
