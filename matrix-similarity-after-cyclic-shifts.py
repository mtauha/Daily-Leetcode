class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])
        shift = (k % cols)

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] != mat[row][(col + shift) % cols]:
                    return False
        
        return True
