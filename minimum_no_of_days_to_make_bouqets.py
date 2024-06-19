"""Description:
    You are given an integer array bloomDay, an integer m and an integer k.

    You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

    The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

    Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
"""

class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def possible(bloomDay, day, m, k):
            count = 0
            bouqets = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    bouqets += count // k
                    count = 0

            bouqets += count // k

            return True if bouqets >= m else False

        low, high, ans = min(bloomDay), max(bloomDay), 0
        while low <= high:
            mid = (low + high) // 2
            if possible(bloomDay, mid, m, k):
                high = mid - 1
            else:
                low = mid + 1

        return low


sol = Solution()
bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
print(sol.minDays(bloomDay, m, k))
