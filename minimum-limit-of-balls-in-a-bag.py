class Solution:
    def minimumSize(self, nums, max_operations):
        """
            You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

            You can perform the following operation at most maxOperations times:

            Take any bag of balls and divide it into two new bags with a positive number of balls.
            For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
            Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

            Return the minimum possible penalty after performing the operations.
        """
        left = 1
        right = max(nums)

        while left < right:
            middle = (left + right) // 2

            if self._is_possible(middle, nums, max_operations):
                right = middle
            else:
                left = middle + 1

        return left

    def _is_possible(self, max_balls_in_bag, nums, max_operations):
        total_operations = 0

        for num in nums:
            operations = math.ceil(num / max_balls_in_bag) - 1
            total_operations += operations

            if total_operations > max_operations:
                return False

        return True
