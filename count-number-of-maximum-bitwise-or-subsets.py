class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
          Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
          An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
          The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
        """
        max_or_value = 0
        dp = [0] * (1 << 17)

        dp[0] = 1

        for num in nums:
            for i in range(max_or_value, -1, -1):
                dp[i | num] += dp[i]

            max_or_value |= num

        return dp[max_or_value]

    def countMaxOrSubsets2(self, nums: List[int]) -> int:
        maxOR = 0

        for num in nums:
            maxOR |= num
        
        n = len(nums)
        totalSubsets = 1 << n
        subsetsWithMaxOR = 0

        for mask in range(totalSubsets):
            currentOr = 0

            for i in range(n):
                if (mask >> i) & 1:
                    currentOr |= nums[i]
                
            if currentOr == maxOR:
                subsetsWithMaxOR += 1
        
        return subsetsWithMaxOR
