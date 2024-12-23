class Solution:
    def minimumOperations(self, root: Optional["TreeNode"]) -> int:
        """
            You are given the root of a binary tree with unique values.

            In one operation, you can choose any two nodes at the same level and swap their values.

            Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

            The level of a node is the number of edges along the path between it and the root node.
        """
        queue = deque([root])
        total_swaps = 0

        # Process tree level by level using BFS
        while queue:
            level_size = len(queue)
            level_values = []

            # Store level values and add children to queue
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add minimum swaps needed for current level
            total_swaps += self._get_min_swaps(level_values)

        return total_swaps

    # Calculate minimum swaps needed to sort an array
    def _get_min_swaps(self, original: list) -> int:
        swaps = 0
        target = sorted(original)

        # Map to track current positions of values
        pos = {val: idx for idx, val in enumerate(original)}

        # For each position, swap until correct value is placed
        for i in range(len(original)):
            if original[i] != target[i]:
                swaps += 1

                # Update position of swapped values
                cur_pos = pos[target[i]]
                pos[original[i]] = cur_pos
                original[cur_pos] = original[i]

        return swaps
