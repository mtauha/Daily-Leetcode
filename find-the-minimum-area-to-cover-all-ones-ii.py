class Solution:

    def minimumSum(self, grid: List[List[int]]) -> int:
        @cache
        def helper(start_x, end_x, start_y, end_y):
            min_i, min_j = float("inf"), float("inf")
            max_i, max_j = -float("inf"), -float("inf")
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    if grid[i][j] == 1:
                        min_i, min_j = min(min_i, i), min(min_j, j)
                        max_i, max_j = max(max_i, i), max(max_j, j)
            return (max_i - min_i + 1) * (max_j - min_j + 1)

        m = len(grid)
        n = len(grid[0])
        res = 10000
        for i in range(m - 1):
            for j in range(i + 1, m - 1):
                res = min(
                    helper(0, i, 0, n - 1)
                    + helper(i + 1, j, 0, n - 1)
                    + helper(j + 1, m - 1, 0, n - 1),
                    res,
                )

        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                res = min(
                    helper(0, m - 1, 0, i)
                    + helper(0, m - 1, i + 1, j)
                    + helper(0, m - 1, j + 1, n - 1),
                    res,
                )

        for i in range(m - 1):
            for j in range(n - 1):
                res = min(
                    helper(0, i, 0, n - 1)
                    + helper(i + 1, m - 1, 0, j)
                    + helper(i + 1, m - 1, j + 1, n - 1),
                    res,
                )
                res = min(
                    helper(0, m - 1, 0, j)
                    + helper(0, i, j + 1, n - 1)
                    + helper(i + 1, m - 1, j + 1, n - 1),
                    res,
                )
                res = min(
                    helper(0, i, 0, j)
                    + helper(0, i, j + 1, n - 1)
                    + helper(i + 1, m - 1, 0, n - 1),
                    res,
                )
                res = min(
                    helper(0, i, 0, j)
                    + helper(i + 1, m - 1, 0, j)
                    + helper(0, m - 1, j + 1, n - 1),
                    res,
                )
        return res
