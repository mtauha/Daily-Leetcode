class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """
            You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

            The chosen integers have to be in the range [1, n].
            Each integer can be chosen at most once.
            The chosen integers should not be in the array banned.
            The sum of the chosen integers should not exceed maxSum.
            Return the maximum number of integers you can choose following the mentioned rules.
        """
        banned.sort()
        chosen = []
        current_max = 0
        count = 0
        def not_in(value, arr):
            low, high = 0, len(arr) -1 
            while low <= high:
                mid = (high+low)//2

                if arr[mid] == value:
                    return False
                
                if arr[mid] < value:
                    low = mid + 1
                else:
                    high = mid - 1
                
            
            return True
        
        for i in range(1, n+1):
            if not_in(i,  banned) and not_in(i, chosen):
            
                chosen.append(i)
                if current_max + i > maxSum:
                    print(count, current_max+i)
                    return count 
                else:
                    count += 1
                    current_max += i
                    
        
        return count
        
      
