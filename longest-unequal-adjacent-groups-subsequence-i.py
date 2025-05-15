class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        n = len(words)
        prev = groups[0]
        ans.append(words[0])

        for i in range(1, n):
            if prev == groups[i]:
                continue
            ans.append(words[i])
            prev = groups[i]

        return ans
