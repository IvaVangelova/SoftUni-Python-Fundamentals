""" Destroying bit digit from number """


def bit_destroyer(number: int, position: int) -> int:
    """ Reversing the bit number and changing the  position """
    mask = 1 << position
    mask = ~mask
    result = number & mask
    return result


current_number = int(input())
bit_position = int(input())
print(bit_destroyer(current_number, bit_position))
