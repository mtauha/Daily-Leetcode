class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = ""
        dictionary = defaultdict(lambda: "?")
        n = len(s)
        i = 0

        for key, value in knowledge:
            dictionary[key] = value
        
        while i < n:
            if s[i] == '(':
                i += 1
                key = ""

                while s[i] != ")":
                    key += s[i]
                    i += 1

                ans += dictionary[key]
            else:
                ans += s[i]
            i += 1
        
        return ans
            
