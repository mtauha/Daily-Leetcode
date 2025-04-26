class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        pos_min = pos_max = bad = -1
        ans = 0

        for idx, num in enumerate(nums):
            if num == minK:
                pos_min = idx
            if num == maxK:
                pos_max = idx
            if num < minK or num > maxK:
                bad = idx
            if pos_min != -1 and pos_max != -1:
                ans += max(0, min(pos_min, pos_max) - bad)
        
        return ans
