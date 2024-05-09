class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        nums.sort()
        return (nums[-1] - 1)*(nums[-2] - 1)

sol = Solution()

arr = [3, 4, 5, 2]
print(sol.maxProduct(arr))