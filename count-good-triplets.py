class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        
        for k in range(len(arr)):
            for j in range(k):
                for i in range(j):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[k] - arr[i]) <= c:
                        ans += 1
        return ans
