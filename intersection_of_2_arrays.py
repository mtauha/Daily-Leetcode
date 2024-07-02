"""Description:
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        for num in nums1[:]:
            if num in nums2:
                nums2.remove(num)
                intersection.append(num)

        return intersection


sol = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(sol.intersect(nums1,nums2))
