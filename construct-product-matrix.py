class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        rows, cols = len(grid), len(grid[0])
        ans = [[0]*cols for _ in range(rows)]

        suffix = 1
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                ans[row][col] = suffix
                suffix = (suffix * grid[row][col]) % MOD
        
        prefix = 1
        for row in range(rows):
            for col in range(cols):
                ans[row][col] = (ans[row][col] * prefix) % MOD
                prefix = (prefix * grid[row][col]) % MOD
        
        return ans
