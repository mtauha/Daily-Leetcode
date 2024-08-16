class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        """Description:
            You are given m arrays, where each array is sorted in ascending order.

            You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

            Return the maximum distance.
        """

        if len(arrays) < 2:
            return 0

        global_max, global_min = arrays[0][-1], arrays[0][0]
        result = 0

        for arr in arrays[1:]:
            local_min, local_max = arr[0], arr[-1]
            result = max(result, max(local_max - global_min, global_max - local_min))
            global_min = min(global_min, local_min)
            global_max = max(global_max, local_max)

        return result


sol = Solution()
print(sol.maxDistance.__doc__)