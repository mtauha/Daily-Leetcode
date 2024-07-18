"""Description:
    You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

    Return the number of good leaf node pairs in the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0

        def dfs(node: TreeNode):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for i in left_dist:
                for j in right_dist:
                    if i + j <= distance:
                        self.pairs += 1

            all_dist = left_dist + right_dist

            return [d + 1 for d in all_dist]

        dfs(root)

        return self.pairs


sol = Solution()
