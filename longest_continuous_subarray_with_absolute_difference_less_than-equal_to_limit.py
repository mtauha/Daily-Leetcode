"""Description:
    Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
"""

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        left, right = 0, 0
        max_length = 0
        max_val, min_val = nums[0], nums[0]

        while right < len(nums):
            max_val = max(max_val, nums[right])
            min_val = min(min_val, nums[right])

            if max_val - min_val <= limit:
                max_length = max(max_length, right - left + 1)
            else:
                left += 1
                max_val = max(nums[left : right + 1])
                min_val = min(nums[left : right + 1])

            right += 1

        return max_length
