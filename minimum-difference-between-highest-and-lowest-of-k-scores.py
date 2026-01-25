class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        print(n)
        nums.sort(reverse=True)
        ans = (10**5) + 1

        if n == k:
            return nums[0] - nums[-1]

        for i in range(n - k + 1):
            ans = min(ans, nums[i] - nums[i + k - 1])
        
        return ans
