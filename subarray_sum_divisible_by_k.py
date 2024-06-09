"""Description:
    Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

    A subarray is a contiguous part of an array.
"""

class Solution:

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_sums = {
            0: 1
        }  

        for num in nums:
            prefix_sum += num
            modulo = prefix_sum % k
            if (
                modulo < 0
            ):  
                modulo += k

            if modulo in prefix_sums:
                count += prefix_sums[modulo]

            if modulo not in prefix_sums:
                prefix_sums[modulo] = 0
            prefix_sums[modulo] += 1

        return count


sol = Solution()
nums = [4, 5, 0, -2, -3, 1]
k = 5
print(sol.subarraysDivByK(nums, k))
