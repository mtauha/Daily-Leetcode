"""Description:
    A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

    Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

    The second minimum value is defined as the smallest value strictly larger than the minimum value.

    For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
    Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

    Notes:

    You can go through any vertex any number of times, including 1 and n.
    You can assume that when the journey starts, all signals have just turned green.
"""

from collections import deque
from typing import List

class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0

        while q:
            node, freq = q.popleft()

            time_taken = dist1[node] if freq == 1 else dist2[node]

            if (time_taken // change) % 2 == 1:
                time_taken = change * (time_taken // change + 1) + time
            else:
                time_taken += time

            for neighbor in adj[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = time_taken
                    q.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != time_taken:
                    if neighbor == n:
                        return time_taken
                    dist2[neighbor] = time_taken
                    q.append((neighbor, 2))

        return 0


sol = Solution()
