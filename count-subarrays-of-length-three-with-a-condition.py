class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        n = len(nums)

        while left + 2 < n:
            if (nums[left] + nums[left + 2]) * 2 == nums[left+1]:
                ans += 1
            
            left += 1
        
        return ans
