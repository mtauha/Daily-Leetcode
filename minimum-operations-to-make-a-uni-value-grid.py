class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        result = 0

        for row in grid:
            nums.extend(row)

        nums.sort()
        length = len(nums)

        median = nums[length//2]

        for num in nums:
            if num % x != median % x:
                return -1
            
            result += abs(median - num) // x
    
        return result
        
