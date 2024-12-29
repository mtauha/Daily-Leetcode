class Solution:
    def numWays(self, words, target):
        """
            You are given a list of strings of the same length words and a string target.

            Your task is to form target using the given words under the following rules:

            target should be formed from left to right.
            To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
            Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
            Repeat the process until you form the string target.
            Notice that you can use multiple characters from the same string in words provided the conditions above are met.

            Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
        """

        dp = [[-1] * len(target) for _ in range(len(words[0]))]
        char_frequency = [[0] * 26 for _ in range(len(words[0]))]

        # Store the frequency of every character at every index.
        for i in range(len(words)):
            for j in range(len(words[0])):
                character = ord(words[i][j]) - 97
                char_frequency[j][character] += 1
        return self.__get_words(words, target, 0, 0, dp, char_frequency)

    def __get_words(
        self, words, target, words_index, target_index, dp, char_frequency
    ):
        if target_index == len(target):
            return 1
        if (
            words_index == len(words[0])
            or len(words[0]) - words_index < len(target) - target_index
        ):
            return 0

        if dp[words_index][target_index] != -1:
            return dp[words_index][target_index]

        count_ways = 0
        cur_pos = ord(target[target_index]) - 97
        # Don't match any character of target with any word.
        count_ways += self.__get_words(
            words, target, words_index + 1, target_index, dp, char_frequency
        )
        # Multiply the number of choices with getWords and add it to count.
        count_ways += char_frequency[words_index][cur_pos] * self.__get_words(
            words, target, words_index + 1, target_index + 1, dp, char_frequency
        )

        dp[words_index][target_index] = count_ways % 1000000007
        return dp[words_index][target_index]
