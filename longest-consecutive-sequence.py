class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        nums = sorted(list(set(nums)))
        ans = 1
        ptr1 = 0

        for ptr2 in range(1, len(nums)):
            if nums[ptr2] != nums[ptr2 - 1] + 1:
                while ptr1 < ptr2:
                    ptr1 += 1
            
            ans = max(ans, ptr2 - ptr1 + 1)
        
        return ans
