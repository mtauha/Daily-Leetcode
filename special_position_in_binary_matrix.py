class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        count = 0
        rows, columns = len(mat), len(mat[0])

        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 1:
                    if sum(mat[i]) == 1:
                        if sum(mat[k][j] for k in range(rows)) == 1:
                            count+=1

        return count


solution = Solution()
mat = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(solution.numSpecial(mat))
