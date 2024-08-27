class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
            You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
            Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
            If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
        """
        max_prob = [0]*n
        max_prob[start_node] = 1

        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        queue = deque([start_node])
        while queue:
            cur_node = queue.popleft()
            for nxt_node, path_prob in graph[cur_node]:
                if max_prob[cur_node] * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = max_prob[cur_node] * path_prob
                    queue.append(nxt_node)
        
        return max_prob[end_node]
