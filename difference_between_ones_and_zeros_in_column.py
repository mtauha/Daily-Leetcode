class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        rows, columns = len(grid), len(grid[0])
        onesRow, onesCol, zerosRow, zerosCol = (
            [0] * rows,
            [0] * columns,
            [0] * rows,
            [0] * columns,
        )
        diff = [[0] * columns for _ in range(rows)]

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                    onesRow[row] += 1
                    onesCol[col] += 1
                else:
                    zerosRow[row] += 1
                    zerosCol[col] += 1

        for row in range(rows):
            for col in range(columns):
                diff[row][col] = (
                    onesRow[row] + onesCol[col] - zerosRow[row] - zerosCol[col]
                )

        print(diff)

        return diff


solution = Solution()

solution.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]])
