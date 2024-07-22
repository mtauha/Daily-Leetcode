"""Description:
    You are given a positive integer k. You are also given:

    a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
    a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
    The two arrays contain integers from 1 to k.

    You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

    The matrix should also satisfy the following conditions:

    The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
    The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
    Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
"""

from collections import defaultdict
class Solution:
    def buildMatrix(
        self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]
    ) -> list[list[int]]:

        def dfs(src, adj, visited, path, order):
            if src in path:
                return False
            if src in visited:
                return True

            visited.add(src)
            path.add(src)

            for neighbour in adj[src]:
                if not dfs(neighbour, adj, visited, path, order):
                    return False

            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges):
            adj = defaultdict(list)

            for src, dest in edges:
                adj[src].append(dest)

            visited, path = set(), set()
            order = []

            for src in range(1, k + 1):
                if not dfs(src, adj, visited, path, order):
                    return []

            return order[::-1]

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        hash_row_order = {n: i for i, n in enumerate(row_order)}
        hash_col_order = {n: i for i, n in enumerate(col_order)}

        result = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            row, col = hash_row_order[num], hash_col_order[num]

            result[row][col] = num

        return result


sol = Solution()
