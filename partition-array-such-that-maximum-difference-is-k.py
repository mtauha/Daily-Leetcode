class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        start = nums[0]

        for num in nums:
            if num - start > k:
                start = num
                ans += 1
        
        return ans
