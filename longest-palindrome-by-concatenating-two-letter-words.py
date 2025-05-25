class Solution:
    def longestPalindrome(self, words):
        count = [[0] * 26 for _ in range(26)]
        length = 0

        for word in words:
            a = ord(word[0]) - ord('a')
            b = ord(word[1]) - ord('a')

            if count[b][a] > 0:
                length += 4
                count[b][a] -= 1
            else:
                count[a][b] += 1

        for i in range(26):
            if count[i][i] > 0:
                length += 2
                break

        return length
