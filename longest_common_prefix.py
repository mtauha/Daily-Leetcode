"""Description:
    Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".    
"""

class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs is None:
            return ""
        elif len(strs) == 1:
            return strs[0]
        elif "" in strs:
            return ""

        prefix = ""
        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return prefix
                
            prefix+=char
        
        return prefix


sol = Solution()
string = ["", "", ""]
print(sol.longestCommonPrefix(string))
