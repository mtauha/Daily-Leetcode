class Solution:
    def makeFancyString(self, s: str) -> str:
        """
            A fancy string is a string where no three consecutive characters are equal.
            Given a string s, delete the minimum possible number of characters from s to make it fancy.
            
            Return the final string after the deletion. It can be shown that the answer will always be unique.
        """
        if len(s) < 3:
            return s

        s_list = list(s)
        j = 2

        for i in range(2, len(s)):
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1

        return "".join(s_list[:j])

    def makeFancyString2(self, s: str) -> str:
        last = s[0]
        count = 1
        ans = s[0]

        for i in range(1, len(s)):
            if s[i] == last:
                count += 1
            else:
                count = 1
                last = s[i]
            
            if count < 3:
                ans += s[i]
        
        return ans
