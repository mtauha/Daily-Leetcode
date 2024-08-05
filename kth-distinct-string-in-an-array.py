"""Description:
    A distinct string is a string that is present only once in an array.

    Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

    Note that the strings are considered in the order in which they appear in the array.
"""

from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = dict(Counter(arr))
        
        skip = 1
        for i in arr:
            if count[i] == 1:
                if skip == k:
                    return i
                skip += 1

        return ""


sol = Solution()
arr = ["d", "b", "c", "b", "c", "a"]
k = 2

print(sol.kthDistinct(arr, k))
