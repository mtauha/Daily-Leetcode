class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        n, m = len(mat), len(mat[0])
        rows = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if j == 0:
                    rows[i][j] = mat[i][j]
                else:
                    print(i, j)
                    rows[i][j] = 0 if mat[i][j] == 0 else rows[i][j-1] + 1
                
                curr = rows[i][j]
                for k in range(i, -1, -1):
                    curr = min(curr, rows[k][j])
                    if curr == 0:
                        break
                    
                    ans += curr
        
        return ans

                
