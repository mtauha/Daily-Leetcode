class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        heap = []
        ans, event = 0, 0

        for day in range(1, max_day + 1):
            while event < n and events[event][0] <= day:
                heapq.heappush(heap, events[event][1])
                event += 1
            
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                ans += 1
        
        return ans

        
        
