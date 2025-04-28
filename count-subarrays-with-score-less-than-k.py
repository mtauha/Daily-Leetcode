class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total, count = 0, 0
        left = 0

        for right in range(n):
            total += nums[right]
            # Loop until left reaches right && len of this sub array * sum of that subarray is less than k
            while left <= right and (right - left + 1) * total >= k:
                total -= nums[left]
                left += 1
            
            count += right - left + 1

        return count
