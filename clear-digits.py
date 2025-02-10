class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s)-1:
            if s[i+1].isdigit():
                del s[i+1]
                del s[i]
                i -= 1
            else:
                i+=1
        
        return "".join(s)
            
