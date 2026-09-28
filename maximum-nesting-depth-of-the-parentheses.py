class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = curr = 0
        itr, n = 0, len(s)

        for char in s:
            if char == "(":
                curr += 1
            if char == ")":
                curr -= 1
            count = max(curr, count)
            
        return count
