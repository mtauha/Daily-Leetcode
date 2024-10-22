# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """
            Given a string s, return the maximum number of unique substrings that the given string can be split into.
            You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
            A substring is a contiguous sequence of characters within a string.
        """
        if not root:
            return -1
        
        levels = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levels.append(level_sum)
        
        levels.sort(reverse=True)
        print(levels)
        return levels[k-1] if k-1 < len(levels) else -1
