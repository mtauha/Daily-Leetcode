class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def four_divisor_sum(n: int) -> int:
            divs = set()
            i = 1
            while i * i <= n:
                if n % i == 0:
                    divs.add(i)
                    divs.add(n // i)
                    if len(divs) > 4:
                        return 0
                i += 1
            return sum(divs) if len(divs) == 4 else 0

        ans = 0
        for num in nums:
            ans += four_divisor_sum(num)

        return ans
