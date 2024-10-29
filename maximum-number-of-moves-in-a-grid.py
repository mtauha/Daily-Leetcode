class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """
            You are given a 0-indexed m x n matrix grid consisting of positive integers.

            You can start at any cell in the first column of the matrix, and traverse the grid in the following way:
            
            From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
            Return the maximum number of moves that you can perform.
        """
        M, N = len(grid), len(grid[0])

        # Create a dp array to store moves, with each cell having a size of 2.
        dp = [[0] * 2 for _ in range(M)]

        # Initialize the first column cells as reachable.
        for i in range(M):
            dp[i][0] = 1

        max_moves = 0

        # Iterate over each column starting from the second one.
        for j in range(1, N):
            for i in range(M):
                # Check if moving from the same row of the previous column is possible.
                if grid[i][j] > grid[i][j - 1] and dp[i][0] > 0:
                    dp[i][1] = max(dp[i][1], dp[i][0] + 1)

                # Check if moving from the upper diagonal is possible.
                if (
                    i - 1 >= 0
                    and grid[i][j] > grid[i - 1][j - 1]
                    and dp[i - 1][0] > 0
                ):
                    dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)

                # Check if moving from the lower diagonal is possible.
                if (
                    i + 1 < M
                    and grid[i][j] > grid[i + 1][j - 1]
                    and dp[i + 1][0] > 0
                ):
                    dp[i][1] = max(dp[i][1], dp[i + 1][0] + 1)

                # Update the maximum moves so far.
                max_moves = max(max_moves, dp[i][1] - 1)

            # Shift dp values for the next iteration.
            for k in range(M):
                dp[k][0] = dp[k][1]
                dp[k][1] = 0

        return max_moves
