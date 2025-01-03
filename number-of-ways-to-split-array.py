class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        """
            You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

            The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
            There is at least one element to the right of i. That is, 0 <= i < n - 1.
            Return the number of valid splits in nums.
        """
        # Keep track of sum of elements on left and right sides
        left_sum = right_sum = 0

        # Initially all elements are on right side
        right_sum = sum(nums)

        # Try each possible split position
        count = 0
        for i in range(len(nums) - 1):
            # Move current element from right to left side
            left_sum += nums[i]
            right_sum -= nums[i]

            # Check if this creates a valid split
            if left_sum >= right_sum:
                count += 1

        return count
