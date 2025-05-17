"""Description:
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def sort(left, right):
            if left < right:
                pivot = partition(left, right)
                sort(left, pivot - 1)
                sort(pivot + 1, right)

        def partition(low, high):
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] < pivot:
                    swap(i, j)
                    i += 1
            swap(i, high)
            return i

        sort(0, len(nums) - 1)
        
