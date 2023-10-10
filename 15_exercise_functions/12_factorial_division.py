""" Finding the factorial division """


def calculate_factorial(first: int, second: int) -> int:
    """ Calculating the factorial of each number """
    first_result = 1
    for i in range(2, first + 1):
        first_result *= i
    second_result = 1
    for i in range(2, second + 1):
        second_result *= i
    return first_result, second_result


first_number = int(input())
second_number = int(input())
result_one, result_two = calculate_factorial(first_number, second_number)
result = result_one / result_two
print(f"{result:.2f}")
