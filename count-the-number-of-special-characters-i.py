class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        word_set = set(word)
        visited = []

        for w in word_set:
            visited.append(w)
            if chr(ord(w) + 32) in visited or chr(ord(w) - 32) in visited:
                ans += 1
        
        return ans
