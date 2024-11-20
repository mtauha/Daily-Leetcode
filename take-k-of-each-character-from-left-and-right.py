class Solution:
    def takeCharacters(self, string: str, k: int) -> int:
        """
            You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

            Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
        """
        counter: List[int] = [0] * 3
        for letter in string:
            counter[ord(letter) - ord("a")] += 1
        if counter[0] < k or counter[1] < k or counter[2] < k:
            return -1
        i: int = 0
        j: int = 0
        middleSubstringLength: int = 0
        string_length: int = len(string)
        while i < string_length:
            counter[ord(string[i]) - ord("a")] -= 1
            while counter[ord(string[i]) - ord("a")] < k:
                counter[ord(string[j]) - ord("a")] += 1
                j += 1
            i += 1
            middleSubstringLength = max(middleSubstringLength, i - j)
        return string_length - middleSubstringLength
