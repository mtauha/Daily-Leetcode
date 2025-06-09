class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
            Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n]
        """
        def steps(prefix1, prefix2):
            # Initialize step variable
            step = 0

            while prefix1 <= n:
                # Find the number of digits between prefix1 and prefix2 
                # For Example, Number of digits between 1 and 2 bounded by n include all the numbers starting
                # from 1 that are less than or equal to n.
                step += min(n + 1, prefix2) - prefix1

                # Move to the next levels
                prefix1 *= 10
                prefix2 *= 10
            
            return step

        
        curr = 1
        k -= 1

        while k > 0:
            step = steps(curr, curr + 1)

            if step <= k:
                # If steps(Numbers between current digit and next digit) is less than k, 
                # Meaning we should skip this prefix and move to the next prefix 
                # For Example if current prefix was 1 then we should move to 2. 
                # To reduce computation we would decrement k by number of steps. 
                # Current will be incremented.
                curr += 1
                k -= step
            else:
                # We move to the next level until k is 0 to avoid extra computation
                curr *= 10
                k -= 1

        return curr
