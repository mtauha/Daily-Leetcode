class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
            You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

            We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

            Return the largest number of chunks we can make to sort the array.
        """
        n = len(arr)
        stack = []

        for i in range(n):
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)
        
        return len(stack)
