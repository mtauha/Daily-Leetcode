class Solution:
    def maxAdjacentDistance1(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(nums[0])

        return max([abs(nums[i] - nums[i+1]) for i in range(n)])

    def maxAdjacentDistance2(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            ans = max(ans, abs(nums[i % n] - nums[(i+1) % n]))

        return ans
        
