class Solution:
    def __init__(self):
        self.HASH_MULTIPLIER = 60013
    
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
            A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

            -2: Turn left 90 degrees.
            -1: Turn right 90 degrees.
            1 <= k <= 9: Move forward k units, one unit at a time.
            Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
            
            Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).
            
            Note:
            
            - North means +Y direction.
            - East means +X direction.
            - South means -Y direction.
            - West means -X direction.
            - There can be obstacle in [0,0].

        """
        ans = 0

        x, y = 0, 0
        #             North ,  East ,   West ,  South
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}

        for command in commands:
            if command == -1:
                curr_dir = (curr_dir + 1) % 4
                continue
            if command == -2:
                curr_dir = (curr_dir + 3) % 4
                continue
            
            dx, dy = directions[curr_dir]
            for _ in range(command):
                next_x, next_y = x+dx, y+dy
                if self._hash_coordinates(next_x, next_y) in obstacle_set:
                    break
                x, y = next_x, next_y
            
            ans = max(ans, x*x + y*y)
        
        return ans
            

        
    
    def _hash_coordinates(self, x, y):
        return x + self.HASH_MULTIPLIER*y
