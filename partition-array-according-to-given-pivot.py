class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        new_nums = []
        count = 0
        for _ in range(2):
            for i in nums:
                if _ == 0:
                    if i < pivot:
                        new_nums.append(i)
                else:
                    if i > pivot:
                        new_nums.append(i)
                
                if i == pivot:
                    count += 1
            if _ == 0:
                for __ in range(count):
                    new_nums.append(pivot)

        return new_nums
            
