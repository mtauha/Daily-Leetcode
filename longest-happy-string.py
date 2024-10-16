class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
          A string s is called happy if it satisfies the following conditions:

          s only contains the letters 'a', 'b', and 'c'.
          s does not contain any of "aaa", "bbb", or "ccc" as a substring.
          s contains at most a occurrences of the letter 'a'.
          s contains at most b occurrences of the letter 'b'.
          s contains at most c occurrences of the letter 'c'.
          Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
          
          A substring is a contiguous sequence of characters within a string.
        """
        curra, currb, currc = 0, 0, 0
        total_iterations = a + b + c
        result = []

        for i in range(total_iterations):
            if (a >= b and a >= c and curra != 2) or (
                a > 0 and (currb == 2 or currc == 2)
            ):
                result.append("a")
                a -= 1
                curra += 1
                currb = 0
                currc = 0
            elif (b >= a and b >= c and currb != 2) or (
                b > 0 and (currc == 2 or curra == 2)
            ):
                result.append("b")
                b -= 1
                currb += 1
                curra = 0
                currc = 0
            elif (c >= a and c >= b and currc != 2) or (
                c > 0 and (curra == 2 or currb == 2)
            ):
                result.append("c")
                c -= 1
                currc += 1
                curra = 0
                currb = 0

        return "".join(result)
