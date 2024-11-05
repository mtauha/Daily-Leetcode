class Solution:
    def minChanges(self, s: str) -> int:
        """
            You are given a 0-indexed binary string s having an even length.

            A string is beautiful if it's possible to partition it into one or more substrings such that:
            
            Each substring has an even length.
            Each substring contains only 1's or only 0's.
            You can change any character in s to 0 or 1.
            
            Return the minimum number of changes required to make the string s beautiful.
        """
        current = s[0]
        consecutive_count = 0
        min_changes = 0

        for char in s:
            if char == current:
                consecutive_count += 1
                continue
            
            if consecutive_count % 2 == 0:
                consecutive_count = 1
            else:
                consecutive_count = 0
                min_changes += 1
            
            current = char
        
        return min_changes
