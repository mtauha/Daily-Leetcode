class Solution(object):
    def minOperations(self, s, k):
        zero = 0
        len_s = len(s)

        for i in range(len_s):
            zero += ~ord(s[i]) & 1
        

        if zero == 0:
            return 0

        if len_s == k:
            return ((1 if zero == len_s else 0) << 1) - 1

        base = len_s - k

        odd = max(
            int(math.ceil(float(zero) / k)),
            int(math.ceil(float(len_s - zero) / base))
        )

        odd += ~odd & 1

        even = max(
            int(math.ceil(float(zero) / k)),
            int(math.ceil(float(zero) / base))
        )

        even += even & 1

        res = float('inf')

        if (k & 1) == (zero & 1):
            res = min(res, odd)

        if (~zero & 1) == 1:
            res = min(res, even)

        return -1 if res == float('inf') else res
