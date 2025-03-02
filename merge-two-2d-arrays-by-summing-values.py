class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        nums1.extend(nums2)
        nums1.sort(key=lambda x: x[0])
        
        tbd = []
        
        for i in range(len(nums1) - 1):
            if nums1[i][0] == nums1[i+1][0]:
                nums1[i][1] += nums1[i+1][1]
                tbd.append(i+1)
        
        for i in reversed(tbd):
            del nums1[i]
        
        return nums1
        
