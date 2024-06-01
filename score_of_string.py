"""Description:
        You are given a string s. The score of a string is defined as the sum of the absolute difference between 
    the ASCII values of adjacent characters.

    Return the score of s.
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum([abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1)])


sol = Solution()
string = "racecar"
print(sol.scoreOfString(string))
