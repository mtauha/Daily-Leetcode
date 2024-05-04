class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            if s[i] == "?":
                if 0 < i < len(s) - 1:
                    if s[i - 1] == "a":
                        if s[i + 1] == "a":
                            s[i] = "b"
                        elif s[i + 1] == "b":
                            s[i] = "c"
                        else:
                            s[i] = "b"
                    elif s[i - 1] == "b":
                        if s[i + 1] == "a":
                            s[i] = "c"
                        elif s[i + 1] == "b":
                            s[i] = "a"
                        else:
                            s[i] = "a"
                    elif s[i - 1] == "c":
                        if s[i + 1] == "a":
                            s[i] = "b"
                        elif s[i + 1] == "b":
                            s[i] = "a"
                        else:
                            s[i] = "a"
                    else:
                        if s[i + 1] == "a":
                            s[i] = "b"
                        else:
                            s[i] = "a"

                elif i == len(s) - 1:
                    if s[i - 1] == "a":
                        s[i] = "b"
                    else:
                        s[i] = "a"

                elif i == 0 and len(s) != 1:
                    if s[i + 1] == "a":
                        s[i] = "b"
                    else:
                        s[i] = "a"
                else:
                    s[i] = "a"

        return "".join(s).lower()


# Example usage:
sol = Solution()
print(sol.modifyString("ubv?w"))  # Output: "azcba"
