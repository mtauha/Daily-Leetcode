class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols - 1, -1, -1):
                if grid[row][col] >= 0:
                    break
                ans += 1
        
        return ans
