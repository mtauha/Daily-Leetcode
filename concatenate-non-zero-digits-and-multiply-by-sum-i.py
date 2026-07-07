class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        num = str(n).replace("0", "")
        s = sum(int(i) for i in num)

        return int(num) * s
