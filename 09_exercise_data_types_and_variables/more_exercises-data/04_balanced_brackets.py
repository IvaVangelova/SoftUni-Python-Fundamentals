number_of_lines = int(input())
open_bracket_count = 0
closed_bracket_count = 0

for line in range(number_of_lines):
    bracket_or_string = input()

    if bracket_or_string == '(':
        open_bracket_count += 1

        if closed_bracket_count == 0 and open_bracket_count > 1:
            break
    elif bracket_or_string == ')':
        closed_bracket_count += 1
        
        if open_bracket_count == 0:
            break

if open_bracket_count == closed_bracket_count:
    print("BALANCED")
else:
    print("UNBALANCED")
