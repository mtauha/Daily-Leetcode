"""Description:
    Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

    A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node: TreeNode):
            if not node:
                return []
            return (
                inorder_traversal(node.left)
                + [node.val]
                + inorder_traversal(node.right)
            )

        elements = inorder_traversal(root)

        def make_tree(tree):
            if not tree:
                return None
            mid = len(tree) // 2
            root = TreeNode(tree[mid])
            root.left = make_tree(tree[:mid])
            root.right = make_tree(tree[mid + 1 :])
            return root

        return make_tree(elements)
