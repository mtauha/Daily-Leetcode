# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None, 0
            
            left, l_height = dfs(node.left)
            right, r_height = dfs(node.right)

            if l_height == r_height:
                return node, l_height + 1
            elif l_height > r_height:
                return left, l_height + 1
            else:
                return right, r_height + 1

        return dfs(root)[0]
