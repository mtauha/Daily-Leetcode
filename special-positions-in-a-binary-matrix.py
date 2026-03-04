class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check_col(col: int):
            return sum(row[col] for row in mat) == 1

        ans = 0

        for row in mat:
            if sum(row) == 1:
                col = row.index(1)
                ans += check_col(col)
        
        return ans
