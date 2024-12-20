# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

        For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
        Return the root of the reversed tree.

        A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

        The level of a node is the number of edges along the path between it and the root node.
    """
    def reverseOddLevels(self, root) -> TreeNode:
        self.__traverse_DFS(root.left, root.right, 0)
        return root

    def __traverse_DFS(self, left_child, right_child, level):
        if left_child is None or right_child is None:
            return
        # If the current level is odd, swap the values of the children.
        if level % 2 == 0:
            temp = left_child.val
            left_child.val = right_child.val
            right_child.val = temp

        self.__traverse_DFS(left_child.left, right_child.right, level + 1)
        self.__traverse_DFS(left_child.right, right_child.left, level + 1)   
