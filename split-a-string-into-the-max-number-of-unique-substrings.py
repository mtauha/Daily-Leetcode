class Solution:
    """
          Given a string s, return the maximum number of unique substrings that the given string can be split into.
          You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
          A substring is a contiguous sequence of characters within a string.
    """
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrack(s, 0, seen)

    def backtrack(self, s, start, seen):
        if start == len(s):
            return 0

        max_count = 0

        for end in range(start + 1, len(s) + 1):
            sub_string = s[start:end]
            if sub_string not in seen:
                seen.add(sub_string)
                max_count = max(max_count, 1 + self.backtrack(s, end, seen))
                seen.remove(sub_string)

        return max_count
