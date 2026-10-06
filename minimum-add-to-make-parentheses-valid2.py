class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_bracketts = 0
        min_add_required = 0

        for c in s:
            if c == "(":
                open_bracketts += 1
            else:
                if open_bracketts > 0:
                    open_bracketts -= 1
                else:
                    min_add_required += 1
        
        return min_add_required + open_bracketts
