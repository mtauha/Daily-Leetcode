"""Description:
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque([(r, c)])

            while queue:
                row, col = queue.popleft()

                if (
                    row < 0
                    or col < 0
                    or row >= rows
                    or col >= cols
                    or grid[row][col] == "0"
                ):
                    continue

                grid[row][col] = "0"

                queue.append((row + 1, col))
                queue.append((row - 1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))

        no_of_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    no_of_islands += 1
                    bfs(r, c)

        return no_of_islands


sol = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(sol.numIslands(grid))
