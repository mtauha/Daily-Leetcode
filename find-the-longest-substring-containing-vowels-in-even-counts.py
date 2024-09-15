class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
            Given the string s, return the size of the longest substring containing each vowel an even number of times. 
            That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
        """
        prefix_xor = 0
        prefix = [-1] * 32
        longest_substring = 0

        def bit_mask(c):
            if c == 'a':
                return 1
            if c == 'e':
                return 2
            if c == 'i':
                return 4
            if c == 'o':
                return 8
            if c == 'u':
                return 16
            else:
                return 0

        for i in range(len(s)):
            prefix_xor ^= bit_mask(s[i])
            if prefix_xor != 0 and prefix[prefix_xor] == -1:
                prefix[prefix_xor] = i
            longest_substring = max(longest_substring, i - prefix[prefix_xor])
        
        return longest_substring





