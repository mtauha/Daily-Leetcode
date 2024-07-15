"""Description:
    You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

    If isLefti == 1, then childi is the left child of parenti.
    If isLefti == 0, then childi is the right child of parenti.
    Construct the binary tree described by descriptions and return its root.

    The test cases will be generated such that the binary tree is valid.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:

        tree = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in tree:
                tree[parent] = TreeNode(parent)
            if child not in tree:
                tree[child] = TreeNode(child)
            if isLeft:
                tree[parent].left = tree[child]
            else:
                tree[parent].right = tree[child]

            children.add(child)

        root = None

        for node in tree.values():
            if node.val not in children:
                root = node
                break

        return root


sol = Solution()
