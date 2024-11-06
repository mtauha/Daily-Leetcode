class Solution:
    def canSortArray(self, nums):
        """
            You are given a 0-indexed array of positive integers nums.

            In one operation, you can swap any two adjacent elements if they have the same number of 
            set bits
            . You are allowed to do this operation any number of times (including zero).
            
            Return true if you can sort the array, else return false.
        """
        n = len(nums)

        values = nums.copy()

        for i in range(n):
            for j in range(n - i - 1):
                if values[j] <= values[j + 1]:
                    continue
                else:
                    if bin(values[j]).count("1") == bin(values[j + 1]).count(
                        "1"
                    ):
                        values[j], values[j + 1] = values[j + 1], values[j]
                    else:
                        return False
        return True
