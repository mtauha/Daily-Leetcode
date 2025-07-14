# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length = -1
        temp = head
        ans = 0

        while temp:
            length += 1
            temp = temp.next
        
        del temp
        while head:
            ans += 2**length*head.val
            length -= 1
            head = head.next
        
        return ans
