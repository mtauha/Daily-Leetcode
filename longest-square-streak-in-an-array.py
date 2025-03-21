class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
            You are given an integer array nums. A subsequence of nums is called a square streak if:

            The length of the subsequence is at least 2, and
            after sorting the subsequence, each element (except the first element) is the square of the previous number.
            Return the length of the longest square streak in nums, or return -1 if there is no square streak.
            
            A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
        """
        uniqueNumbers = set(nums)
        longestStreak = 0
        
        for i in nums:
            currentStreak = 0
            current = i

            while current in uniqueNumbers:
                currentStreak += 1
                if current*current > 10**5:
                    break
                
                current *= current
            
            longestStreak = max(longestStreak, currentStreak)
        
        return longestStreak if longestStreak >= 2 else -1

            

