class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = list(str(num))

        for idx, dig in enumerate(num_list):
            if dig == '6':
                num_list[idx] = '9'
                break
        
        return int(''.join(num_list))
