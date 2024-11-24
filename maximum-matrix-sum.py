class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
            You are given an n x n integer matrix. You can do the following operation any number of times:

            Choose any two adjacent elements of matrix and multiply each of them by -1.
            Two elements are considered adjacent if and only if they share a border.

            Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
        """
        total_sum = 0
        min_abs_val = float("inf")
        negative_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(val))

        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_val

        return total_sum
