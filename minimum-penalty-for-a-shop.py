class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = curr_penalty = sum(1 for i in customers if i == 'Y')
        earliest_hour = 0

        for curr_hour in range(len(customers)):
            if customers[curr_hour] == 'Y':
                curr_penalty -= 1
            else:
                curr_penalty += 1
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                earliest_hour = curr_hour + 1
        
        return earliest_hour
