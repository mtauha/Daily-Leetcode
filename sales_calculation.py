from collections import Counter

# Reading input
total_shoes = int(input())
available_sizes = list(map(int, input().split()))
num_customers = int(input())
customer_requests = []

# Reading customer requests
for _ in range(num_customers):
    size, price = map(int, input().split())
    customer_requests.append((size, price))

# Counting available shoe sizes
shoes_counter = Counter(available_sizes)

# Total earnings
earnings = 0

# Iterating over customer requests
for size, price in customer_requests:
    if shoes_counter[size] > 0:
        earnings += price
        shoes_counter[size] -= 1

print(earnings)


# *

""" 
Description:

Ali is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Ali earned. """
