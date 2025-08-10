class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_dig(num):
            count = [0]*10
            
            while num > 0:
                count[num%10] += 1
                num //= 10
            
            return count

        if n > 0 and (n & (n-1)) == 0:
            return True
        
        n_count = count_dig(n)

        for i in range(30):
            if count_dig(1 << i) == n_count:
                return True
        
        return False
