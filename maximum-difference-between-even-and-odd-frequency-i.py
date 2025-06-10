class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        even, odd = [], []

        for k, v in counts.items():
            if v % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        
        return max(odd) - min(even)
