class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
            You are given a string s. You can convert s to a palindrome by adding characters in front of it.
            Return the shortest palindrome you can find by performing this transformation.
        """
      
        n = len(s)
        reverse = s[::-1]
        if s == reverse:
            return s

        for i in range(n):
            if s[:n-i] == reverse[i:]:
                return reverse[:i] + s
