class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
          Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
        """
        minutes = []
        differences = []

        for time in timePoints:
            hours1, mins1 = time.split(":")
            mins1 = 60*int(hours1) + int(mins1) 

            minutes.append(mins1)
        
        minutes.sort()
        ans = min(minutes[i+1] - minutes[i] for i in range(len(minutes) - 1))

        print(minutes)

        return min(ans, 24*60 - minutes[-1] + minutes[0])
                


