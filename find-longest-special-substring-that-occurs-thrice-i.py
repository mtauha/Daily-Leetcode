class Solution:
    def maximumLength(self, s: str) -> int:
        """
            You are given a string s that consists of lowercase English letters.

            A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

            Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

            A substring is a contiguous non-empty sequence of characters within a string.
        """
        substring_length = 0
        ans = -1
        previous_character = ""
        substring_lengths = [[-1, -1, -1] for _ in range(26)]
        for character in s:
            if character == previous_character:
                substring_length += 1
            else:
                substring_length = 1
                previous_character = character

            min_length = min(substring_lengths[ord(character) - ord("a")])
            if substring_length > min_length:
                substring_lengths[ord(character) - ord("a")][
                    substring_lengths[ord(character) - ord("a")].index(
                        min_length
                    )
                ] = substring_length

        for char_idx in range(26):
            ans = max(ans, min(substring_lengths[char_idx]))

        return ans
