class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)

        points.sort(key=lambda x: (-x[0], x[1]))

        for i in range(n - 1):
            y = float("inf")
            for j in range(i + 1, n):
                point_a, point_b = points[i], points[j]

                if y > point_b[1] >= point_a[1]:
                    ans += 1
                    y = point_b[1]
        
        return ans
