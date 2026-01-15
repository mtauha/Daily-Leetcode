class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # We'll be finding the smallest consecutive length of one side that can
        # be formed in order to maximize the Area of rectangle

        hBars.sort()
        vBars.sort()
        h_max, v_max = 1, 1
        h_cur, v_cur = 1, 1

        # Maximum Consecutive length by removing horizontal bars
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                h_cur += 1
            else:
                h_cur = 1
            h_max = max(h_max, h_cur)
        
        # Maximum Consecutive length by removing vertical bars
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                v_cur += 1
            else:
                v_cur = 1
            v_max = max(v_max, v_cur)
        
        # Length to make a square
        return (min(h_max, v_max) + 1)**2
