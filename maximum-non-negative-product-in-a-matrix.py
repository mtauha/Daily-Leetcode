class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows = len(grid)
        cols = len(grid[0])

        min_dp = [[0]*cols for _ in range(rows)]
        max_dp = [[0]*cols for _ in range(rows)]

        min_dp[0][0] = max_dp[0][0] = grid[0][0]

        for col in range(1, cols):
            max_dp[0][col] = max_dp[0][col-1] * grid[0][col]
            min_dp[0][col] = min_dp[0][col-1] * grid[0][col]
        
        for row in range(1, rows):
            max_dp[row][0] = max_dp[row-1][0] * grid[row][0]
            min_dp[row][0] = max_dp[row-1][0] * grid[row][0]

        for row in range(1, rows):
            for col in range(1, cols):
                curr = grid[row][col]

                max_top = max_dp[row-1][col]
                min_top = min_dp[row-1][col]

                max_left = max_dp[row][col-1]
                min_left = min_dp[row][col-1]

                candidates = [max_top * curr, min_top * curr, max_left * curr, min_left * curr]
                max_val = max(candidates)
                min_val = min(candidates)

                max_dp[row][col] = max_val
                min_dp[row][col] = min_val

        return max_dp[-1][-1] % MOD if max_dp[-1][-1] >= 0 else -1
