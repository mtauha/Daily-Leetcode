class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        """
            An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

            You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
            subarray
            nums[fromi..toi] is special or not.

            Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.
        """
        ans = [False] * len(queries)
        prefix = [0] * len(nums)
        prefix[0] = 0

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            ans[i] = prefix[end] - prefix[start] == 0

        return ans
