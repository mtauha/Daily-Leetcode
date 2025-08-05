class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        filled = set()
        n = len(fruits)
        ans = n

        for i in range(n):
            for j in range(n):
                if j not in filled and fruits[i] <= baskets[j]:
                    filled.add(j)
                    ans -= 1
                    break

        return ans 
