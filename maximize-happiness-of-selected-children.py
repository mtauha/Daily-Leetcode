class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0

        for child, happy in enumerate(happiness):
            if k <= 0:
                break
            ans += happy - child if happy - child > 0 else 0
            k -= 1
        
        return ans
