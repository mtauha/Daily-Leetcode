"""Description:
    In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

    Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

    Given the integer array position and the integer m. Return the required force.
"""

class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        def check(mid):
            count, last = 1, position[0]

            for i in range(1, len(position)):
                if position[i] - last >= mid:
                    count+=1
                    last = position[i]

                    if count == m:
                        return True

            return False

        position.sort()

        low = 1
        high = position[-1] - position[0]
        ans = 0

        while low <= high:
            mid = (low+high)//2
            if check(mid):
                ans = mid
                low = mid+1
            else:
                high = mid - 1

        return ans
