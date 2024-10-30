class Solution:
    def getLongestIncreasingSubsequenceLength(self, v: List[int]) -> List[int]:
        """
            You may recall that an array arr is a mountain array if and only if:

            arr.length >= 3
            There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
            arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
            Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.
        """
        lis_len = [1] * len(v)
        lis = [v[0]]

        for i in range(1, len(v)):
            index = self.lowerBound(lis, v[i])

            if index == len(lis):
                lis.append(v[i])
            else:
                lis[index] = v[i]

            lis_len[i] = len(lis)

        return lis_len

    def lowerBound(self, lis: List[int], target: int) -> int:
        left, right = 0, len(lis)
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = self.getLongestIncreasingSubsequenceLength(nums)

        nums.reverse()
        lds_length = self.getLongestIncreasingSubsequenceLength(nums)
        lds_length.reverse()

        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals
