# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.ans = []
    def help_postorder(self, root: 'Node'):
        if not root:
            return
        
        for child in root.children:
            self.help_postorder(child)
        
        self.ans.append(root.val)
    
    def postorder(self, root: 'Node')->List[int]:
        """
          Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
          Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value  
        """
        if not root:
            return []
        
        self.help_postorder(root)

        return self.ans        
