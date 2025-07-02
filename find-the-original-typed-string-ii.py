class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(word)
        current_run_length = 1
        consecutive_group_lengths = []

        # Step 1: Compress word into groups of same characters
        for i in range(1, n):
            if word[i] == word[i - 1]:
                current_run_length += 1
            else:
                consecutive_group_lengths.append(current_run_length)
                current_run_length = 1
        consecutive_group_lengths.append(current_run_length)

        # Step 2: Calculate initial answer as product of run lengths
        total_ways = 1
        for group_len in consecutive_group_lengths:
            total_ways = (total_ways * group_len) % MOD

        # Step 3: If already at least k groups, return total product
        if len(consecutive_group_lengths) >= k:
            return total_ways

        # Step 4: DP to count invalid ways
        dp = [1] + [0] * (k - 1)
        prefix_sums = [1] * k

        for group_len in consecutive_group_lengths:
            new_dp = [0] * k
            for j in range(1, k):
                new_dp[j] = prefix_sums[j - 1]
                if j - group_len - 1 >= 0:
                    new_dp[j] = (new_dp[j] - prefix_sums[j - group_len - 1]) % MOD
            new_prefix_sums = [new_dp[0]] + [0] * (k - 1)
            for j in range(1, k):
                new_prefix_sums[j] = (new_prefix_sums[j - 1] + new_dp[j]) % MOD
            dp = new_dp
            prefix_sums = new_prefix_sums

        return (total_ways - prefix_sums[k - 1]) % MOD
