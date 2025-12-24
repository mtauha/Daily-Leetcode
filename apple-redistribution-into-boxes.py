class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        ans = 0
        total = sum(apple)

        for i in capacity:
            if total <= 0:
                break
            total -= i
            ans += 1
        
        return ans
