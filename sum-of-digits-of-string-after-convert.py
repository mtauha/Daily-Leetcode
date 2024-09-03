class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
            You are given a string s consisting of lowercase English letters, and an integer k.
            First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
            For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
            
            Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
            Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
            Transform #2: 17 ➝ 1 + 7 ➝ 8
            
            Return the resulting integer after performing the operations described above.
        """
        numeric_string = ""
        for ch in s:
            numeric_string += str(ord(ch) - ord("a") + 1)

        while k > 0:
            digit_sum = 0
            for digit in numeric_string:
                digit_sum += int(digit)
            numeric_string = str(digit_sum)
            k -= 1

        return int(numeric_string)
