year = int(input())  # 8989-9012 # 1001-1023
counter = 0
current_digit = 0
is_found = True
while True:
    for digit in str(year):
        digit_as_int = int(digit)
        if counter == 0:
            current_digit = digit_as_int
        elif current_digit == digit_as_int:
            is_found = False
            break
        counter += 1
    year += 1
    counter = 0
    if is_found:
        break
print(year)
