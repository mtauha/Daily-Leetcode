"""Description:
    An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

    Given the grid grid represented as a string array, return the number of regions.

    Note that backslash characters are escaped, so a '\' is represented as '\\'.
"""

from collections import deque

class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        # Each cell is represented as a 2x2 grid (thus 4 triangles per cell)
        size = n * 3  # Expanded grid size (n * 3 x n * 3)

        # Create the expanded grid
        expanded_grid = [[0] * size for _ in range(size)]
        
        # Mark the slashes on the expanded grid
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded_grid[i * 3][j * 3 + 2] = 1  # Top-right triangle
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1  # Center
                    expanded_grid[i * 3 + 2][j * 3] = 1  # Bottom-left triangle
                elif grid[i][j] == '\\':
                    expanded_grid[i * 3][j * 3] = 1  # Top-left triangle
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1  # Center
                    expanded_grid[i * 3 + 2][j * 3 + 2] = 1  # Bottom-right triangle

        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                x, y = queue.popleft()
                if x < 0 or y < 0 or x >= size or y >= size or expanded_grid[x][y] == 1:
                    continue
                expanded_grid[x][y] = 1  # Mark visited
                # Add all 4 possible directions
                queue.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

        # Count the regions using BFS
        regions = 0
        for i in range(size):
            for j in range(size):
                if expanded_grid[i][j] == 0:  # Found an unvisited region
                    bfs(i, j)  # Flood fill using BFS
                    regions += 1  # Increment the region count

        return regions

sol = Solution()
