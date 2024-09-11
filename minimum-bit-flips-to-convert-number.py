class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
            A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.
            For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
            Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
        """
      
        count = 0
        source_bin = bin(start).lstrip("0b")
        target_bin = bin(goal).lstrip("0b")

        while len(source_bin) < len(target_bin):
            source_bin = "0" + source_bin 
        while len(source_bin) > len(target_bin):
            target_bin = "0" + target_bin

        for i in range(len(source_bin)):
            if target_bin[i] != source_bin[i]:
                count += 1
        
        return count
