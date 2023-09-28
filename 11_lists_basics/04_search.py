number = int(input())
special_word = input()
strings_list = []
modified_list = []
for _ in range(number):
    current_string = input()
    strings_list.append(current_string)

print(strings_list)

for i in strings_list:
    if special_word in i:
        modified_list.append(i)

print(modified_list)
