class Solution:
    def replaceValueInTree(self, root):
        """
            Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
            Two nodes of a binary tree are cousins if they have the same depth with different parents.
            Return the root of the modified tree.
            Note that the depth of a node is the number of edges in the path from the root node to it.
        """
        if root is None:
            return root
        node_queue = deque()
        node_queue.append(root)
        previous_level_sum = root.val

        while node_queue:
            level_size = len(node_queue)
            current_level_sum = 0

            for _ in range(level_size):
                current_node = node_queue.popleft()
                current_node.val = previous_level_sum - current_node.val

                sibling_sum = (
                    0 if current_node.left is None else current_node.left.val
                ) + (
                    0 if current_node.right is None else current_node.right.val
                )

                if current_node.left is not None:
                    current_level_sum += (
                        current_node.left.val
                    )
                    current_node.left.val = (
                        sibling_sum
                    )
                    node_queue.append(
                        current_node.left
                    ) 
                if current_node.right is not None:
                    current_level_sum += (
                        current_node.right.val
                    )
                    current_node.right.val = (
                        sibling_sum 
                    )
                    node_queue.append(
                        current_node.right
                    ) 
            previous_level_sum = current_level_sum
        return root
