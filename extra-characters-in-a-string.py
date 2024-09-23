class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
            You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. 
            There may be some extra characters in s which are not present in any of the substrings.
            Return the minimum number of extra characters left over if you break up s optimally.
        """
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]
