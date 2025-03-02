class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        zeros = 0
        nums_copy = [i for i in nums if i != 0]

        for i in nums:
            if i == 0:
                zeros += 1

        zero = [0]*zeros
        nums_copy.extend(zero)
                
        return nums_copy
