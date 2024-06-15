loads, stdin = input(), input()
class Solution:
    pass

#* Copy From here:

if __name__ == "__main__":
    sol = Solution()
    with open("user.out", "w") as f:
        for k, w, profits, capital in zip(
            map(loads, stdin), map(loads, stdin), map(loads, stdin), map(loads, stdin)
        ):
            print(sol.findMaximizedCapital(k, w, profits, capital), file=f)
    exit()
