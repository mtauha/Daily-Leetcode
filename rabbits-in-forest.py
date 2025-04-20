class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0

        for key, value in freq.items():
           group_size = key + 1
           groups = ceil(value / group_size)
           total += groups * group_size

        return total 

