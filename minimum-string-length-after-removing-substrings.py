class Solution:
    def minLength(self, s: str) -> int:
        """
          You are given a string s consisting only of uppercase English letters.
          You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.
          
          Return the minimum possible length of the resulting string that you can obtain.
          
          Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.
        """
        stack = []

        for curr in s:
            if not stack:
                stack.append(curr)
                continue
            
            if curr == "B" and stack[-1] == "A":
                stack.pop()
            elif curr == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(curr)
        
        return len(stack)
