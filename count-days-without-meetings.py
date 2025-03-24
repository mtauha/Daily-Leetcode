class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        free_days = 0
        latest_end = 0

        for start, end in meetings:
            if start > latest_end + 1:
                free_days += start - latest_end - 1

            latest_end = max(end, latest_end)

        return free_days + days - latest_end
