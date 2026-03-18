class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])

        dp = [0] * cols

        for row in range(rows):
            curr_sum = 0
            for col in range(cols):
                dp[col] += grid[row][col]
                curr_sum += dp[col]
                if curr_sum <= k:
                    ans += 1
        
        return ans
        
