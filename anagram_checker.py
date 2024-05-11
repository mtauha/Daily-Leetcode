class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [*s]
        t_list = [*t]

        return sorted(t_list) == sorted(s_list)


class Solution2:
    def isAnagram(self, s:str, t:str)->bool:
        from collections import Counter
        return Counter(s) == Counter(t)


sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))

sol2 = Solution2()
print(sol.isAnagram(s,t))
