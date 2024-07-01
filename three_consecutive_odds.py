"""Description:
    Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
"""

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                count += 1
            else:
                count = 0

            if count == 3:
                return True

        return False
