employees_happiness = [int(number) for number in input().split()]
factor = int(input())
multiply_happiness = [person * factor for person in employees_happiness]
average = sum(multiply_happiness) // len(multiply_happiness)
happy_count = [happy_employ for happy_employ in multiply_happiness if happy_employ > average]

if len(happy_count) >= len(multiply_happiness) // 2:
    print(f"Score: {len(happy_count)}/{len(multiply_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(multiply_happiness)}. Employees are not happy!")
