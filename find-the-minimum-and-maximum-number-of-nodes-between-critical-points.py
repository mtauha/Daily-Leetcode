"""Description:
    A critical point in a linked list is defined as either a local maxima or a local minima.

    A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

    A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

    Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

    Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        pointer = head.next
        prev = head

        node_no = 0
        Next = pointer.next
        distances = []

        while Next:
            if (
                pointer.val > prev.val
                and pointer.val > Next.val
                or pointer.val < prev.val
                and pointer.val < Next.val
            ):
                distances.append(node_no)

            prev = pointer
            pointer = pointer.next
            Next = pointer.next
            node_no += 1

        n = len(distances)
        if n < 2:
            return [-1, -1]

        min_distance = float('inf')
        for i in range(1, n):
            min_distance = min(min_distance, distances[i] - distances[i-1])

        max_distance = distances[-1] - distances[0]

        return [min_distance, max_distance]


def list_to_linked_list(lst):
    # Edge case: if the input list is empty, return None
    if not lst:
        return None

    # Initialize the head of the linked list with the first element of the list
    head = ListNode(lst[0])
    current = head

    # Iterate over the rest of the elements and create nodes
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


sol = Solution()


# Example usage:
head = [5, 3, 1, 2, 5, 1, 2]
head = list_to_linked_list(head)

print(sol.nodesBetweenCriticalPoints(head))
