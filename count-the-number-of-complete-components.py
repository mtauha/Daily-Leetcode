class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * n
        count = 0
        
        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, component):
            stack = [node]
            visited[node] = True
            component.add(node)
            
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                        component.add(neighbor)
        
        # Count complete components
        for i in range(n):
            if not visited[i]:
                component = set()
                dfs(i, component)
                
                # Check if the component is complete
                is_complete = all(len(graph[node]) == len(component) - 1 for node in component)
                if is_complete:
                    count += 1
        
        return count
