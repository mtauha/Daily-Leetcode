# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        """
          Description:
            You are given two integers m and n, which represent the dimensions of a matrix.
            You are also given the head of a linked list of integers.
            Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
            Return the generated matrix.
        """
      
        matrix = [[-1] * n for _ in range(m)]
        left, right = 0, n
        top, bottom = 0, m
        direction = 0
        #             Right    Down    Left      Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while head:
            for i in range(left, right):
                if not head:
                    return matrix
                matrix[top][i] = head.val
                head = head.next
            top += 1

            for i in range(top, bottom):
                if not head:
                    return matrix
                matrix[i][right - 1] = head.val
                head = head.next
            right -= 1

            for i in range(right -1, left -1, -1):
                if not head:
                    return matrix
                matrix[bottom - 1][i] = head.val
                head = head.next
            bottom -= 1
            
            
            for i in range(bottom - 1, top - 1, -1):
                if not head:
                    return matrix
                matrix[i][left] = head.val
                head = head.next
            left += 1

        return matrix
            
