def smallest_number(numbers: list) -> int:
    return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers_in_list = [first_number, second_number, third_number]
print(smallest_number(numbers_in_list))
