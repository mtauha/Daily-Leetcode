class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        valid = set()

        for num in nums:
            if num < k:
                return -1
            if num > k:
                valid.add(num)

        return len(valid)
