class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        """
            Description:
                  Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
                  The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
                  The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
                  Return an array of the k parts.
        """
      
        ans = [None] * k

        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next

        split_size = size // k
        num_remaining_parts = size % k

        current = head
        prev = current
        for i in range(k):
            new_part = current
            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1

            j = 0
            while j < current_size:
                prev = current
                if current is not None:
                    current = current.next
                j += 1

            if prev is not None:
                prev.next = None

            ans[i] = new_part

        return ans
