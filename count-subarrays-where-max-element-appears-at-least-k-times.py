class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        freq = 0
        left = 0
        n = len(nums)
        maxx = max(nums)
        ans = 0

        for right in range(n):
            if nums[right] == maxx:
                freq += 1
            
            while freq >= k:
                # All the subarrays starting from left to right are valid. So,
                ans += n - right
                if nums[left] == maxx:
                    freq -= 1
                
                left += 1
        
        return ans
            
