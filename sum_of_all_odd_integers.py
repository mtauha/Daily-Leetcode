class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ln = len(arr)
        subsets = [arr[i:j] for i in range(ln) for j in range(i + 1, ln + 1)]
        summ = 0

        for list in subsets:
            if len(list) % 2 != 0:
                summ += sum(list)

        return summ


sol = Solution()
arr = [1, 4, 2, 5, 3]
print(sol.sumOddLengthSubarrays(arr))
