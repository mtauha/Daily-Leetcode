"""Description:
    Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]

            left_sorted = merge_sort(left_half)
            right_sorted = merge_sort(right_half)

            return merge(left_sorted, right_sorted)

        def merge(left, right):
            merged = []
            left_index, right_index = 0, 0

            while left_index < len(left) and right_index < len(right):
                if left[left_index] <= right[right_index]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1

            merged.extend(left[left_index:])
            merged.extend(right[right_index:])

            return merged

        return merge_sort(nums)


sol = Solution()
