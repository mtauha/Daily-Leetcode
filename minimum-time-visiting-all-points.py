class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        curr = points[0]
        for i in range(1, len(points)):
            ans += max(abs(curr[0] - points[i][0]), abs(curr[1] - points[i][1]))
            curr = points[i]
        
        return ans
