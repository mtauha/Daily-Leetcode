'''Description:
    You are given a string s and two integers x and y. You can perform two types of operations any number of times.

    Remove substring "ab" and gain x points.
    For example, when removing "ab" from "cabxbae" it becomes "cxbae".
    Remove substring "ba" and gain y points.
    For example, when removing "ba" from "cabxbae" it becomes "cabxe".
    Return the maximum points you can gain after applying the above operations on s.
'''


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if not s:
            return 0

        def remove(s, first, second, points):
            stack = []
            total = 0

            for char in s:
                if char == second and stack and stack[-1] == first:
                    total += points
                    stack.pop()
                else:
                    stack.append(char)

            return "".join(stack), total

        if x >= y:
            s, ans1 = remove(s, "a", "b", x)
            s, ans2 = remove(s, "b", "a", y)
        else:
            s, ans1 = remove(s, "b", "a", y)
            s, ans2 = remove(s, "a", "b", x)

        return ans1 + ans2


sol = Solution()
