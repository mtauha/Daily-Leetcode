class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
            Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

            Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

            A palindrome is a string that reads the same forwards and backwards.

            A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

            For example, "ace" is a subsequence of "abcde".
        """
        first = [-1] * 26
        last = [-1] * 26
        
        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if first[curr] == -1:
                first[curr] = i
            
            last[curr] = i
        
        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue
                
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
            
            ans += len(between)

        return ans
