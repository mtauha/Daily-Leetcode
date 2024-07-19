"""Description:
    Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
"""

from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minimum = {min(i) for i in matrix}
        maximum = {max(i) for i in zip(*matrix)}

        return list(minimum&maximum)


sol = Solution()

matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
print(sol.luckyNumbers(matrix))
