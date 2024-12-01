class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
            Given an array arr of integers, check if there exist two indices i and j such that :

            - i != j
            - 0 <= i, j < arr.length
            - arr[i] == 2 * arr[j]
        """
        visited = set()

        for num in arr:
            if (num * 2 in visited) or ((num % 2 == 0) and (num // 2 in visited)):
                return True
            visited.add(num)
        return False
