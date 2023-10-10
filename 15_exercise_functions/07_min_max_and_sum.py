""" Finding min, max and sum """

numbers = [int(number) for number in input().split()]
min_number = min(numbers)
max_number = max(numbers)
sum_result = sum(numbers)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_result}")
