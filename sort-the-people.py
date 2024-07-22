"""Description:
    You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

    For each index i, names[i] and heights[i] denote the name and height of the ith person.

    Return names sorted in descending order by the people's heights.
"""

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:

        people = list(zip(names, heights))
        people.sort(key=lambda x: x[1], reverse=True)
        return [i[0] for i in people]


sol = Solution()
