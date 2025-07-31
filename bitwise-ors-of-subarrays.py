class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        curr = {0}

        for num in arr:
            curr = {num | OR for OR in curr} | {num}
            ans |= curr

        return len(ans)
