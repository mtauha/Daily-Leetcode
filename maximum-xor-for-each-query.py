class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
        You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:

        Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
        Remove the last element from the current array nums.
        Return an array answer, where answer[i] is the answer to the ith query.
        """
        prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        ans = [0] * len(nums)

        # Main Logic
        mask = (1 << maximumBit) - 1

        for i in range(len(nums)):
            current_xor = prefix_xor[len(prefix_xor) - 1 - i]
            ans[i] = current_xor ^ mask

        return ans
