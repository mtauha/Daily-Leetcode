# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      """
        Given the root of a binary tree, return the postorder traversal of its nodes' values.
      """
        ans = []
        def traversal(node):
            if not node:
                return
            
            traversal(node.left)
            traversal(node.right)
            ans.append(node.val)
        
        traversal(root)
        return ans
