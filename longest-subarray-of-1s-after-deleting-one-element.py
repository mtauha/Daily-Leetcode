class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        ptr1 = 0
        n = len(nums)
        count = 0

        for ptr2 in range(n):
            if nums[ptr2] == 0:
                count += 1

            while count > 1:
                if nums[ptr1] == 0:
                    count -= 1
                ptr1 += 1
            
            ans = max(ans , ptr2 - ptr1)
        return ans
