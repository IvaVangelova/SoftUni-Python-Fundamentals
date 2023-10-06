def calculation(operator, number_1, number_2):

    if operator == "multiply":
        return number_1 * number_2
    elif operator == "divide":
        return number_1 / number_2
    elif operator == "add":
        return number_1 + number_2
    elif operator == "subtract":
        return number_1 - number_2


operator_string = input()
num_1 = int(input())
num_2 = int(input())
print(int(calculation(operator_string, num_1, num_2)))
