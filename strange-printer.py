class Solution:
    def strangePrinter(self, s: str) -> int:
        """Descripton:
          There is a strange printer with the following two special properties:

          The printer can only print a sequence of the same character each time.
          At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
          Given a string s, return the minimum number of turns the printer needed to print it.  
        """
        @functools.lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            res = dp(i+1, j) + 1  # Print s[i] separately
            for k in range(i+1, j+1):
                if s[i] == s[k]:
                    res = min(res, dp(i, k-1) + dp(k+1, j))
            return res

        return dp(0, len(s) - 1)
