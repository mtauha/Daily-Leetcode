class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()
        ptr1 = 0
        ans = 0
        total = 0

        for ptr2 in range(n):
            while nums[ptr2] in visited:
                total -= nums[ptr1]
                visited.remove(nums[ptr1])
                ptr1 += 1
            
            visited.add(nums[ptr2])
            total += nums[ptr2]
            ans = max(ans, total)

        return ans
