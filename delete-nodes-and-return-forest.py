'''Description:

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        to_delete_set = set(to_delete)
        remaining_nodes = []

        def remove(node):
            if not node:
                return None
            
            node.left = remove(node.left)
            node.right = remove(node.right)

            if node.val in to_delete_set:
                if node.left:
                    remaining_nodes.append(node.left)
                if node.right:
                    remaining_nodes.append(node.right)
                return None
            
            return node
        
        root = remove(root)

        if root:
            remaining_nodes.append(root)
        
        return remaining_nodes


sol = Solution()
