class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
            Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
        """
        curr = 1
        k -= 1
        def countSteps(n, prefix1, prefix2):
            steps = 0
            while prefix1 <= n:
                steps += min(n+1, prefix2) - prefix1
                prefix1 *= 10
                prefix2 *= 10
            
            return steps

        while k > 0:
            steps = countSteps(n, curr, curr+1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
            
        
        return curr
