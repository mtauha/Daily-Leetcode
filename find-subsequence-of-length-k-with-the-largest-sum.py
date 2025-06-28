class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        values = [[i, nums[i]] for i in range(n)]
        values.sort(key=lambda x: -x[1])

        values = sorted(values[:k])
        ans = [value for idx, value in values]
        return ans
