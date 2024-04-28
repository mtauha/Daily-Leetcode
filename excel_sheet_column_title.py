class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        if columnNumber == 0:
            return "A"
        elif columnNumber <= 26:
            return chr(65 + (columnNumber - 1))

        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            result = chr(65 + remainder) + result
            columnNumber = (columnNumber - 1) // 26

        return result


solution = Solution()
print(solution.convertToTitle(2147483647))
