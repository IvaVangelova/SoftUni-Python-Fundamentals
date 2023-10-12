""" Binary Digit Count. We will create function and count the binary digit in it """


def count_function(current_number: int, digit: int) -> int:
    """ Create a counter and check the current number """
    counter = 0
    while current_number > 0:
        remainder = current_number % 2
        current_number = current_number // 2

        if remainder == digit:
            counter += 1
    return counter


number = int(input())
binary_digit = int(input())
print(count_function(number, binary_digit))
