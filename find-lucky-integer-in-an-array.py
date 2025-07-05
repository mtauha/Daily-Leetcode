class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        ans = -1

        for n in arr:
            counts[n] += 1

        for n, c in counts.items():
            if n == c:
                ans = max(ans, n)
        
        return ans
        
