class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
            You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

            A stone '#'
            A stationary obstacle '*'
            Empty '.'
            The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

            It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

            Return an n x m matrix representing the box after the rotation described above.
        """
        m = len(box)
        n = len(box[0])
        result = [["" for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                result[i][j] = box[j][i]

        for i in range(n):
            result[i].reverse()

        for j in range(m):
            lowest_row_with_empty_cell = n - 1
            for i in range(n - 1, -1, -1):
                if result[i][j] == "#":
                    result[i][j] = "."
                    result[lowest_row_with_empty_cell][j] = "#"
                    lowest_row_with_empty_cell -= 1
                if result[i][j] == "*":
                    lowest_row_with_empty_cell = i - 1

        return result
