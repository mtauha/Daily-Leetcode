from itertools import combinations

def subsets(List):
    result = []
    for i in range(len(List) + 1):
        result.extend([list(subset) for subset in combinations(List, i)])

    return result

def xor(List):
    ans = 0
    for i in List:
        ans = ans^i
    
    return ans

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        lists = subsets(nums)
        xors = []
        for i in lists:
            xors.append(xor(i))
        
        return sum(xors)




sol = Solution()
nums = [1, 3]
print(subsets(nums))
print(sol.subsetXORSum(nums))
