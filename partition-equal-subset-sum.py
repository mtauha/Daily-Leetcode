class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)

        if summ % 2 != 0:
            return False
        
        target = summ // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for currSum in range(target, num - 1, -1):
                dp[currSum] |= dp[currSum - num]
        
        return dp[target]
