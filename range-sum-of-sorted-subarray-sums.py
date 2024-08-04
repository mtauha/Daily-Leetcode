"""Description:
    You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

    Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
"""


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        sum_arr = []

        for index in range(n):
            current_sum = 0
            for i in range(index, n):
                current_sum += nums[i]
                sum_arr.append(current_sum)

        sum_arr.sort()
        return sum(sum_arr[left - 1 : right]) % (10**9 + 7)


sol = Solution()
nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
print(sol.rangeSum(nums, n, left, right))
