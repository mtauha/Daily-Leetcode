class Solution:
    def minimumSteps(self, s: str) -> int:
        """
            There are n balls on a table, each ball has a color black or white.
            You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.
            In each step, you can choose two adjacent balls and swap them.

            Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.
        """
        black_count = 0
        score = 0

        for i in s:
            if i == "0":
                score += black_count
            else:
                black_count += 1
        
        return score
