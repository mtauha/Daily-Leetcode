"""Description:
    You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

    For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

    Return the head of the modified linked list.

"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(0)
        pointer = dummy
        summ = 0
        head = head.next

        while head:
            if head.val == 0:
                if count > 0:
                    pointer.next = ListNode(summ)
                    pointer = pointer.next
                    summ, count = 0, 0
            else:
                summ += head.val
                count += 1

            head = head.next

        return dummy.next
