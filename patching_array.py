"""Description:
    Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

    Return the minimum number of patches required.
"""

class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        element = 1
        patches = 0
        i = 0

        while element <= n:
            if i < len(nums) and nums[i] <= element:
                element += nums[i]
                i += 1
            else:
                element += element
                patches += 1

        return patches
