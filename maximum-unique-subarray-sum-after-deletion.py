class Solution:
    def maxSum(self, nums: List[int]) -> int:
        Set = set([num for num in nums if num > 0])
        
        if len(Set) == 0:
            return max(nums)
        else:
            return sum(Set)
