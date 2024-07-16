"""Description:
    You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

    Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

    'L' means to go from a node to its left child node.
    'R' means to go from a node to its right child node.
    'U' means to go from a node to its parent node.
    Return the step-by-step directions of the shortest path from node s to node t.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:

        def findLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        def findPath(root, target, path):
            if not root:
                return False
            if root.val == target:
                return True
            path.append("L")
            if findPath(root.left, target, path):
                return True
            path.pop()
            path.append("R")
            if findPath(root.right, target, path):
                return True
            path.pop()
            return False

        lca = findLCA(root, startValue, destValue)

        path_to_start = []
        path_to_dest = []
        findPath(lca, startValue, path_to_start)
        findPath(lca, destValue, path_to_dest)

        directions = "U" * len(path_to_start) + "".join(path_to_dest)
        return directions


sol = Solution()
