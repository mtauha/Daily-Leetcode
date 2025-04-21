class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        """
            Notes:
                prefix: array just tells how much current element deviates from the first one
        """
        summ = sum(differences)
        prefix = [0]

        for d in differences:
            prefix.append(prefix[-1] + d)

        min_val = min(prefix) # Checks how far the deviation goes in negative side of first element
        max_val = max(prefix) # Checks how far the deviation goes in positive side of first element 

        return max(0, (upper - max_val) - (lower - min_val)  + 1) # Restrict the domain size between [lower, upper] using min max values
