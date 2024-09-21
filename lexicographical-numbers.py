class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
            Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
            You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
        """
      
        ans = []
        currentNumber = 1
        for _ in range(n):
            ans.append(currentNumber)

            if currentNumber*10 <= n:
                currentNumber *= 10
            else:
                while currentNumber%10 == 9 or currentNumber >= n:
                    currentNumber //= 10
                    
                currentNumber += 1
        
        return ans
