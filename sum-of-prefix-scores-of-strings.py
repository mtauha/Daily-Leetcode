class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0


class Solution:
    def __init__(self):
        self.root = trie_node()

    def insert(self, word):
        node = self.root
        for c in word:
            if node.next[ord(c) - ord("a")] is None:
                node.next[ord(c) - ord("a")] = trie_node()
            node.next[ord(c) - ord("a")].cnt += 1
            node = node.next[ord(c) - ord("a")]

    def count(self, s):
        node = self.root
        ans = 0
        for c in s:
            ans += node.next[ord(c) - ord("a")].cnt
            node = node.next[ord(c) - ord("a")]
        return ans

    def sumPrefixScores(self, words):
        """
            You are given an array words of size n consisting of non-empty strings.
            We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].
            For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
            Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].
            Note that a string is considered as a prefix of itself.
        """
        N = len(words)
        for i in range(N):
            self.insert(words[i])
        scores = [0] * N
        for i in range(N):
            scores[i] = self.count(words[i])
        return scores
