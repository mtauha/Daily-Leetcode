class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        graph = defaultdict(list)

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        min_heap = [(0, 0)]
        shortest_time = [float("inf")] * n
        path_count = [0] * n
        
        shortest_time[0] = 0
        path_count[0] = 1

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_time > shortest_time[curr_node]:
                continue
            
            for neighbour_node, time in graph[curr_node]:
                if curr_time + time < shortest_time[neighbour_node]:
                    shortest_time[neighbour_node] = curr_time + time
                    path_count[neighbour_node] = path_count[curr_node]
                    heapq.heappush(
                        min_heap, (shortest_time[neighbour_node], neighbour_node)
                    )
                elif curr_time + time == shortest_time[neighbour_node]:
                    path_count[neighbour_node] = (
                        path_count[neighbour_node] + path_count[curr_node]
                    ) % MOD
        return path_count[n - 1]        

