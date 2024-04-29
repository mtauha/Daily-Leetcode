class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) ):
                if nums[i] + nums[j] == target:
                    ans.extend([i, j])
                    return ans


solution = Solution()
nums = [-3, 4, 3, 90]
target = 0
print(solution.twoSum(nums=nums, target=target))
