"""Description:
    There are n 1-indexed robots, each having a position on a line, health, and movement direction.

    You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

    All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

    If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

    Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

    Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

    Note: The positions may be unsorted.
"""


class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        if "L" not in directions or "R" not in directions:
            return healths

        directions = [i for i in directions]
        robots = sorted(zip(positions, healths, directions, range(len(positions))))

        stack = []

        for pos, health, dir, index in robots:
            if dir == "R":
                stack.append((pos, health, dir, index))
            else:
                while stack and stack[-1][2] == "R":
                    r_pos, r_health, r_dir, r_index = stack.pop()

                    if r_health > health:
                        r_health -= 1
                        stack.append((r_pos, r_health, r_dir, r_index))
                        health = 0
                        break
                    elif r_health < health:
                        health -= 1
                    else:
                        health = 0
                        break
                
                if health > 0:
                    stack.append((pos, health, dir, index))
        
        survivors = sorted(stack, key=lambda x:x[3])

        return [health for pos, health, dir, idx in survivors]


positions = [5, 4, 3, 2, 1]
healths = [2, 17, 9, 15, 10]
directions = "RRRRR"
sol = Solution()

print(sol.survivedRobotsHealths(positions, healths, directions))
