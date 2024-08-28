class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
            You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
            An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
            Return the number of islands in grid2 that are considered sub-islands.
        """
        rows, cols = len(grid1), len(grid1[0])

        def bfs(row, col):
            queue = deque([(row, col)])
            is_sub_island = True
            
            while queue:
                r, c = queue.popleft()
                
                if (
                    r < 0
                    or c < 0
                    or r >= rows
                    or c >= cols
                    or grid2[r][c] == 0
                ):
                    continue
                
                if grid1[r][c] == 0:
                    is_sub_island = False
                
                grid2[r][c] = 0

                queue.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
            
            return is_sub_island
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    if bfs(row, col):
                        count += 1
        
        return count
