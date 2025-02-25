class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count, prefix_sum = 0, 0
        odd_count = 0
        even_count = 1
        MOD = 10**9 + 7

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1

            count %= MOD 
        
        return count
