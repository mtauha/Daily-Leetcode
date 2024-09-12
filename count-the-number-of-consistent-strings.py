class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
            You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
            Return the number of consistent strings in the array words.
        """
        count = 0
        for word in words:
            for i in word:
                if i not in allowed:
                    count += 1

        
        return len(words) - count
        
