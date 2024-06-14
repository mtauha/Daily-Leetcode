"""Description:
    You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

    Return the minimum number of moves to make every value in nums unique.

    The test cases are generated so that the answer fits in a 32-bit integer.
"""

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        moves = 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] - nums[i] + 1
                nums[i] += increment
                moves += increment


        return moves


sol = Solution()
nums = [2, 1, 1, 1]
print(sol.minIncrementForUnique(nums))
