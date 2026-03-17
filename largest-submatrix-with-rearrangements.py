class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if row == 0:
                    break
                if matrix[row][col] != 0:
                    # Add uppermost value in the same column
                    matrix[row][col] += matrix[row-1][col]

            curr_row = sorted(matrix[row], reverse=True)
            for col in range(cols):
                # Get the maximum Area by multiplying height with width
                # curr_row[col] is the height we got by running prev for loop
                # col + 1 is the width of the rectangle
                ans = max(ans, curr_row[col] * (col + 1))
        
        return ans
