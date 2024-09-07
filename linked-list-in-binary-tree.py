class Solution:
    def isSubPath(
        self, head: Optional[ListNode], root: Optional[TreeNode]
    ) -> bool:
        """
          Given a binary tree root and a linked list with head as the first node. 
          Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
          In this context downward path means a path that starts at some node and goes downwards.
        """
        if root is None:
            return False
        return self._check_path(root, head)

    def _check_path(
        self, node: Optional[TreeNode], head: Optional[ListNode]
    ) -> bool:
        if node is None:
            return False
        if self._dfs(node, head):
            return True  # If a matching path is found

        # Recursively check left and right subtrees
        return self._check_path(node.left, head) or self._check_path(
            node.right, head
        )

    def _dfs(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if head is None:
            return True  # All nodes in the list matched
        if node is None:
            return False  # Reached end of tree without matching all nodes
        if node.val != head.val:
            return False  # Value mismatch
        return self._dfs(node.left, head.next) or self._dfs(
            node.right, head.next
        )
