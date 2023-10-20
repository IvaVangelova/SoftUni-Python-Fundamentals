""" Create function to check numbers """


def check_numbers(numbers: list):
    """ Checking if number is positive, negative, odd or even"""
    positive_numbers = []
    negative_numbers = []
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number >= 0:
            if number % 2 == 0:
                even_numbers.append(str(number))
            else:
                odd_numbers.append(str(number))
            positive_numbers.append(str(number))
        else:
            if number % 2 != 0:
                odd_numbers.append(str(number))
            else:
                even_numbers.append(str(number))
            negative_numbers.append(str(number))
    return f"Positive: {', '.join(positive_numbers)}" \
           f"\nNegative: {', '.join(negative_numbers)}" \
           f"\nEven: {', '.join(even_numbers)}\nOdd: {', '.join(odd_numbers)}"


list_of_numbers = [int(number) for number in input().split(", ")]
result = check_numbers(list_of_numbers)
print(result)
