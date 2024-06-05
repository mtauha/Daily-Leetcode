"""Description:
    Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
"""

from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        def common(word1:str, word2:str):
            counter1 = Counter(word1)
            counter2 = Counter(word2)

            common_chars = []

            for char in word1:
                if counter1[char] > 0 and counter2[char] > 0:
                    common_chars.append(char)
                    counter1[char] -= 1
                    counter2[char] -= 1
            
            return common_chars
        

        Common = []

        for i in range(len(words)-1):
            if i == 0:
                Common = common(words[i], words[i+1])
            else:
                Common = common(Common, common(words[i], words[i+1]))

        return Common


sol = Solution()
string = ["bella", "label", "roller"]
print(sol.commonChars(string))
