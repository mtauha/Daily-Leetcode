class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_dict = defaultdict(int)
        ans = []

        for num in nums:
            count_dict[num] += 1
            if count_dict[num] > 1:
                ans.append(num)

        return ans
