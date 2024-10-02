class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
            Given an array of integers arr, replace each element with its rank.

            The rank represents how large the element is. The rank has the following rules:
            
            Rank is an integer starting from 1.
            The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
            Rank should be as small as possible.
        """
        num_to_indices = {k: [] for k in sorted(set(arr))}

        for i, num in enumerate(arr):
            num_to_indices[num].append(i)

        rank = 1
        for num in num_to_indices.keys():
            for index in num_to_indices[num]:
                arr[index] = rank
            rank += 1

        return arr
