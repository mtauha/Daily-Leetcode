class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        summ = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j or i == len(mat) - j - 1:
                    summ += mat[i][j]

        return summ


sol = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sol.diagonalSum(mat))
