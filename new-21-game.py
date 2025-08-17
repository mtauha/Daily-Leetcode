class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or (n > k + maxPts - 1):
            return 1.0
        
        prob = [0.0]*(n + 1)
        prob[0] = 1.0
        w = 1.0
        ans = 0.0

        for i in range(1, n + 1):
            prob[i] = w/maxPts
            if i < k:
                w += prob[i]
            else:
                ans += prob[i]
            if i - maxPts >= 0 and i - maxPts < k:
                w -= prob[i - maxPts]
        
        return ans
