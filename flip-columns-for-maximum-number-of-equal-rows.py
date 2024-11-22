class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
            You are given an m x n binary matrix matrix.

            You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

            Return the maximum number of rows that have all values equal after some number of flips.
        """
        num_cols = len(matrix[0])
        ans = 0

        for row in matrix:
            flipped = [1-x for x in row]
            identical = sum(
                1 for compare in matrix if compare == row or compare == flipped
            )

            ans = max(ans, identical)
        
        return ans
