class Solution:
    def minimumSubarrayLength(self, nums, k):
        """
            You are given an array nums of non-negative integers and an integer k.

            An array is called special if the bitwise OR of all of its elements is at least k.

            Return the length of the shortest special non-empty 
            subarray
            of nums, or return -1 if no special subarray exists.

        """
        def updateBits(count, num, val):
            for i in range(32):
                if num & (1 << i):
                    count[i] += val

        def getVal(count):
            ans = 0
            for i in range(32):
                if count[i] > 0:
                    ans |= (1 << i)
            return ans

        count = [0] * 32
        start = 0
        min_length = len(nums) + 1

        for end in range(len(nums)):
            updateBits(count, nums[end], 1)

            while start <= end and getVal(count) >= k:
                min_length = min(min_length, end - start + 1)
                updateBits(count, nums[start], -1)
                start += 1

        return -1 if min_length == len(nums) + 1 else min_length

        
