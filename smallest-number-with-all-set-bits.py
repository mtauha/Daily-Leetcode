class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = bin(n)[2:]

        result = ''.join('1' if b == '0' else b for b in binary)
        
        return int(result, 2)
