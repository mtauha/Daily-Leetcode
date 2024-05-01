class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k == 0:
            return [0]*len(code)
        decrypt = code
        code = code * 2
        for i in range(len(decrypt)):
            if k > 0:
                decrypt[i] = sum(code[i + 1 : i + k + 1])
            else:
                decrypt[i] = sum(code[i + len(decrypt) + k : i + len(decrypt)])
        return decrypt


solution = Solution()
code = [10, 5, 7, 7, 3, 2, 10, 3, 6, 9, 1, 6]
k = -4
print(solution.decrypt(code=code, k=k))
