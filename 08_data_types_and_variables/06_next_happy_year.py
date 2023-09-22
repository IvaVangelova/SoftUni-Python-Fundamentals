year = int(input())
while True:
    year += 1
    year_as_string = str(year)
    counter = 1
    for digit in year_as_string:
        if year_as_string.count(digit) > 1:
            counter += 1
            break
    if counter == 1:
        break
print(year)


# year = int(input())
# while True:
#     year += 1
#     year_as_string = str(year)
#     if len(year_as_string) == len(set(year_as_string)):
#         break
# print(year)
