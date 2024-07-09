"""Description:
    There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

    arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
    timei is the time needed to prepare the order of the ith customer.
    When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

    Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
"""


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        time = []
        current_time = 0

        for customer in customers:
            arrival_time, preparation_time = customer

            current_time = max(current_time, arrival_time)

            waiting_time = current_time + preparation_time - arrival_time

            current_time += preparation_time

            time.append(waiting_time)

        return sum(time) / len(time)
