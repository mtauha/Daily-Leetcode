"""Description:
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.
"""

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


class Solution:
    def sort(self, nums, low, high):
        if low < high:
            pivot_index = self.partition(nums, low, high)
            self.sort(nums, low, pivot_index - 1)
            self.sort(nums, pivot_index + 1, high)

    def partition(self, nums: list[int], low, high):
        pivot = nums[low]
        left = low + 1
        right = high

        while True:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left <= right:
                swap(nums, left, right)
            else:
                break

        swap(nums, low, right)
        return right

    def sortColors(self, nums: list[int]) -> None:
        self.sort(nums, 0, len(nums) - 1)
