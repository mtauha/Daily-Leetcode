"""Description:
    Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

    A good subarray is a subarray where:

    its length is at least two, and
    the sum of the elements of the subarray is a multiple of k.
    Note that:

    A subarray is a contiguous part of the array.
    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix_sums = {0: -1}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            if k != 0:
                current_sum = current_sum % k

            if current_sum in prefix_sums:
                if i - prefix_sums[current_sum] > 1:
                    print(i, current_sum, prefix_sums[current_sum])
                    return True
            else:
                prefix_sums[current_sum] = i

        return False


sol = Solution()
nums = [23, 2, 6, 4, 7]
k = 6
print(sol.checkSubarraySum(nums, k))
