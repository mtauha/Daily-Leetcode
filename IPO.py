"""Description:
    Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

    You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

    Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

    Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

    The answer is guaranteed to fit in a 32-bit signed integer.
"""

import heapq

class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(profits))]

        projects.sort(key=lambda x: x[0])

        maxheap = []
        index = 0

        for _ in range(k):
            while index < len(projects) and projects[index][0] <=w:
                heapq.heappush(maxheap, -projects[index][1])
                index +=1

            if maxheap:
                w -= heapq.heappop(maxheap)

            if not maxheap and (index >= len(projects) or projects[index][0] > w):
                break

        return w


sol = Solution()
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

print(sol.findMaximizedCapital(k,w,profits,capital))
