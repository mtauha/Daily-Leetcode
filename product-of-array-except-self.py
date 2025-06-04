class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            We will solve it using prefix and suffix multiplication
            prefix: Number storing products of all numbers behind current index
            suffix: Number storing products of all numbers ahead of current index

            result: Array storing product of all numbers except number at current index by multiplying prefix and suffix at the current index.
        """

        n = len(nums)
        result = [0]*n

        prefix = suffix = 1

        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
