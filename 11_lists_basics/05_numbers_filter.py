# n = int(input())
# command_even = "even"
# command_odd = "odd"
# command_negative = "negative"
# command_positive = "positive"
# numbers_list = [int(input()) for _ in range(n)]
# checking_numbers = []
# command = input()
# for i in numbers_list:
#     checking_command = (command == command_even and i % 2 == 0) \
#                or (command == command_odd and i % 2 != 0) \
#                or (command == command_negative and i < 0) \
#                or (command == command_positive and i >= 0)
#     if checking_command:
#         checking_numbers.append(i)
# print(checking_numbers)

number_lines = int(input())

numbers_to_list = []
check_list = []

for i in range(number_lines):
    number = int(input())
    numbers_to_list.append(number)

command = input()

for j in numbers_to_list:

    if command == 'even' and j % 2 == 0:
        check_list.append(j)
    elif command == 'odd' and j % 2 != 0:
        check_list.append(j)
    elif command == 'negative' and j < 0:
        check_list.append(j)
    elif command == 'positive' and j >= 0:
        check_list.append(j)

print(check_list)
