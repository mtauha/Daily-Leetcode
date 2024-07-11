"""Description:
    You are given a string s that consists of lower case English letters and brackets.

    Reverse the strings in each pair of matching parentheses, starting from the innermost one.

    Your result should not contain any brackets.
"""


"""Complexity O(n^2)"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in s:
            if i != ")":
                stack.append(i)
            else:
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())

                stack.pop()
                stack.extend(temp)

        return "".join(stack)


"""Complexity O(n)"""
class Solution2:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        hash_map = {}

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                j = stack.pop()
                hash_map[i] = j
                hash_map[j] = i

        ans = []
        itr, direction = 0, 1

        while itr < len(s):
            if s[itr] == "(" or s[itr] == ")":
                itr = hash_map[itr]
                direction = -direction
            else:
                ans.append(s[itr])

            itr += direction

        return "".join(ans)


sol = Solution()
