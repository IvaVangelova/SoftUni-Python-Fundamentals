""" Check if first_sequence is in second_sequence """
first_sequence = input().split(", ")
second_sequence = input().split(", ")
new_list_of_strings = []
for string in first_sequence:
    for current_string in second_sequence:
        if string in current_string:
            if string not in new_list_of_strings:
                new_list_of_strings.append(string)


print(new_list_of_strings)
