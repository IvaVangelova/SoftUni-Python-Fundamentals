""" Creating a function yo see if number is even """


def is_even(numbers: int):
    """ Return True if number is even"""
    return numbers % 2 == 0


sequence_of_numbers = [int(number) for number in input().split()]
result = list(filter(is_even, sequence_of_numbers))
print(result)
