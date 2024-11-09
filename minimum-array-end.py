class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
            You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

            Return the minimum possible value of nums[n - 1].
        """
        ans = x

        n -= 1  
        mask = 1

        while n > 0:
            if (mask & x) == 0:
                ans |= (n & 1) * mask
                n >>= 1
            mask <<= 1

        return ans
