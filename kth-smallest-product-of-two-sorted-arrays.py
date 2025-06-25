class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def part(mid):
            count = 0
            n2 = len(nums2)
            for x in nums1:
                if x > 0:
                    target = mid // x
                    count += bisect_right(nums2, target)
                elif x < 0:
                    target = ceil(mid / x)
                    count += n2 - bisect_left(nums2, target)
                else:
                    if mid >= 0:
                        count += n2
            
            return count

        left = min(nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1])
        right = max(nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1])


        while left < right:
            mid = (left + right) // 2

            if part(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
