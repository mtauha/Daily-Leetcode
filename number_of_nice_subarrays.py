"""Description:
    Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

    Return the number of nice sub-arrays.
"""

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        nums = [1 if num % 2 == 1 else 0 for num in nums]

        prefix_sum = 0
        prefix_count = {0: 1}
        result = 0

        for num in nums:
            prefix_sum += num

            # * Checks if number of odds til index of 'num' is equal or greater than k. If it
            # * is greater than then check if it is present in 'prefix_count' hash map. If it
            # * is not present in hashmap then add it to the hashmap else add the answer to
            # * the result.
            if prefix_sum-k in prefix_count:
                result += prefix_count[prefix_sum-k]

            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                # * This is where you add
                prefix_count[prefix_sum] = 1

        return result

sol = Solution()
nums = [1, 1, 2, 1, 1]
k = 3
print(sol.numberOfSubarrays(nums, k))
