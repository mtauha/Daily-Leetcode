class Solution:
    def check_prime(self, x: int) -> bool:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        """
            You are given a 0-indexed integer array nums of length n.

            You can perform the following operation as many times as you want:

            Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
            Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

            A strictly increasing array is an array whose each element is strictly greater than its preceding element.
        """
        for i in range(len(nums)):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i - 1]

            if bound <= 0:
                return False

            largest_prime = 0
            for j in range(bound - 1, 1, -1):
                if self.check_prime(j):
                    largest_prime = j
                    break

            nums[i] = nums[i] - largest_prime
        return True
