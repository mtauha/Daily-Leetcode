class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:

        minimum = min(prices)
        prices.remove(minimum)
        remaining = money - minimum
        remaining -= min(prices)

        if remaining < 0:
            return money

        return remaining


sol = Solution()
prices = [3, 2, 3]
money = 3
print(sol.buyChoco(prices, money))
