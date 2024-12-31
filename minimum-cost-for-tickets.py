class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
            You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

            Train tickets are sold in three different ways:

            a 1-day pass is sold for costs[0] dollars,
            a 7-day pass is sold for costs[1] dollars, and
            a 30-day pass is sold for costs[2] dollars.
            The passes allow that many days of consecutive travel.

            For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
            Return the minimum number of dollars you need to travel every day in the given list of days.
        """
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        i = 0
        for day in range(1, last_day + 1):
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                i += 1
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2]
                )

        return dp[last_day]
