"""Description:
    You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

    You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

    You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

    Return the maximum total importance of all roads possible after assigning the values optimally.
"""

class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        from collections import defaultdict

        degree = defaultdict(int)
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        sorted_cities = sorted(degree.items(), key=lambda x: x[1], reverse=True)

        value = n
        city_values = {}

        for city, _ in sorted_cities:
            city_values[city] = value
            value -= 1

        for city in range(n):
            if city not in city_values:
                city_values[city] = value
                value -= 1

        importance = 0
        for a, b in roads:
            importance += city_values[a] + city_values[b]

        return importance


sol = Solution()
n = 5
roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]

print(sol.maximumImportance(n, roads))
