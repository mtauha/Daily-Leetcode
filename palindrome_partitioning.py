class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> list[list[str]]:
        def backtrack(start, path):
            if start == len(s):
                result.append(path)
                return
            for end in range(start + 1, len(s) + 1):
                if self.isPalindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result


sol = Solution()
print(sol.partition("illi"))
