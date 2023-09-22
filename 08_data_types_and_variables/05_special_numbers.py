number = int(input())
is_special = False
for i in range(1, number + 1):
    split_digit = i
    total_digit = 0
    for j in str(i):
        current_digit = int(j)
        total_digit += current_digit
        if total_digit == 5 or total_digit == 7 or total_digit == 7:
            is_special = True
    print(f"{i} -> {is_special}")
    is_special = False
       