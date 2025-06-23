class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def Base(n: int, b: int):
            if n == 0:
                return "0"
            digits = []
            while n > 0:
                digits.append(str(n % b))
                n //= b
            
            return ''.join(reversed(digits))
        
        def yield_palindrome():
            for num in range(1, 10):
                yield num

            length = 2
            while True:
                half_len = (length + 1) // 2
                for num in range(10**(half_len-1), 10**half_len):
                    s = str(num)
                    if length % 2 == 0:
                        yield int(s + s[::-1])
                    else:
                        yield int(s + s[-2::-1])
                length += 1

        
        def is_palindrome(s):
            return s == s[::-1]
        
        ans = 0
        count = 0

        for num in yield_palindrome():
            if is_palindrome(Base(num, k)):
                ans += num
                count += 1
                if count == n:
                    return ans 
