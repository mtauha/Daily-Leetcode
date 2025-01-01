class Solution:
    def maxScore(self, s: str) -> int:
        """
            Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

            The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
        """
        ones = 0
        zeros = 0
        best = -inf

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1
            
            best = max(best, zeros - ones)
            
        if s[-1] == "1":
            ones += 1
        
        return best + ones
