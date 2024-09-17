class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
            A sentence is a string of single-space separated words where each word consists only of lowercase letters.
            A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
            Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
        """
      
        list1, list2 = s1.split(' '), s2.split(' ')
        counter1 = Counter(list1)
        counter2 = Counter(list2)

        ans = []

        for word in list1:
            if counter1[word] == 1 and word not in list2:
                ans.append(word)

        for word in list2:
            if counter2[word] == 1 and word not in list1:
                ans.append(word)

        return ans
