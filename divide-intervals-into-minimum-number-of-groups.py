class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        """
            You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
            You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.
            
            Return the minimum number of groups you need to make.
            Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.
        """
        events = []

        for interval in intervals:
            events.append((interval[0], 1))  
            events.append((interval[1] + 1, -1))

    
        events.sort(key=lambda x: (x[0], x[1]))

        concurrent_intervals = 0
        max_concurrent_intervals = 0

        for event in events:
            concurrent_intervals += event[1]
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )

        return max_concurrent_intervals
