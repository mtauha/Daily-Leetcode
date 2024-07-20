"""Description:
    You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

    Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

    Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

"""


class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        rows = len(rowSum)
        cols = len(colSum)

        matrix = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            matrix[row][0] = rowSum[row]

        for col in range(cols):
            current_col_sum = 0
            for row in range(rows):
                current_col_sum += matrix[row][col]

            row = 0
            while current_col_sum > colSum[col]:
                diff = current_col_sum - colSum[col]

                shift = min(matrix[row][col], diff)
                matrix[row][col] -= shift
                matrix[row][col + 1] += shift

                current_col_sum -= shift

                row += 1

        return matrix


sol = Solution()
