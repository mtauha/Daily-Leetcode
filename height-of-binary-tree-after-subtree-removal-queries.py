class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        """
            You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

            You have to perform m independent queries on the tree where in the ith query you do the following:
            
            Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
            Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.
            
            Note:
            The queries are independent, so the tree returns to its initial state after each query.
            The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
        """
        node_depths = {}
        subtree_heights = {}

        first_largest_height = {}
        second_largest_height = {}

        def _dfs(node, level):
            if not node:
                return 0

            node_depths[node.val] = level

            left_height = _dfs(node.left, level + 1)
            right_height = _dfs(node.right, level + 1)
            current_height = 1 + max(left_height, right_height)

            subtree_heights[node.val] = current_height

            if current_height > first_largest_height.get(level, 0):
                second_largest_height[level] = first_largest_height.get(
                    level, 0
                )
                first_largest_height[level] = current_height
            elif current_height > second_largest_height.get(level, 0):
                second_largest_height[level] = current_height

            return current_height

        _dfs(root, 0)

        return [
            node_depths[q]
            + (
                second_largest_height.get(node_depths[q], 0)
                if subtree_heights[q] == first_largest_height[node_depths[q]]
                else first_largest_height.get(node_depths[q], 0)
            )
            - 1
            for q in queries
        ]
