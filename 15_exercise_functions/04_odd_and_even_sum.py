""" Finding odd sum and even sum in number as string """


def odd_and_even_sum(current_number: str) -> int and str:
    """ Finding odd sum and even sum """
    odd_sum = 0
    even_sum = 0
    for digit in current_number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_as_string = input()
print(odd_and_even_sum(number_as_string))

# def odd_and_even(number: str) -> int and int:
#     odd_sum = 0
#     even_sum = 0
#     for digit in number:
#         if int(digit) % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#     return odd_sum, even_sum
# some_number_as_string = input()
# odd_sum_digit, even_sum_digit = odd_and_even(some_number_as_string)
# print(f"Odd sum = {odd_sum_digit}, Even sum = {even_sum_digit}")
