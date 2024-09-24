class TrieNode:
    def __init__(self):
        self.children = [None] * 10


class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, node, num):
        numStr = str(num)
        for i in numStr:
            idx = int(i)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]

    def findLongestPrefix(self, node, num):
        numStr = str(num)
        length = 0
        for digit in numStr:
            idx = int(digit)
            if node.children[idx]:
                length += 1
                node = node.children[idx]
            else:
                break
        
        return length

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
            You are given two arrays with positive integers arr1 and arr2.
            A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.
            A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.
            You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.
            Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.
        """
        ans = 0

        for i in arr1:
            self.insert(self.root, i)
        
        for i in arr2:
            ans = max(ans, self.findLongestPrefix(self.root, i))
        
        return ans
