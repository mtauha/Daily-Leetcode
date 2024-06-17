"""Description:
    Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
"""

from math import isqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if isqrt(c) ** 2 == c:
            return True

        for a in range(int(isqrt(c)) + 1):
            b_squared = c - a**2
            if b_squared < 0:
                continue
            b = int(isqrt(b_squared))
            if b**2 == b_squared:
                return True

        return False


sol = Solution()
c = 3
print(sol.judgeSquareSum(c))
