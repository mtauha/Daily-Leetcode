"""Description:
    You are given a binary array nums and an integer k.

    A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

    Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

    A subarray is a contiguous part of an array.
"""


class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        length = len(nums)
        if not 1 in nums and length == k:
            return 1
        flip_count = 0
        flip_indicator = [0] * length
        current_flips = 0

        for i in range(length):
            if i >= k:
                current_flips ^= flip_indicator[i - k]

            if nums[i] == current_flips:
                if i + k > length:
                    return -1

                flip_count += 1
                current_flips ^= 1
                flip_indicator[i] = 1

        return flip_count
