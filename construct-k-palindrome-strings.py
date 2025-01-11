class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
          Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
        """
        n = len(s)
        if n < k:
            return False

        char_count = Counter(s)

        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)

        return odd_count <= k
