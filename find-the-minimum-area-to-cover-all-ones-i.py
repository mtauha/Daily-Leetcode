class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        first_col, first_row = m, n
        last_col, last_row = 0, 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                        first_row, first_col = min(first_row, i), min(first_col, j)
                        last_row, last_col = max(last_row, i), max(last_col, j)

        
        return (last_row - first_row + 1) * (last_col - first_col + 1)
