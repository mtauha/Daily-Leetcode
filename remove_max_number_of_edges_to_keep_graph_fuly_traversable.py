"""Description:
    Alice and Bob have an undirected graph of n nodes and three types of edges:

    Type 1: Can be traversed by Alice only.
    Type 2: Can be traversed by Bob only.
    Type 3: Can be traversed by both Alice and Bob.
    Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

    Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
"""

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:

        type1, type2, type3 = [], [], []
        
        for edge in edges:
            if edge[0] == 3:
                type3.append((edge[1], edge[2]))
            elif edge[0] == 1:
                type1.append((edge[1], edge[2]))
            elif edge[0] == 2:
                type2.append((edge[1], edge[2]))

        parent = list(range(n + 1))

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 != parent2:
                parent[parent2] = parent1
                return True

            return False

        used_nodes = 0
        for u, v in type3:
            if union(u, v):
                used_nodes += 1

        parent_bob = parent[:]
        for u, v in type1:
            if union(u, v):
                used_nodes += 1

        parent = parent_bob
        for u, v in type2:
            if union(u, v):
                used_nodes += 1

        if len(set(find(node) for node in range(1, n + 1))) == 1:
            return len(edges) - used_nodes
        else:
            return -1


sol = Solution()

n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
sol.maxNumEdgesToRemove(n, edges)
print(edges)
