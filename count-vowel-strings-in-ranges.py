from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
            You are given a 0-indexed array of strings words and a 2D array of integers queries.

            Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

            Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

            Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
        """
        valid = [0] * len(words)
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Use set for faster lookup
        ans = []
        n = len(words)

        total = 0  # Avoid overwriting 'sum' (built-in function)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                total += 1
            valid[i] = total

        for l, r in queries:
            ans.append(valid[r] - (0 if l == 0 else valid[l - 1]))

        return ans
