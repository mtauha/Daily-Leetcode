def Sum(first: int, num: int, diff: int) -> int:
    return int((num / 2) * (2 * first + (num - 1) * diff))


class Solution:
    def totalMoney(self, n: int) -> int:
        quotient = n // 7
        remainder = n % 7

        return Sum(28, quotient, 7) + Sum(quotient + 1, remainder, 1)


solution = Solution()
print(solution.totalMoney(10))
