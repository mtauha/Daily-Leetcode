class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)

        total_happiness = 0
        for i in range(k):
            total_happiness += max(0, happiness[i] - i)

        return total_happiness


sol = Solution()
arr = [12, 1, 42]
k = 3
print(sol.maximumHappinessSum(arr, k))
