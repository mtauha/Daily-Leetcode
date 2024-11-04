class Solution:
    def compressedString(self, word: str) -> str:
        """
            Given a string word, compress it using the following algorithm:

            Begin with an empty string comp. While word is not empty, use the following operation:
            Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
            Append the length of the prefix followed by c to comp.
            Return the string comp.
        """
        comp = ""
        def consecutive_count(word):
            char = word[0]
            i = 0
            count = 0
            while i < len(word) and word[i] == char:
                if count == 9:
                    return 9, i
                count += 1
                i += 1
            
            return count, i
        
        i = 0
        while i < len(word):
            count, next_index = consecutive_count(word[i:])
            comp += str(count) + word[i]
            i += next_index

        return comp
        
        
