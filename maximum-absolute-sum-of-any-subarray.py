class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefixSum = 0
        minPrefix, maxPrefix = 0, 0

        for num in nums:
            prefixSum += num

            minPrefix = min(minPrefix, prefixSum)
            maxPrefix = max(maxPrefix, prefixSum)
        
        return maxPrefix - minPrefix
