class Solution:
    def minimumTotalDistance(
        self, robots: List[int], factories: List[List[int]]
    ) -> int:
        """
            There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.
            The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.
            All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.
            At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.
            
            Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.
            
            Note that:
            - All robots move at the same speed.
            - If two robots move in the same direction, they will never collide.
            - If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
            - If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
            - If the robot moved from a position x to a position y, the distance it moved is |y - x|.
        """
        robots.sort()
        factories.sort()

        factory_positions = []
        for factory in factories:
            for i in range(factory[1]):
                factory_positions.append(factory[0])

        robot_count = len(robots)
        factory_count = len(factory_positions)
        next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]

        for i in range(robot_count - 1, -1, -1):
            if i != robot_count - 1:
                next_dist[factory_count] = 1e12

            current[factory_count] = 1e12

            for j in range(factory_count - 1, -1, -1):
                assign = (
                    abs(robots[i] - factory_positions[j]) + next_dist[j + 1]
                )

                skip = current[j + 1]
                current[j] = min(assign, skip)

            next_dist = current[:]

        return current[0]
