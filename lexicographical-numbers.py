class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
            This is the brute force approach in which you append all the 10th place integers then 10th and 1 place and so on.
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
        
    def lexicalOrder2(self, n: int) -> List[int]:
        """
            This is a Trie approach in which we just make a tree out of each and every integer exclusively til 10.
            WE stop generating tree when all numbers are generated till n
            Then we parse through the whole trie and using Depth First search and store the search in array.

            This way we get all the number lexicographically arranged
        """ 
        def lex(start, limit, arr):
            if start > limit:
                return
            
            arr.append(start)
            
            for i in range(10):
                generated = start*10 + i

                if generated <= limit:
                    lex(generated, limit, arr)
                else:
                    break
        
        ans = []
        for i in range(1, 10):
            lex(i, n, ans)

        return ans

            
