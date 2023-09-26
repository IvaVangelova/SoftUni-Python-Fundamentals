key = int(input())
number_of_lines = int(input())
decryting_word = ''
for i in range(number_of_lines):
    character = ord(input())
    current_sum = key + character
    decryting_word += chr(current_sum)

print(decryting_word)
