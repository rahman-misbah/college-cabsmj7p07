# Initial input
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squaring numbers using map
squared_nums = list(map(lambda x: x**2, numbers))

# Finding odd numbers using filter
odd_nums = list(filter(lambda x: x & 1, numbers))

# Print results
print("Squared Numbers:", squared_nums)
print("Odd Numbers:", odd_nums)