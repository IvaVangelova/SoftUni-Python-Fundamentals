""" Shifting p-times bit number to see digit """


def shifting_to_p(number: int, digit: int) -> int:
    """ Shift number and check digit """
    shifted_number = number >> digit

    bit_at_position = shifted_number & 1

    return bit_at_position


current_number = int(input())
bit_digit = int(input())
print(shifting_to_p(current_number, bit_digit))
