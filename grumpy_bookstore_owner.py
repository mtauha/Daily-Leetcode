"""Description:
    There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

    On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

    When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

    The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

    Return the maximum number of customers that can be satisfied throughout the day.
"""

class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        if len(customers) <= 1 and (minutes >= 1 or not grumpy[0]):
            return customers[0]
        
        always_happy_customers = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        
        max_additional_happy_customers = 0
        current_additional_happy_customers = 0

        for i in range(len(customers)):
            if grumpy[i] == 1:
                current_additional_happy_customers += customers[i]
            
            if i >= minutes and grumpy[i - minutes] == 1:
                current_additional_happy_customers -= customers[i - minutes]

            max_additional_happy_customers = max(max_additional_happy_customers, current_additional_happy_customers)
        
        total_happy_customers = always_happy_customers + max_additional_happy_customers
        return total_happy_customers


sol = Solution()
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
print(sol.maxSatisfied(customers, grumpy, minutes))
