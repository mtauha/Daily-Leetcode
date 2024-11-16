class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
            You are given an array of integers nums of length n and a positive integer k.

            The power of an array is defined as:

            Its maximum element if all of its elements are consecutive and sorted in ascending order.
            -1 otherwise.
            You need to find the power of all 
            subarrays
            of nums of size k.

            Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].
        """
        length = len(nums)
        result = [-1] * (length - k + 1)
        index_deque = collections.deque()

        for current_index in range(length):
            if index_deque and index_deque[0] < current_index - k + 1:
                index_deque.popleft()
            if (
                index_deque
                and nums[current_index] != nums[current_index - 1] + 1
            ):
                index_deque.clear()

            index_deque.append(current_index)

            if current_index >= k - 1:
                if len(index_deque) == k:
                    result[current_index - k + 1] = nums[index_deque[-1]]
                else:
                    result[current_index - k + 1] = -1

        return result
