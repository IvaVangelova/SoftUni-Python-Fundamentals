factor = int(input())
count = int(input())
numbers_list = []

for number in range(1, count + 1):

    current_number = number * factor
    numbers_list.append(current_number)

print(numbers_list)
