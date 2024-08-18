"""Description:
  An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

  Given an integer n, return the nth ugly number.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = set()
        ugly.add(1)

        for i in range(n):
            current_ugly = min(ugly)
            ugly.remove(current_ugly)

            ugly.add(current_ugly*2)
            ugly.add(current_ugly*3)
            ugly.add(current_ugly*5)
        
        return current_ugly
