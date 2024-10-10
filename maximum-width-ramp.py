class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
              A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
              Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
        """
        n = len(nums)
        indices = [i for i in range(n)]

        indices.sort(key=lambda i: (nums[i], i))

        min_index = n
        max_width = 0

        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)

        return max_width
