class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        sm = 0
        cnt = 0
        bits = k.bit_length() # Number of bits in which k is represented
        for i, ch in enumerate(s[::-1]):
            if ch == "1":
                # Add 1 only if the addition doesn't exceed k
                if i < bits and sm + (1 << i) <= k: # Checks if index is less than bit length and adding 1 to the binary doesn't exceed k
                    sm += 1 << i # Add 1 to the binary
                    cnt += 1 # Increment length
            else:
                # Always add 0
                cnt += 1 # Increment length

        return cnt
