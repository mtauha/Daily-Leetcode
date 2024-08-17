

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
      """Description:
          You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
          To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
          However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
          Return the maximum number of points you can achieve.
          
          abs(x) is defined as:
          x for x >= 0.
          -x for x < 0.
      """
        cols = len(points[0])
        current_row = [0]*cols
        prev_row = [0] * cols

        for row in points:
            local_max = 0

            for col in range(cols):
                local_max = max(local_max - 1, prev_row[col])
                current_row[col] = local_max

            local_max = 0
            for col in range(cols-1, -1, -1):
                local_max = max(local_max - 1, prev_row[col])
                current_row[col] = max(current_row[col], local_max) + row[col]           

            prev_row = current_row.copy()

        return max(prev_row)
