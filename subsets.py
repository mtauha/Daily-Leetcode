"""
Description:
    Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        x = len(nums)

        for i in range(1 << x):
            result.append([nums[j] for j in range(x) if (i & (1 << j))])

        return result
