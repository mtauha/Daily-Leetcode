class Solution:
    def maximumSwap(self, num: int) -> int:
        """
            You are given an integer num. You can swap two digits at most once to get the maximum valued number.
            Return the maximum valued number you can get.
        """
        num_list = list(str(num))
        
        last = {int(d): i for i, d in enumerate(num_list)}
        
        for i, digit in enumerate(num_list):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(''.join(num_list))
        
        return num