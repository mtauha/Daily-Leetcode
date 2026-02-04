class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        NEG_INF = -10**18
        UNVISITED = None

        dp = [[UNVISITED]*4 for _ in range(n+1)]

        def solve(i, trend):
            if i == n:
                return 0 if trend == 3 else NEG_INF

            if dp[i][trend] is not UNVISITED:
                return dp[i][trend]

            take = NEG_INF
            skip = NEG_INF

            # skip only before starting
            if trend == 0:
                skip = solve(i+1, 0)

            # allowed to end only after full trionic
            if trend == 3:
                take = nums[i]

            if i+1 < n:
                curr, nxt = nums[i], nums[i+1]

                if trend == 0 and nxt > curr:
                    take = max(take, curr + solve(i+1, 1))

                elif trend == 1:
                    if nxt > curr:
                        take = max(take, curr + solve(i+1, 1))
                    elif nxt < curr:
                        take = max(take, curr + solve(i+1, 2))

                elif trend == 2:
                    if nxt < curr:
                        take = max(take, curr + solve(i+1, 2))
                    elif nxt > curr:
                        take = max(take, curr + solve(i+1, 3))

                elif trend == 3 and nxt > curr:
                    take = max(take, curr + solve(i+1, 3))

            dp[i][trend] = max(take, skip)
            return dp[i][trend]

        return solve(0, 0)
