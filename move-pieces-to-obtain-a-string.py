class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """
            You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

            The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
            The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
            Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.
        """
        if start.replace('_', '') != target.replace('_', ''):
            return False


        start_pointer, target_pointer = 0, 0
        while start_pointer < len(start) and target_pointer < len(target):
            while start_pointer < len(start) and start[start_pointer] == '_':
                start_pointer += 1

            
            while target_pointer < len(target) and target[target_pointer] == '_':
                target_pointer += 1
            
            if start_pointer >= len(start) and target_pointer >= len(target):
                return True
            
            
            if start_pointer >= len(start) or target_pointer >= len(target):
                return True

            if start[start_pointer] != target[target_pointer]:
                return False
            
            if start[start_pointer] == 'L' and start_pointer < target_pointer:
                return False
            if start[start_pointer] == 'R' and start_pointer > target_pointer:
                return False
            
            start_pointer += 1
            target_pointer += 1
            
        return True
