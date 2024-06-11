"""Description:
    Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

    Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""

from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result = []
        counter = Counter(arr1)

        for i in range(len(arr2)):
            if arr2[i] in counter:
                result.extend([arr2[i]]*counter[arr2[i]])
                del counter[arr2[i]]

        remaining_elements = sorted([num for num in counter for _ in range(counter[num])])
        result.extend(remaining_elements)

        return result


sol = Solution()
arr1, arr2 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]

print(sol.relativeSortArray(arr1,arr2))
