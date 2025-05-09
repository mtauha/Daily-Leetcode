class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
            Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

            Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
        """
        # Variables to track the best indices for one, two, and three subarray configurations
        best_single_start = 0
        best_double_start = [0, k]
        best_triple_start = [0, k, k * 2]

        # Compute the initial sums for the first three subarrays
        current_window_sum_single = sum(nums[:k])
        current_window_sum_double = sum(nums[k : k * 2])
        current_window_sum_triple = sum(nums[k * 2 : k * 3])

        # Track the best sums found so far
        best_single_sum = current_window_sum_single
        best_double_sum = current_window_sum_single + current_window_sum_double
        best_triple_sum = (
            current_window_sum_single
            + current_window_sum_double
            + current_window_sum_triple
        )

        # Sliding window pointers for the subarrays
        single_start_index = 1
        double_start_index = k + 1
        triple_start_index = k * 2 + 1

        # Slide the windows across the array
        while triple_start_index <= len(nums) - k:
            # Update the sums using the sliding window technique
            current_window_sum_single = (
                current_window_sum_single
                - nums[single_start_index - 1]
                + nums[single_start_index + k - 1]
            )
            current_window_sum_double = (
                current_window_sum_double
                - nums[double_start_index - 1]
                + nums[double_start_index + k - 1]
            )
            current_window_sum_triple = (
                current_window_sum_triple
                - nums[triple_start_index - 1]
                + nums[triple_start_index + k - 1]
            )

            # Update the best single subarray start index if a better sum is found
            if current_window_sum_single > best_single_sum:
                best_single_start = single_start_index
                best_single_sum = current_window_sum_single

            # Update the best double subarray start indices if a better sum is found
            if current_window_sum_double + best_single_sum > best_double_sum:
                best_double_start[0] = best_single_start
                best_double_start[1] = double_start_index
                best_double_sum = current_window_sum_double + best_single_sum

            # Update the best triple subarray start indices if a better sum is found
            if current_window_sum_triple + best_double_sum > best_triple_sum:
                best_triple_start[0] = best_double_start[0]
                best_triple_start[1] = best_double_start[1]
                best_triple_start[2] = triple_start_index
                best_triple_sum = current_window_sum_triple + best_double_sum

            # Move the sliding windows forward
            single_start_index += 1
            double_start_index += 1
            triple_start_index += 1

        # Return the starting indices of the three subarrays with the maximum sum
        return best_triple_start
