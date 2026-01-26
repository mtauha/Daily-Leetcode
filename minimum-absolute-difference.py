class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        min_diff = 10**6 + 1
        ans = []

        for i in range(1, n):
            min_diff = min(min_diff, abs(arr[i] - arr[i - 1]))
        
        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                ans.append([arr[i-1], arr[i]])
        
        return ans
