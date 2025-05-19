class Solution:
    def triangleType(self, nums: List[int]) -> str:
        base, width, hyp = nums[0], nums[1], nums[2]
        uniq = len(set(nums))

        if not ((base + width > hyp) and (base + hyp > width) and (width + hyp > base)):
            return "none"
    
        if uniq == 1:
            return "equilateral"
        if uniq == 2:
            return "isosceles"
        else:
            return "scalene"
