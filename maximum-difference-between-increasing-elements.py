class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx = -1
        n = len(nums)
        last = nums[n - 1]

        for i in range(n - 2, -1, -1):
            if nums[i] >= last:
                last = nums[i]
            else:
                maxx = max(maxx, last - nums[i])        
        
        return maxx
