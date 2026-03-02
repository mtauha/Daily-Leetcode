class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = list(map(lambda r: (r[::-1] + [1]).index(1), grid))

        swaps = 0

        # Pattern to check number of required positions in each row:
        # (n - i - 1)

        for i in range(n):
            req = n - i - 1
            j = (zeros + [n]).index(next(filter(lambda v: v >= req, zeros + [n])))
            if j == len(zeros):
                return -1
            
            swaps += j
            zeros.pop(j)
        
        return swaps
