class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        """
        There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

        You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.

        A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.

        Return the maximum number of components in any valid split.
        """
        if n < 2:
            return 1
        component_count = 0
        graph = defaultdict(list)
        in_degree = [0 for _ in range(n)]

        # Build the graph and calculate in-degrees
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            in_degree[node1] += 1
            in_degree[node2] += 1

        # Initialize the queue with nodes having in-degree of 1 (leaf nodes)
        queue = deque(node for node in range(n) if in_degree[node] == 1)

        while queue:
            current_node = queue.popleft()
            in_degree[current_node] -= 1
            add_value = 0

            # Check if the current node's value is divisible by k
            if values[current_node] % k == 0:
                component_count += 1
            else:
                add_value = values[current_node]

            # Propagate the value to the neighbor nodes
            for neighbor_node in graph[current_node]:
                if in_degree[neighbor_node] == 0:
                    continue
                in_degree[neighbor_node] -= 1
                values[neighbor_node] += add_value

                # If the neighbor node's in-degree becomes 1, add it to the queue
                if in_degree[neighbor_node] == 1:
                    queue.append(neighbor_node)

        return component_count
