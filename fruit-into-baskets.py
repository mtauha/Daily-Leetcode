class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        ans = 0
        ptr1 = 0
        curr_count = defaultdict(int)
        
        for ptr2 in range(n):
            curr_count[fruits[ptr2]] += 1

            while ptr1 < ptr2 and len(curr_count) > 2:
                curr_count[fruits[ptr1]] -= 1
                if curr_count[fruits[ptr1]] == 0:
                    curr_count.pop(fruits[ptr1])
                ptr1 += 1
            
            ans = max(ans, ptr2 - ptr1 + 1)
        
        return ans            
