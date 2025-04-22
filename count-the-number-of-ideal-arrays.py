from collections import defaultdict

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        max_k = 14  # Max chain length (log2(10^4))
        C = [[0] * (max_k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, max_k + 1):
                if j <= i:
                    C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        dp = [defaultdict(int) for _ in range(maxValue + 1)]
        for val in range(1, maxValue + 1):
            dp[val][1] = 1

        for length in range(2, max_k + 1):
            for val in range(1, maxValue + 1):
                for mul in range(2 * val, maxValue + 1, val):
                    dp[mul][length] = (dp[mul][length] + dp[val][length - 1]) % MOD

        ans = 0
        for val in range(1, maxValue + 1):
            for k in dp[val]:
                if k <= n:
                    ans = (ans + dp[val][k] * C[n - 1][k - 1]) % MOD

        return ans
