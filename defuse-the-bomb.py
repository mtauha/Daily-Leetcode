class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
            You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

            To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

            If k > 0, replace the ith number with the sum of the next k numbers.
            If k < 0, replace the ith number with the sum of the previous k numbers.
            If k == 0, replace the ith number with 0.
            As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

            Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
        """
        result = [0 for _ in range(len(code))]
        if k == 0:
            return result
        start, end, window_sum = 1, k, 0
        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1
        for i in range(start, end + 1):
            window_sum += code[i]
        for i in range(len(code)):
            result[i] = window_sum
            window_sum -= code[start % len(code)]
            window_sum += code[(end + 1) % len(code)]
            start += 1
            end += 1
        return result
