from collections import defaultdict
class Solution:
    def beautifulSubsets(self, nums, k):
        n, dict1 = len(nums), defaultdict(int)

        def backtrack(idx):
            total = 0

            for j in range(idx, n):
                if dict1[nums[j] + k] == 0 and dict1[nums[j] - k] == 0:
                    dict1[nums[j]] += 1
                    total += 1 + backtrack(j + 1)
                    dict1[nums[j]] -= 1

            return total

        return backtrack(0)


# Example usage:
sol = Solution()
nums = [10, 4, 5, 7, 2, 1]
k = 3
print(sol.beautifulSubsets(nums, k))


sol = Solution()
nums = [10, 4, 5, 7, 2, 1]
k = 3
print(sol.beautifulSubsets(nums, k))
