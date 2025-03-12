class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_neg, count_pos = 0, 0

        for i in nums:
            if i < 0:
                count_neg += 1
            if i > 0:
                count_pos += 1
        
        return max(count_neg, count_pos)
