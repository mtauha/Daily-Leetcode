class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        def diagonal(length, width):
            return math.sqrt(length**2 + width**2)
        ans = 0
        max_diag = 0

        for length, width in dimensions:
            curr_diag = diagonal(length, width)
            if curr_diag > max_diag:
                max_diag = curr_diag
                ans = length * width
            elif curr_diag == max_diag:
                ans = max(ans, length * width)
        
        return ans
