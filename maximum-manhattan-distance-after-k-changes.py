class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        pos = [0, 0]

        for idx, i in enumerate(s):
            if i == 'N':
                pos[0] += 1
            elif i == 'S':
                pos[0] -= 1
            elif i == 'E':
                pos[1] += 1
            else:
                pos[1] -= 1
            
            # Calculte the distance
            distance = abs(pos[0]) + abs(pos[1])
            
            # max(ans, ...): Bounded Maximum distance is calculated. 
            # (distance + k*2) : If we change a character it means we shift 2 points in the grid. Suppose You are at +1 when you changed character now you are at -1. Difference between +1 and -1 is 2. That's why you multiplied k by 2 to calculate the maximum possible distance.
            # idx + 1: Maximum position you can go. This is Size constraint.
            # min(distance + k*2, idx + 1): Check max distance under constraint of size
            ans = max(ans, min(distance + k*2, idx + 1))

        return ans 
