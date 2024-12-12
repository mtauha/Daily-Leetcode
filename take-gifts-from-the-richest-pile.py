class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
            You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

            Choose the pile with the maximum number of gifts.
            If there is more than one pile with the maximum number of gifts, choose any.
            Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
            Return the number of gifts remaining after k seconds.
        """
        heap = [-i for i in gifts]
        heapq.heapify(heap)
        ans = 0

        for _ in range(k):
            gift = -heapq.heappop(heap)
            heapq.heappush(heap, -math.floor(math.sqrt(gift)))
        
        while heap:
            ans -= heapq.heappop(heap)
        
        return ans
        
