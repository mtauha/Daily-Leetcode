class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
            Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
        """
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*(col+1) for _ in range(row+1)]
        ans = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i+1][j+1] = (
                        min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    )
                    ans += dp[i+1][j+1]
        
        return ans

    def countSquares2(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0]*cols for _ in range(rows)]
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    ans += dp[i][j]
        
        return ans
