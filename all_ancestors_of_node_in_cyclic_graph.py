"""Description:
    You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

    You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

    Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

    A node u is an ancestor of another node v if u can reach v via a set of edges.
"""

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        answer = [set() for _ in range(n)]

        from collections import defaultdict, deque

        indegree = [0] * n
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])

        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                answer[neighbour].update(answer[node])
                answer[neighbour].add(node)

                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return [list(sorted(ans)) for ans in answer]


sol = Solution()
n = 9
edges = [
    [8, 3],
    [6, 3],
    [1, 6],
    [7, 0],
    [8, 5],
    [2, 1],
    [4, 0],
    [2, 3],
    [0, 3],
    [5, 3],
    [7, 4],
    [4, 1],
]
print(sol.getAncestors(n, edges))
