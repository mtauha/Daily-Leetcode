"""Description:
    Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
"""

import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(first, first+groupSize):
                if card_count[i] == 0:
                    return False

                card_count[i] -= 1

                if card_count[i] == 0:
                    if i != min_heap[0]:
                        return False

                    heapq.heappop(min_heap)

        return True


sol = Solution()
hand = [1, 2, 3, 4, 5]
groupSize = 4

print(sol.isNStraightHand(hand, groupSize))
