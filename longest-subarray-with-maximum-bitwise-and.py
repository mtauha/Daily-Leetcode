class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
            You are given an integer array nums of size n.
            Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
            In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
            Return the length of the longest such subarray.
            The bitwise AND of an array is the bitwise AND of all the numbers in it.
            A subarray is a contiguous sequence of elements within an array.
        """
      
        max_val = ans = current_streak = 0

        for num in nums:
            if max_val < num:
                max_val = num
                ans = current_streak = 0

            if max_val == num:
                current_streak += 1
            else:
                current_streak = 0
            
            ans = max(ans, current_streak)

        return ans

    def longestSubarrayOptimized(self, nums: List[int]) -> int:
        max_element = max(nums)

        ans = 0
        count = 0

        for ptr2 in range(len(nums)):
            if nums[ptr2] == max_element:
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        ans = max(ans, count)      
        return ans
        


