class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
            Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

            Return the length of the shortest subarray to remove.

            A subarray is a contiguous subsequence of the array.
        """
        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right - left - 1)
            left += 1
        return ans
