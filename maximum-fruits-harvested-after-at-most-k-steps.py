class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # Sliding Window Approach:

        left = 0 # Left index for the window
        max_fruits = 0 # This is your answer
        n = len(fruits) # Number of fruits
        total = 0 # Sum of all fruits in the window

        for right in range(n):
            # Record all the fruits in [left...right]
            total += fruits[right][1]

            while left <= right:
                # Extract left and right positions
                l_pos, r_pos = fruits[left][0], fruits[right][0]

                # This is optimization step to count minimum number of steps
                # by checking steps when we go [left...right] or [right...left] 
                min_steps = min(
                    abs(startPos - l_pos) + (r_pos - l_pos), # [left...right]
                    abs(startPos - r_pos) + (r_pos - l_pos)  # [right...left]
                )

                # Check if Minimum number of steps still lie under contraint k
                if min_steps <= k:
                    # If yes then break and go update the answer at `UPDATE_ANS`
                    break
                else:
                    # Otherwise increment the left pointer and remove fruits at 
                    # that position
                    total -= fruits[left][1]
                    left += 1
            
            # `UPDATE_ANS`:
            max_fruits = max(max_fruits, total)
        
        return max_fruits
