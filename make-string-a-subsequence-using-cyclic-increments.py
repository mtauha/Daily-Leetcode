class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
            You are given two 0-indexed strings str1 and str2.

            In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

            Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

            Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.
        """
        i, j = 0, 0
        n1, n2 = len(str1), len(str2)

        while i < n1 and j < n2:
            if (
                str1[i] == str2[j]
                or (str1[i] == "z" and str2[j] == "a")
                or (chr(ord(str1[i]) + 1) == str2[j])
            ):
                j += 1
            i += 1

        return j == n2
