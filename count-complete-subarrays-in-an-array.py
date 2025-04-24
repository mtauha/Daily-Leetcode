from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total_unique = len(set(nums))
        count = defaultdict(int)
        unique = 0
        ans = 0
        right = 0

        for left in range(n):
            while right < n and unique < total_unique:
                if count[nums[right]] == 0:
                    unique += 1
                count[nums[right]] += 1
                right += 1

            if unique < total_unique:
                break

            ans += n - (right - 1)

            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                unique -= 1

        return ans
