class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        Colors = [ord(c) - 97 for c in colors]
        indegree = [0] * n
        queue = deque()
        dp = [[0]*26 for _ in range(n)]

        for i, j in edges:
            graph[i].append(j)
            indegree[j] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][Colors[i]] = 1
        
        seen, res = 0, 0
        while queue:
            node = queue.popleft()
            seen += 1
            anode = max(dp[node])

            if anode > res:
                res = anode
            
            base = dp[node]
            for v in graph[node]:
                row_v = dp[v]
                col_v = Colors[v]

                for c in range(26):
                    val = base[c] + (1 if c == col_v else 0)
                    if val > row_v[c]:
                        row_v[c] = val
                
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
            dp[node] = None
        
        return res if seen == n else -1
