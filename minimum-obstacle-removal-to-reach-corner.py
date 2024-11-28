class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
            You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

            0 represents an empty cell,
            1 represents an obstacle that may be removed.
            You can move up, down, left, or right from and to an empty cell.

            Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
        """
        row, col = len(grid), len(grid[0])

        obstacle = [[float("inf")] * col for _ in range(row)]

        q = deque([(0, 0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        obstacle[0][0] = 0

        while q:
            obs, x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue

                if obstacle[nx][ny] == float("inf"):
                    if grid[nx][ny] == 1:
                        obstacle[nx][ny] = obs + 1
                        q.append((obs + 1, nx, ny))
                    else:
                        obstacle[nx][ny] = obs
                        q.appendleft((obs, nx, ny))

        return obstacle[row - 1][col - 1]
