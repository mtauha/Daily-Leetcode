class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dp = defaultdict(lambda: defaultdict(int))
        ans = 0

        for i, num in enumerate(nums):
            mod_i = i % k

            if num in dp:
                for mod_j, count in dp[num].items():
                    if (mod_i * mod_j) % k == 0:
                        ans += count

            dp[num][mod_i] += 1 
        
        print({i[0]: dict(i[1]) for i in dict(dp).items()})
        return ans
