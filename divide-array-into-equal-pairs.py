class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for i in counter.keys():
            if (counter[i]%2)%2 != 0:
                return False
        
        return True
