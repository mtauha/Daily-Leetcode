class Solution:
    def findScore(self, nums: List[int]) -> int:
        """
            You are given an array nums consisting of positive integers.

            Starting with score = 0, apply the following algorithm:

            Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
            Add the value of the chosen integer to score.
            Mark the chosen element and its two adjacent elements if they exist.
            Repeat until all the array elements are marked.
            Return the score you get after applying the above algorithm.
        """
        n = len(nums)
        score = 0
        visited = defaultdict(bool)
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap,(num, i))
        
        while len(visited) < n:
            curr_num, curr_indx = heapq.heappop(heap)
            if visited[curr_indx]:
                continue
            visited[curr_indx] = True
            score += curr_num
            if curr_indx > 0 and curr_indx < n-1:
                visited[curr_indx-1], visited[curr_indx+1] = True, True
            elif curr_indx ==0 :
                visited[curr_indx+1] = True
            else:
                visited[curr_indx-1] = True


        return score
