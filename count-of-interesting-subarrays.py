class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        dp = defaultdict(int)
        dp[0] = 1
        prefix = 0
        n = len(nums)

        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            ans += dp[(prefix - k + modulo) % modulo]
            dp[prefix % modulo] += 1
        
        return ans
