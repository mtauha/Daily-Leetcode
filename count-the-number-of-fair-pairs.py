class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
            Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

            A pair (i, j) is fair if:

            0 <= i < j < n, and
            lower <= nums[i] + nums[j] <= upper
        """
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                result += right - left
                left += 1
            else:
                right -= 1
        return result
