class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        """
            You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

            Return any valid arrangement of pairs.

            Note: The inputs will be generated such that there exists a valid arrangement of pairs.
        """
        graph = defaultdict(list)
        degrees = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            degrees[start] += 1 # Out-degree
            degrees[end] -= 1 # In-degree
        
        start = pairs[0][0]
        for node in degrees:
            if degrees[node] == 1:
                start = node
                break
        
        path = []

        def dfs(current_node):
            while graph[current_node]:
                next_node = graph[current_node].pop()
                dfs(next_node)
                path.append((current_node, next_node))
        
        dfs(start)
        return path[::-1]
