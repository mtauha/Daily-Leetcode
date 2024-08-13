"""Description:
  Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

  Each number in candidates may only be used once in the combination.
  
  Note: The solution set must not contain duplicate combinations.
"""

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start, target, path):
            if target == 0:
                ans.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                
                backtrack(i + 1, target - candidates[i], path+[candidates[i]])            
        
        candidates.sort()
        ans = []
        backtrack(0, target, [])
        return ans
            
