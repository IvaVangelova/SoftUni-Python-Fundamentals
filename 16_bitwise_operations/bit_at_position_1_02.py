def bit_at_position(number: int) -> int:
    """ Checking the number bit position """
    shifted_number = number >> 1
    lsb = shifted_number & 1
    return lsb


print(bit_at_position(int(input())))
