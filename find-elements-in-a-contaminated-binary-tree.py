# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.generate(root, 0)
    
    def generate(self, node: TreeNode, value: int):
        if node is None:
            return
        self.seen.add(value)
        self.generate(node.left, 2*value + 1)
        self.generate(node.right, 2*value + 2)

    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
