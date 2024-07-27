"""Description:
    You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

    You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

    Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

    Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
"""

from collections import defaultdict
import heapq


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:

        adj = defaultdict(list)

        for i in range(len(original)):
            adj[original[i]].append((changed[i], cost[i]))

        def djisktra(src):
            heap = [(0, src)]
            min_cost_map = {}

            while heap:
                cost, node = heapq.heappop(heap)
                if node in min_cost_map:
                    continue

                min_cost_map[node] = cost
                for neigh, neigh_cost in adj[node]:
                    heapq.heappush(heap, (neigh_cost + cost, neigh))

            return min_cost_map

        min_cost_map = {node: djisktra(node) for node in set(source)}
        result = 0

        for i in range(len(source)):
            if target[i] not in min_cost_map[source[i]]:
                return -1

            result += min_cost_map[source[i]][target[i]]

        return result


sol = Solution()
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]

print(sol.minimumCost(source, target, original, changed, cost))
