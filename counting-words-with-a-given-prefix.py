class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
            You are given an array of strings words and a string pref.

            Return the number of strings in words that contain pref as a prefix.

            A prefix of a string s is any leading contiguous substring of s.
        """
        count = 0

        for i in words:
            if i.startswith(pref):
                count += 1

        return count
