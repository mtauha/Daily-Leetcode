class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        """
          The bitwise AND of an array nums is the bitwise AND of all integers in nums.
          
          For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
          Also, for nums = [7], the bitwise AND is 7.
          You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.
          
          Return the size of the largest combination of candidates with a bitwise AND greater than 0.
        """
        bit_count = [0] * 24
        for i in range(24):
            for num in candidates:
                if (num & (1 << i)) != 0:
                    bit_count[i] += 1

        return max(bit_count)
